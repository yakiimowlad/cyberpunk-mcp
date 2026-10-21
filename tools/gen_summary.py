"""Собирает один компактный справочник мастера из сырого JSON-экспорта Grist.

Запуск из корня репозитория: python3 tools/gen_summary.py data/raw docs/gm-spravochnik.md
"""
import json, os, re, sys
from collections import defaultdict

RAW, OUT = sys.argv[1], sys.argv[2]


def load(name):
    with open(os.path.join(RAW, name + ".json"), encoding="utf-8") as f:
        return json.load(f)["records"]


def esc(v):
    return str(v if v is not None else "").replace("|", "/").replace("\n", " ").strip()


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows]
    return "\n".join(out) + "\n"


def short(s, n=110):
    s = re.sub(r"\s+", " ", s or "").strip()
    m = re.match(r"(.{20,%d}?[.!?])(\s|$)" % n, s)
    if m:
        return m.group(1)
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"


cat = {r["id"]: r["fields"] for r in load("Katalog")}
people = {r["id"]: r["fields"] for r in load("Personazhi")}
navyki = [r["fields"] for r in load("Navyki")]
inv = [r["fields"] for r in load("Inventar")]
by_cat = defaultdict(list)
for f in cat.values():
    by_cat[f["Category"]].append(f)
nm = lambda f: f["NameRu"] or f["Name"]
t = []

t.append("""# Cyberpunk RED — справочник мастера

Одна страница со всем, что нужно при написании сюжета и сценариев сиквела. Собрано из таблиц Grist «Cyberpunk RED — Команда». Полные данные: `data/md/` (читаемо) и `data/raw/` (JSON).

## 1. Базовые формулы (сверено по листам команды)

- **HP** = 10 + 5 × округл.вверх((BODY + WILL) / 2). Тяжёлое ранение — при HP ≤ половины (округл. вверх), Death Save = BODY.
- **Человечность** (макс.) = EMP × 10 минус постоянные потери от хрома: 2 за имплант, 4 за боргвар. Терапия возвращает человечность до этого потолка.
- **Цены:** Cheap 10 · Everyday 20 · Costly 50 · Premium 100 · Expensive 500 · Very Expensive 1 000 · Luxury 5 000 · Super Luxury 10 000+ eb. Без Fixer'а покупается только до Premium; Fixer с Haggle даёт ±20%.
- **Качество оружия:** Excellent +1 к атаке (цена на ступень выше), Poor клинит при крит. провале (цена ниже). Exotic всегда Standard.
- **Оплата работ за человека:** лёгкая 500 · типичная 1 000 · опасная 2 000 eb.
- **Vendit** (автомат): товар 10–100 eb, сам автомат — укрытие Thick Steel с турелью-огнемётом.
- **NET-действия за ход** по рангу Interface: 1–3 → 2, 4–6 → 3, 7–9 → 4, 10 → 5. Либо одно Meat-действие, либо NET-действия; Move всегда.
- **Кибердека:** Poor 5 слотов (100 eb) · Standard 7 (500) · Excellent 9 (1 000). Программа — 1 слот, Black ICE — 2, Demon не влезает.
""")

# ---- команда
t.append("## 2. Команда (состояние на момент выгрузки)\n")
rows = []
for pid, p in sorted(people.items()):
    mine = sorted([f for f in navyki if f["Person"] == pid and f["Lvl"] >= 4], key=lambda f: -(f["Base"] + (f["BonusSum"] or 0)))
    top = ", ".join(f"{f['NameRu']} {f['Base'] + (f['BonusSum'] or 0)}" for f in mine[:4])
    mi = [f for f in inv if f["Person"] == pid and not f["Sold"]]
    cyber = ", ".join(nm(cat[f["Item"]]) for f in mi if f["Item"] in cat and cat[f["Item"]]["Category"] == "Cyberware" and f["Installed"])
    guns = ", ".join(nm(cat[f["Item"]]) for f in mi if f["Item"] in cat and cat[f["Item"]]["Category"] in ("Ranged Weapon", "Melee Weapon", "Exotic Weapon", "Branded Weapon"))
    rows.append([f"**{p['Handle']}** ({p['Player'] or '—'})", f"{p['Role']} {p['RoleRank']}", " ".join(f"{k}{p[k]}" for k in "INT REF DEX TECH COOL WILL LUCK MOVE BODY EMP".split()),
                 f"{p['HP']}/{p['HP_max']}", f"{p['Armor_head']}/{p['Armor_body']}", f"{p['Humanity']}/{p['HumanityMax']}", p["Eddies"], p["IP_left"], top, cyber or "—", guns or "—"])
