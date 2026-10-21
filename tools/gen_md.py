"""Генерирует читаемые MD-таблицы из сырого JSON-экспорта Grist.

Запуск из корня репозитория: python3 tools/gen_md.py data/raw data/md
"""
import json, os, re, sys, datetime
from collections import OrderedDict, defaultdict

RAW, OUT = sys.argv[1], sys.argv[2]


def load(name):
    with open(os.path.join(RAW, name + ".json"), encoding="utf-8") as f:
        return json.load(f)["records"]


def by_id(name):
    return {r["id"]: r["fields"] for r in load(name)}


def esc(v):
    if v is None:
        return ""
    s = str(v).replace("|", "\\|").replace("\r", "")
    return s.replace("\n", "<br>").strip()


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(esc(c) for c in r) + " |")
    return "\n".join(out) + "\n"


def write(path, text):
    p = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")


def slug(s):
    tr = dict(zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                  ["a","b","v","g","d","e","e","zh","z","i","y","k","l","m","n","o","p","r","s","t","u","f","h","c","ch","sh","sch","","y","","e","yu","ya"]))
    s = "".join(tr.get(c, c) for c in s.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def date(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).strftime("%Y-%m-%d") if ts else "—"


cat = by_id("Katalog")
people = by_id("Personazhi")
handle = {i: p["Handle"] for i, p in people.items()}
index = []

# ---------------- Каталог по категориям
COLS = [("Subcategory", "Подкатегория"), ("Cost", "Цена, eb"), ("PriceCat", "Ценовая кат."), ("Damage", "Урон"), ("ROF", "ROF"),
        ("Magazine", "Магазин"), ("Hands", "Рук"), ("Skill", "Навык"), ("AmmoType", "Боеприпас"), ("Features", "Особенности"),
        ("SP", "SP"), ("ArmorPenalty", "Штраф брони"), ("ProgramClass", "Класс"), ("ATK", "ATK"), ("DEF", "DEF"), ("REZ", "REZ"),
        ("HumanityLossText", "Потеря человечности"), ("Requires", "Требует"), ("Install", "Установка"), ("OptionSlots", "Слотов даёт"),
        ("Slots", "Слотов занимает"), ("Page", "Стр.")]
groups = defaultdict(list)
for i, r in sorted(cat.items()):
    groups[r["Category"]].append(r)
cat_index = []
for c, items in sorted(groups.items()):
    use = [(k, h) for k, h in COLS if any(r.get(k) not in (None, "", 0, False) for r in items)]
    rows = [[r["NameRu"] or r["Name"], r["Name"]] + [r.get(k, "") if r.get(k) not in (None, 0, False) or k == "Cost" else "" for k, _ in use] for r in items]
    text = f"# {c}\n\nПредметов: {len(items)}. Источник: таблица `Katalog` (Grist).\n\n" + table(["Название", "Name"] + [h for _, h in use], rows)
    text += "\n## Описания\n\n"
    for r in items:
        text += f"### {r['NameRu'] or r['Name']} · _{r['Name']}_\n\n"
        for k, h in (("Opisanie", None), ("Effect", "Эффект"), ("NotesRu", "Примечание")):
            if r.get(k):
                text += (f"**{h}:** " if h else "") + str(r[k]).strip() + "\n\n"
    fn = f"katalog/{slug(c)}.md"
    write(fn, text)
    cat_index.append((c, len(items), fn))
index.append(("Каталог предметов", [(f"{c} ({n})", fn) for c, n, fn in cat_index]))

# ---------------- Справочники
skills = load("SpravochnikNavykov")
t = "# Навыки\n\nСправочник навыков (68). **x2** — навык стоит двойную цену, **множ.** — берётся отдельно под язык/науку/инструмент и т.п.\n\n"
bycat = OrderedDict()
for r in skills:
    bycat.setdefault(r["fields"]["Category"], []).append(r["fields"])
for c, rs in bycat.items():
    t += f"## {c}\n\n" + table(["Навык", "Name", "Стат", "x2", "Множ.", "Описание"],
        [[f["NameRu"], f["Name"], f["Stat"], "да" if f["Double"] else "", "да" if f["Multiple"] else "", f["Opisanie"]] for f in rs]) + "\n"
write("mehanika/navyki.md", t)

t = "# Роли\n\n"
for r in load("Roli"):
    f = r["fields"]
    t += f"## {f['Role']} — {f['RoleAbility']} (ранг {f['AbilityRank']}, стр. {f['Page']})\n\n{f['OpisanieRoli']}\n\n**Способность.** {f['OpisanieAbility']}\n\n"
write("mehanika/roli.md", t)

t = "# Действия в NET\n\n"
kinds = OrderedDict()
for r in load("NetDeystviya"):
    kinds.setdefault(r["fields"]["Kind"], []).append(r["fields"])
for k, rs in kinds.items():
    t += f"## {k}\n\n" + table(["Название", "Name", "Стоимость", "Бросок", "Описание", "Стр."],
        [[f["NameRu"], f["Name"], f["Costs"], f["Rolls"], f["Opisanie"], f["Page"]] for f in rs]) + "\n"
write("mehanika/net-deystviya.md", t)

t = "# Бонусы имплантов\n\nЧисловые бонусы хрома (`BonusyKibera`). «Условие» — когда бонус действует.\n\n"
rows = []
for r in load("BonusyKibera"):
    f = r["fields"]
    it = cat.get(f["Item"], {})
    rows.append([it.get("NameRu") or it.get("Name") or f["Item"], f["Target"], f["SkillName"] or f["Stat"], f["Value"], f["Condition"] or "всегда", f["Note"]])
t += table(["Имплант", "Что даёт", "Навык/стат", "Знач.", "Условие", "Примечание"], rows)
write("mehanika/bonusy-kibera.md", t)

t = "# Языки по регионам\n\n"
reg = OrderedDict()
for r in load("Yazyki"):
    reg.setdefault(r["fields"]["RegionRu"], []).append(r["fields"])
for k, rs in reg.items():
    t += f"## {k}\n\n" + ", ".join(f"{f['NameRu']} ({f['Name']})" for f in rs) + "\n\n"
write("mehanika/yazyki.md", t)

t = "# Лайфпас\n\nТаблицы бросков для создания предыстории (`Lifepath`).\n\n"
lp = OrderedDict()
for r in sorted(load("Lifepath"), key=lambda r: (r["fields"]["CatOrder"], r["fields"]["Role"], r["fields"]["Roll"])):
    f = r["fields"]
    lp.setdefault((f["Category"], f["Role"]), []).append(f)
for (c, role), rs in lp.items():
    t += f"## {c}" + (f" — {role}" if role else "") + "\n\n" + table(["Бросок", "Результат"], [[f["Roll"], f["TextRu"]] for f in rs]) + "\n"
write("mehanika/lifepath.md", t)

# ---------------- Шаблоны ролей (создание персонажа)
t = "# Шаблоны ролей\n\nСтатистика и стартовый набор по ролям (метод Streetrat).\n\n"
stats = defaultdict(list)
for r in load("ShablonStats"):
    stats[r["fields"]["Role"]].append(r["fields"])
sk = defaultdict(list)
for r in load("ShablonNavyki"):
    sk[r["fields"]["Role"]].append(r["fields"])
gear = defaultdict(list)
for r in load("ShablonSnaryaga"):
    gear[r["fields"]["Role"]].append(r["fields"])
for role in stats:
    t += f"## {role}\n\n### Статы (бросок d10)\n\n" + table(["d10", "INT", "REF", "DEX", "TECH", "COOL", "WILL", "LUCK", "MOVE", "BODY", "EMP"],
        [[f["Roll"]] + [f[k] for k in "INT REF DEX TECH COOL WILL LUCK MOVE BODY EMP".split()] for f in sorted(stats[role], key=lambda f: f["Roll"])])
    t += "\n### Навыки\n\n" + table(["Навык", "Уровень", "Уточнение"],
        [[(cat_sk := next((s for s in skills if s["fields"]["Name"] == f["SkillName"]), None)) and cat_sk["fields"]["NameRu"] + f" ({f['SkillName']})" or f["SkillName"], f["Lvl"], f["Spec"]] for f in sk[role]])
    t += "\n### Снаряжение\n\nСтрока с «Выбор» — выбирается один вариант из группы.\n\n" + table(["Предмет", "Кол.", "Тип", "Выбор", "Примечание", "HL"],
        [[(cat.get(f["Item"], {}).get("NameRu") or "") + (f" · _{f['ItemName']}_" if cat.get(f["Item"], {}).get("NameRu") else f["ItemName"]), f["Qty"], f["Kind"],
          (f["ChoiceGroup"] + ": " + f["ChoiceOption"]) if f["ChoiceGroup"] else "", f["Note"], f["HL"] or ""] for f in gear[role]]) + "\n"
write("mehanika/shablony-roley.md", t)

# ---------------- Персонажи
navyki = load("Navyki")
inv = load("Inventar")
for pid, p in sorted(people.items()):
    h = p["Handle"]
    t = f"# {h} — {p['Role']}\n\nИгрок: {p['Player'] or '—'} · {p['RoleAbility']}, ранг {p['RoleRank']}\n\n"
    t += "## Характеристики\n\n" + table("INT REF DEX TECH COOL WILL LUCK MOVE BODY EMP".split(), [[p[k] for k in "INT REF DEX TECH COOL WILL LUCK MOVE BODY EMP".split()]])
    t += "\n## Состояние\n\n" + table(["HP", "Броня (голова/тело)", "Штраф брони", "Человечность", "EMP", "Состояние", "Эдди", "IP свободно", "Репутация"],
        [[f"{p['HP']}/{p['HP_max']}", f"{p['Armor_head']}/{p['Armor_body']}", p["ArmorPenalty"], f"{p['Humanity']}/{p['HumanityMax']}", p["EMP_rules"], p["WoundState"], p["Eddies"], p["IP_left"], p["Rep"]]])
    t += f"\nТяжёлое ранение с {p['SeriouslyWounded']} HP · Death Save {p['DeathSave']} · заработано IP {p['IP_earned']}, потрачено {p['IP_spent']}\n"
    mine = sorted([r["fields"] for r in navyki if r["fields"]["Person"] == pid and r["fields"]["Lvl"] > 0], key=lambda f: (f["Category"], -f["Lvl"]))
    t += "\n## Навыки\n\n" + table(["Категория", "Навык", "Стат", "Ур.", "Итого"], [[f["Category"], f["NameRu"], f["Stat"], f["Lvl"], f["Base"] + (f["BonusSum"] or 0)] for f in mine])
    mi = [r["fields"] for r in inv if r["fields"]["Person"] == pid]
    def nm(f):
        it = cat.get(f["Item"], {})
        return f["CustomName"] or it.get("NameRu") or it.get("Name") or f["Item"]
    def cg(f):
        return cat.get(f["Item"], {}).get("Category", "Кастом")
    owned = [f for f in mi if not f["Sold"]]
    sold = [f for f in mi if f["Sold"]]
    t += "\n## Снаряжение и хром\n\n"
    for c in sorted({cg(f) for f in owned}):
        t += f"### {c}\n\n" + table(["Предмет", "Кол.", "Слот", "Вживлён", "Заметки"],
            [[nm(f), f["Qty"], f["Slot"], "да" if f["Installed"] else "", f["Notes"]] for f in owned if cg(f) == c]) + "\n"
    if sold:
        t += "### Продано\n\n" + table(["Предмет", "Цена, eb"], [[nm(f), f["SoldFor"]] for f in sold]) + "\n"
    t += "## Предыстория\n\n"
    for k, lab in (("Culture", "Культура"), ("Languages", "Языки"), ("Personality", "Характер"), ("ClothingStyle", "Стиль одежды"), ("Hairstyle", "Причёска"),
                   ("Affectation", "Причуда"), ("Motivation", "Мотивация"), ("FamilyBackground", "Семья"), ("ChildhoodEnv", "Детство"),
                   ("FamilyCrisis", "Семейный кризис"), ("Enemies", "Враги"), ("LoveAffairs", "Романы"), ("RoleLifepath", "Лайфпас роли"), ("Notes", "Заметки")):
        if p.get(k):
            t += f"- **{lab}:** {str(p[k]).strip()}\n"
    write(f"personazhi/{slug(h)}.md", t)
index.append(("Персонажи", [(f"{p['Handle']} — {p['Role']}", f"personazhi/{slug(p['Handle'])}.md") for _, p in sorted(people.items())]))

# ---------------- История игры
nid = {r["id"]: r["fields"] for r in navyki}
t = "# История игры\n\n## Начисления\n\n" + table(["Кому", "Что", "Сколько", "За что", "Когда"],
    [[handle.get(r["fields"]["Person"]), r["fields"]["Kind"], r["fields"]["Amount"], r["fields"]["Reason"], date(r["fields"]["Kogda"])] for r in load("Nachisleniya")])
t += "\n## Прокачка навыков\n\n" + table(["Кому", "Навык", "До уровня", "Цена, IP", "Когда"],
    [[handle.get(r["fields"]["Person"]), nid.get(r["fields"]["Skill"], {}).get("NameRu", r["fields"]["Skill"]), r["fields"]["ToLvl"], r["fields"]["Cost"], date(r["fields"]["Kogda"])] for r in load("Prokachka")])
t += "\n## Терапия\n\n" + table(["Кому", "Тип", "Где", "Выпало", "Эффект", "Цена, eb", "Лечил", "Когда"],
    [[handle.get(r["fields"]["Person"]), r["fields"]["Kind"], r["fields"]["Where"], r["fields"]["Rolled"], r["fields"]["Effect"], r["fields"]["Cost"],
      handle.get(r["fields"]["Medtech"], ""), date(r["fields"]["Kogda"])] for r in load("Terapiya")])
write("istoriya.md", t)

index.append(("Механики и справочники", [("Навыки", "mehanika/navyki.md"), ("Роли", "mehanika/roli.md"), ("Действия в NET", "mehanika/net-deystviya.md"),
    ("Бонусы имплантов", "mehanika/bonusy-kibera.md"), ("Языки", "mehanika/yazyki.md"), ("Лайфпас", "mehanika/lifepath.md"),
    ("Шаблоны ролей", "mehanika/shablony-roley.md")]))
index.append(("Ход игры", [("История игры: начисления, прокачка, терапия", "istoriya.md")]))

t = "# Cyberpunk RED — данные кампании\n\nЧитаемая выгрузка из Grist (документ «Cyberpunk RED — Команда»). Сырой JSON лежит в [`../raw`](../raw).\n\n"
for title, items in index:
    t += f"## {title}\n\n" + "\n".join(f"- [{n}]({fn})" for n, fn in items) + "\n\n"
write("README.md", t)
print("ok")