t.append(table(["Персонаж", "Роль/ранг", "Статы", "HP", "SP г/т", "Человечн.", "Эдди", "IP", "Топ-навыки (итог)", "Вживлено", "Оружие"], rows))
t.append("### Крючки для сюжета: предыстории\n")
rows = []
for pid, p in sorted(people.items()):
    rows.append([p["Handle"], p["Culture"], p["Motivation"], short(p["FamilyBackground"], 120), short(p["FamilyCrisis"], 100), short(p["Enemies"], 100), short(p["RoleLifepath"], 120)])
t.append(table(["Кто", "Культура", "Мотивация", "Семья", "Семейный кризис", "Враги", "Лайфпас роли"], rows))

# ---- роли
t.append("## 3. Роли и способности (старт — ранг 4)\n")
t.append(table(["Роль", "Способность", "Суть"], [[r["fields"]["Role"], r["fields"]["RoleAbility"], short(r["fields"]["OpisanieAbility"], 230)] for r in load("Roli")]))

# ---- навыки
t.append("## 4. Навыки по категориям (стат; x2 — двойная цена)\n")
bc = defaultdict(list)
for r in load("SpravochnikNavykov"):
    f = r["fields"]
    bc[f["Category"]].append(f"{f['NameRu']} ({f['Stat']}{', x2' if f['Double'] else ''})")
for c, xs in bc.items():
    t.append(f"- **{c}:** " + "; ".join(xs))
t.append("\nБросок: СТАТ + НАВЫК + 1d10 против DV. Типовые DV: стабилизация раненого 10/13/15 (по Wound State), ремонт Minor 9 / Major 13 / Destroyed 17.\n")

# ---- нетраннинг
t.append("## 5. Нетраннинг\n")
t.append("### Действия\n")
t.append(table(["Что", "Цена", "Бросок", "Суть"], [[f"{r['fields']['NameRu']} ({r['fields']['Name']})", r["fields"]["Costs"], r["fields"]["Rolls"], short(r["fields"]["Opisanie"], 140)] for r in load("NetDeystviya")]))
t.append("### Программы\n")
t.append(table(["Программа", "Цена", "Класс", "ATK", "DEF", "REZ", "Эффект"], [[f["Name"], f["Cost"], f["ProgramClass"], f["ATK"], f["DEF"], f["REZ"], short(f["Effect"], 120)] for f in sorted(by_cat["Program"], key=lambda f: f["ProgramClass"])]))
t.append("### Black ICE и демоны\n")
t.append(table(["ICE", "Цена", "Класс", "ATK", "DEF", "REZ", "Эффект"], [[f["Name"], f["Cost"], f["ProgramClass"], f["ATK"], f["DEF"], f["REZ"], short(f["Effect"], 120)] for f in sorted(by_cat["Black ICE"], key=lambda f: (f["ProgramClass"], f["REZ"]))]))
t.append("### Архитектура (цена постройки)\n")
t.append(table(["Элемент", "Цена, eb"], [[f["Name"], f["Cost"]] for f in by_cat["NET Architecture"] if f["Cost"]]))

# ---- снаряжение
def gear(title, cname, cols, desc=None):
    t.append(f"### {title}\n")
    hdr = ["Название", "Цена"] + [h for h, _ in cols] + (["Суть"] if desc else [])
    rows = []
    for f in sorted(by_cat[cname], key=lambda f: (f["Cost"] or 0, f["Name"])):
        rows.append([f"{nm(f)}" + (f" · _{f['Name']}_" if f["NameRu"] else ""), f["Cost"] or ""] + [f[k] or "" for _, k in cols] + ([short(f["Opisanie"], desc)] if desc else []))
    t.append(table(hdr, rows))

def lst(title, cname):
    xs = sorted(by_cat[cname], key=lambda f: (f["Cost"] or 0, f["Name"]))
    t.append(f"- **{title}:** " + "; ".join(f"{nm(f)} {f['Cost']}" if f["Cost"] else nm(f) for f in xs))


t.append("## 6. Снаряжение\n")
W = [("Урон", "Damage"), ("ROF", "ROF"), ("Маг.", "Magazine"), ("Рук", "Hands"), ("Навык", "Skill")]
gear("Огнестрел", "Ranged Weapon", W)
gear("Холодное", "Melee Weapon", [("Урон", "Damage"), ("ROF", "ROF"), ("Рук", "Hands")])
gear("Экзотическое оружие", "Exotic Weapon", [("Урон", "Damage"), ("ROF", "ROF")])
gear("Броня", "Armor", [("SP", "SP"), ("Штраф", "ArmorPenalty")])
t.append("### Хром (Cyberware)\n")
t.append(table(["Имплант", "Подкатегория", "Цена", "HL", "Требует", "Суть"], [[f"{nm(f)}", f["Subcategory"], f["Cost"] or "", f["HumanityLossText"] or f["HumanityLoss"], f["Requires"], short(f["Opisanie"], 70)] for f in sorted(by_cat["Cyberware"], key=lambda f: (f["Subcategory"], f["Cost"] or 0))]))
gear("Наркотики", "Drug", [], 100)
t.append("### Прочее (название и цена в eb)\n")
lst("Боеприпасы", "Ammunition")
lst("Обвесы", "Weapon Attachment")
lst("Медицина", "Medical")
lst("Нетраннерское железо", "Netrunner Gear")
lst("Кибердеки", "Cyberdeck")
t.append("")

t.append("## 7. Транспорт, жильё, услуги\n")
gear("Транспорт", "Vehicle", [("Тип", "Subcategory")])
t.append("### Прочее (название и цена в eb)\n")
lst("Апгрейды транспорта", "Vehicle Upgrade")
lst("Дроны", "Drone")
lst("Жильё", "Housing")
lst("Образ жизни (в месяц)", "Lifestyle")
lst("Услуги", "Service")
lst("Защита дома", "Home Defense")
t.append("")

# ---- лайфпас
t.append("## 8. Таблицы лайфпаса (для быстрых NPC)\n")
lp = defaultdict(int)
for r in load("Lifepath"):
    f = r["fields"]
    lp[(f["CatOrder"], f["Category"], f["Role"])] += 1
t.append("Бросок d10 (или выбор) по таблицам: " + "; ".join(dict.fromkeys(f"{c}{' — ' + role if role else ''}" for (_, c, role), n in sorted(lp.items()))) + ". Содержимое: `data/md/mehanika/lifepath.md`.\n")
t.append("Языки по регионам — `data/md/mehanika/yazyki.md`; шаблоны ролей (статы d10, навыки, стартовый набор) — `data/md/mehanika/shablony-roley.md`.\n")

# ---- где что
t.append("""## 9. Где искать остальное

- `data/md/katalog/*.md` — все 559 предметов с описаниями (мода, гаджеты, брендовое оружие, ночной рынок, роль-снаряжение).
- `data/md/personazhi/*.md` — полные листы персонажей. `data/md/istoriya.md` — начисления, прокачка, терапия.
- `data/raw/*.json` — исходные таблицы. `tools/gen_md.py`, `tools/gen_summary.py` — генераторы.
""")

os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(t).rstrip() + "\n")
print(os.path.getsize(OUT), "bytes")
