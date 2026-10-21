# Cyberpunk RED — справочник мастера

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

## 2. Команда (состояние на момент выгрузки)

| Персонаж | Роль/ранг | Статы | HP | SP г/т | Человечн. | Эдди | IP | Топ-навыки (итог) | Вживлено | Оружие |
|---|---|---|---|---|---|---|---|---|---|---|
| **Gina Saymi** (Елизавета) | Netrunner 5 | INT7 REF8 DEX6 TECH6 COOL6 WILL4 LUCK7 MOVE7 BODY5 EMP6 | 35/35 | 11/11 | 56/56 | 11985 | 160 | Пистолеты 14, Скрытие/Раскрытие объекта 13, Криптография 13, Образование 13 | Нейролинк, Интерфейсные разъёмы, Линзы-хамелеоны | Очень тяжёлый пистолет, Тяжёлый пистолет |
| **August** (Владислав) | Rockerboy 4 | INT7 REF6 DEX6 TECH5 COOL6 WILL8 LUCK7 MOVE7 BODY3 EMP8 | 40/40 | 11/11 | 76/76 | 1335 | 310 | Композиция 13, Проницательность 13, Пистолеты 13, Рукопашный бой 12 | Кибераудиосистема, Диктофон, Техволосы, Химкожа | Очень тяжёлый пистолет, Тяжёлое холодное оружие |
| **Redtail** (Елена) | Medtech 4 | INT8 REF7 DEX6 TECH6 COOL3 WILL4 LUCK8 MOVE7 BODY6 EMP7 | 35/35 | 11/11 | 64/64 | 3000 | 70 | Дедукция 14, Образование 14, Наука (выбрать науку) 14, Тактическое оружие 13 | Киберглаз, Телеоптика, Носовые фильтры, Биомонитор | Дробовик |
| **Албанец** (Терра) | Nomad 4 | INT5 REF7 DEX6 TECH5 COOL8 WILL8 LUCK8 MOVE7 BODY5 EMP4 | 45/45 | 11/11 | 28/28 | 1205 | 280 | Пистолеты 14, Торговля 14, Вождение 13, Рукопашный бой 12 | Интерфейсные разъёмы, Нейролинк, Выдвижной щит, Выдвижной гранатомёт, Царапки | Тяжёлый пистолет, Тяжёлый пистолет, Гранатомёт, Боевой нож |
| **Слепой Еж** (Влад) | Medtech 4 | INT8 REF6 DEX5 TECH8 COOL5 WILL4 LUCK8 MOVE5 BODY7 EMP7 | 40/40 | 11/11 | 64/64 | 1345 | 160 | Образование 14, Знание техники 14, Дедукция 14, Парамедик 14 | Биомонитор, Киберглаз, Носовые фильтры, Телеоптика | Eagletech "Bearcat", Arasaka "Rapid Assault" |
| **Медведь** (Виталий) | Solo 4 | INT5 REF8 DEX7 TECH4 COOL7 WILL7 LUCK6 MOVE7 BODY8 EMP5 | 50/50 | 11/11 | 46/46 | 500 | 0 | Автоматический огонь 14, Пистолеты 14, Тактическое оружие 14, Уклонение 13 | Биомонитор, Нейролинк, Sandevistan | Штурмовая винтовка, Очень тяжёлый пистолет, Тяжёлое холодное оружие |
| **Билли** (Игорь) | Solo 4 | INT5 REF8 DEX7 TECH4 COOL7 WILL7 LUCK6 MOVE7 BODY8 EMP5 | 50/50 | 11/11 | 46/46 | 500 | 0 | Автоматический огонь 14, Пистолеты 14, Тактическое оружие 14, Уклонение 13 | Биомонитор, Нейролинк, Волверы | Штурмовая винтовка, Очень тяжёлый пистолет |

### Крючки для сюжета: предыстории

| Кто | Культура | Мотивация | Семья | Семейный кризис | Враги | Лайфпас роли |
|---|---|---|---|---|---|---|
| Gina Saymi | North American | Power | Corporate Managers. Обеспеченная семья: большой дом, безопасный район, хорошие машины, иногда прислуга. | На семье лежит родовая вражда, тянущаяся поколениями. |  | Тип нетраннера: хакает по заказу для Media, политиков или Lawman. |
| August | North American | Knowledge | Reclaimers. Начали на дороге, потом осели в брошенном городе-призраке и отстраивали его. | Семья исчезла. Он единственный оставшийся. | Marcelino Michie — отказал ему в работе или в чувствах. | Тип рокербоя: Orator (оратор). |
| Redtail | Sub-Saharan African | Vengeance | Corporate Technicians. | Семья исчезла. Он единственный оставшийся. |  | Тип медтеха: Cryosystems Operator. |
| Албанец | Western European | Данное слово. | Nomad Pack. Домом были потрёпанные трейлеры, машины и огромные дорожные kombi. | Твою семью предали, и она потеряла всё. | Бывший друг. · Один бросил или предал другого. |  |
| Слепой Еж | Eastern European | Знания. | Corporate Technicians. | Твою семью предали, и она потеряла всё. | Бывший друг. · Вы были соперниками в любви. | Создал новый тип умного защитного покрытия, которое усиливает жизненные показатели которая превосходила возможности… |
| Медведь | Восточная Европа. Языки на выбор: Английский, Финский, Польский, Румынский, Русский, Украинский. | Честность. | Ganger «Family». Дикий, жестокий дом там, где банда смогла закрепиться. | Семья замешана в долгой истории — заговоре, организации или клане: криминальная семья,… | Отдалившийся родственник. |  |
| Билли | Северная Америка. Языки на выбор: Китайский, Кри, Креольский, Английский, Французский, Навахо, Испанский. | Честь. | Corporate Managers. Обеспеченная жизнь: большой дом, безопасный район, хорошие машины. | Семья потеряла всё из-за собственных плохих решений. | Враг из детства. · Вы просто друг друга не выносите. | Работает на Арасаку и уважает ее, желать добиться успеха в корпорации |

## 3. Роли и способности (старт — ранг 4)

| Роль | Способность | Суть |
|---|---|---|
| Rockerboy | Charismatic Impact | Charismatic Impact позволяет влиять на людей чистой силой личности и работает только на Fans. |
| Solo | Combat Awareness | Combat Awareness даёт обострённое ситуационное осознание боя. |
| Netrunner | Interface | Interface — то, что вообще позволяет делать Netrun: определяет число NET Actions за ход и открывает Interface Abilities. |
| Tech | Maker | Maker позволяет чинить, улучшать, модифицировать, создавать и изобретать предметы. |
| Medtech | Medicine | Medicine даёт медицинские возможности, недоступные остальным. |
| Media | Credibility | Credibility означает, что Медиа убедителен для аудитории и глубоко подключён к информационным сетям. |
| Exec | Teamwork | Teamwork даёт команду, которая помогает достигать целей. |
| Lawman | Backup | Backup позволяет вызвать группу коллег-правоохранителей. |
| Fixer | Operator | Operator — вращение в чёрном рынке и сеть контактов. |
| Nomad | Moto | Moto — привилегии Family Motorpool и врождённое мастерство вождения. |

## 4. Навыки по категориям (стат; x2 — двойная цена)

- **Восприятие:** Концентрация (WILL); Скрытие/Раскрытие объекта (INT); Чтение по губам (INT); Внимательность (INT); Выслеживание (INT)
- **Физические:** Атлетика (DEX); Акробатика (DEX); Танец (DEX); Выносливость (WILL); Сопр. пыткам/наркотикам (WILL); Скрытность (DEX)
- **Управление:** Вождение (REF); Пилотирование (REF, x2); Судоходство (REF); Верховая езда (REF)
- **Образование:** Бухгалтерия (INT); Обращение с животными (INT); Бюрократия (INT); Бизнес (INT); Композиция (INT); Криминология (INT); Криптография (INT); Дедукция (INT); Образование (INT); Азартные игры (INT); Язык (INT, x2); Поиск информации (INT); Знание местности (INT); Наука (INT, x2); Тактика (INT); Выживание в пустыне (INT)
- **Ближний бой:** Рукопашный бой (DEX); Уклонение (DEX); Боевые искусства (DEX, x2); Оружие ближнего боя (DEX)
- **Сценические:** Актёрское мастерство (COOL); Игра на инструменте (TECH)
- **Дальний бой:** Стрельба из лука (REF); Автоматический огонь (REF, x2); Пистолеты (REF); Оружие крупного кал. (REF, x2); Тактическое оружие (REF)
- **Социальные:** Подкуп (COOL); Общение (EMP); Проницательность (EMP); Допрос (COOL); Убеждение (COOL); Уход за собой (COOL); Знаток Улиц (COOL); Торговля (COOL); Гардероб и стиль (COOL)
- **Технические:** Авиационные технологии (TECH); Знание техники (TECH); Кибертехника (TECH); Подрывник (TECH, x2); Электроника/Безопасность (TECH, x2); Первая помощь (TECH); Фальсификация (TECH); Автомеханика (TECH); Художественное ремесло (TECH); Парамедик (TECH, x2); Кино- и фототехника (TECH); Взлом замков (TECH); Карманник (TECH); Морские технологии (TECH); Оружейник (TECH); Хирургия (TECH); Медтехника (TECH)

Бросок: СТАТ + НАВЫК + 1d10 против DV. Типовые DV: стабилизация раненого 10/13/15 (по Wound State), ремонт Minor 9 / Major 13 / Destroyed 17.

## 5. Нетраннинг

### Действия

| Что | Цена | Бросок | Суть |
|---|---|---|---|
| Войти и выйти (Jack In / Jack Out) | NET-действие | — | Подключиться к Architecture, находясь в 6 м от точки доступа (стена между вами блокирует), или безопасно выйти. |
| Применить способность (Use Interface Ability) | NET-действие | Interface + 1d10 против DV | Любая из девяти способностей ниже, кроме Scanner (он стоит Meat Action) и Zap (он бросается против цели, а не против DV). |
| Включить или выключить программу (Activate / Deactivate Program) | NET-действие | — | Каждая программа на деке включается не чаще одного раза за раунд Meatspace. |
| Прочее (Miscellaneous) | NET-действие | по решению ГМ | Редкий случай: то, что не попадает ни в одну категорию. |
| Взлом пароля (Backdoor) | NET-действие | Interface + 1d10 против DV пароля | Пробиться через Password или другую преграду в Architecture. |
| Замести следы (Cloak) | NET-действие | Interface + 1d10, результат становится DV | Спрятать следы своего присутствия и оставленный Virus. |
| Перехват узла (Control) | NET-действие | Interface + 1d10 против DV узла | Взять Control Node — а через него камеры, дроны, турели, лазерные сетки, лифты, спринклеры. |
| Опознать данные (Eye-Dee) | NET-действие | Interface + 1d10 против DV файла | Понять, что за файл ты нашёл и сколько он стоит. |
| Разведка карты (Pathfinder) | NET-действие | Interface + 1d10 | Частично раскрыть «карту» Architecture. |
| Поиск точек доступа (Scanner) | Meat-действие | Interface + 1d10 | Единственная способность, которая тратит не NET-действие, а обычное действие в реальном мире. |
| Уйти от Black ICE (Slide) | NET-действие | Interface + 1d10 против PER Black ICE + 1d10 | Оторваться от одной не-Демонской Black ICE. |
| Оставить вирус (Virus) | столько NET-действий, сколько назначит ГМ | Interface + 1d10 против DV, назначенного ГМ | Только на самом нижнем этаже Architecture. |
| Удар (Zap) | NET-действие | Interface + 1d10 против DEF программы + 1d10 или Interface нетраннера + 1d10 | Базовая атака нетраннера — работает и по программам, и по чужим нетраннерам, без всяких программ на деке. |
| Что не стоит действия (Movement and files are free) | бесплатно | — | Двигаться по Architecture можно сколько угодно за ход — но не сквозь преграду вроде пароля. |
| Бой в сети (NET combat) | — | Interface + ATK программы + 1d10 против Interface цели + 1d10 или DEF программы + 1d10 | При попадании цель получает эффект программы. |
| Встреча с Black ICE (Encountering Black ICE) | — | Interface + бонусы к Speed + 1d10 против SPD Black ICE + 1d10 | Наткнулся на затаившуюся Black ICE — сразу состязание скорости. |

### Программы

| Программа | Цена | Класс | ATK | DEF | REZ | Эффект |
|---|---|---|---|---|---|---|
| DeckKRASH | 100 | Anti-Personnel | 0 | 0 | 0 | Вражеского нетраннера принудительно и небезопасно выбрасывает (unsafe Jack Out) из Architecture; на выходе он получает… |
| Hellbolt | 100 | Anti-Personnel | 2 | 0 | 0 | Наносит 2d6 урона напрямую в мозг вражескому нетраннеру. |
| Nervescrub | 100 | Anti-Personnel | 0 | 0 | 0 | INT, REF и DEX вражеского нетраннера снижаются каждый на 1d6 на следующий час (минимум 1). |
| Poison Flatline | 100 | Anti-Personnel | 0 | 0 | 0 | Уничтожает одну случайную Non-Black ICE программу, установленную на кибердеке цели-нетраннера. |
| Superglue | 100 | Anti-Personnel | 2 | 0 | 0 | Вражеский нетраннер не может продвигаться глубже в Architecture и не может безопасно сделать Jack Out в течение 1d6… |
| Vrizzbolt | 50 | Anti-Personnel | 1 | 0 | 0 | Наносит 1d6 урона напрямую в мозг нетраннеру и снижает общее число NET Actions, которые он может совершить на своём… |
| Banhammer | 50 | Anti-Program | 1 | 0 | 0 | Наносит 3d6 REZ по Non-Black ICE программе или 2d6 REZ по Black ICE программе. |
| Sword | 50 | Anti-Program | 1 | 0 | 0 | Наносит 3d6 REZ по Black ICE программе или 2d6 REZ по Non-Black ICE программе. |
| Eraser | 20 | Booster | 0 | 0 | 7 | Увеличивает все Cloak Checks, которые ты делаешь, на +2, пока эта программа Rezzed. |
| See Ya | 20 | Booster | 0 | 0 | 7 | Увеличивает все Pathfinder Checks, которые ты делаешь, на +2, пока эта программа Rezzed. |
| Speedy Gonzalvez | 100 | Booster | 0 | 0 | 7 | Увеличивает твою Speed на +2, пока эта программа Rezzed. |
| Worm | 50 | Booster | 0 | 0 | 7 | Увеличивает все Backdoor Checks, которые ты делаешь, на +2, пока эта программа Rezzed. |
| Armor | 50 | Defender | 0 | 0 | 7 | Снижает весь получаемый тобой brain damage на 4, пока эта программа Rezzed. |
| Flak | 50 | Defender | 0 | 0 | 7 | Снижает ATK всех Non-Black ICE Attacker-программ, направленных против тебя, до 0, пока эта программа Rezzed. |
| Shield | 20 | Defender | 0 | 0 | 7 | Останавливает первый успешный эффект Non-Black ICE программы, наносящий brain damage. |

### Black ICE и демоны

| ICE | Цена | Класс | ATK | DEF | REZ | Эффект |
|---|---|---|---|---|---|---|
| Skunk | 500 | Anti-Personnel | 4 | 2 | 10 | Пока эта программа не Derezzed, вражеский нетраннер, задетый эффектом, делает все Slide Checks с -2. |
| Asp | 100 | Anti-Personnel | 2 | 2 | 15 | Уничтожает одну случайную программу, установленную на кибердеке вражеского нетраннера. |
| Raven | 50 | Anti-Personnel | 4 | 2 | 15 | Derezz'ит одну случайную Defender-программу, которую держит Rezzed вражеский нетраннер, затем наносит 1d6 урона… |
| Scorpion | 100 | Anti-Personnel | 2 | 2 | 15 | MOVE вражеского нетраннера снижается на 1d6 на следующий час (минимум 1). |
| Wisp | 50 | Anti-Personnel | 4 | 2 | 15 | Наносит 1d6 урона напрямую в мозг вражескому нетраннеру и снижает общее число NET Actions, которые тот может совершить… |
| Hellhound | 500 | Anti-Personnel | 6 | 2 | 20 | Наносит 2d6 урона напрямую в мозг нетраннеру. |
| Giant | 1000 | Anti-Personnel | 8 | 4 | 25 | Наносит 3d6 урона напрямую в мозг вражескому нетраннеру. |
| Liche | 500 | Anti-Personnel | 6 | 2 | 25 | INT, REF и DEX вражеского нетраннера снижаются каждый на 1d6 на следующий час (минимум 1). |
| Kraken | 1000 | Anti-Personnel | 8 | 4 | 30 | Наносит 3d6 урона напрямую в мозг вражескому нетраннеру. |
| Killer | 500 | Anti-Program | 6 | 2 | 20 | Наносит 4d6 урона программе. |
| Sabertooth | 1000 | Anti-Program | 6 | 2 | 25 | Наносит 6d6 урона программе. |
| Dragon | 1000 | Anti-Program | 6 | 6 | 30 | Наносит 6d6 урона программе. |
| Imp | 1000 | Demon | 0 | 0 | 15 | REZ 15, Interface 3, 2 NET Actions за ход, Combat Number 14. |
| Efreet | 5000 | Demon | 0 | 0 | 25 | REZ 25, Interface 4, 3 NET Actions за ход, Combat Number 14. |
| Balron | 10000 | Demon | 0 | 0 | 30 | REZ 30, Interface 7, 4 NET Actions за ход, Combat Number 14. |

### Архитектура (цена постройки)

| Элемент | Цена, eb |
|---|---|
| Control Node Defense (DV13 to Counter) | 1000 |
| Control Node Defense (DV17 to Counter) | 5000 |
| Control Node Defense (DV21 to Counter) | 10000 |
| Control Node Defense (DV9 to Counter) | 500 |
| NET Architecture (13 to 18 Floors) | 10000 |
| NET Architecture (3 to 6 Floors) | 1000 |
| NET Architecture (7 to 12 Floors) | 5000 |
| Password, Control Node, or File (DV10) | 5000 |
| Password, Control Node, or File (DV12) | 10000 |
| Password, Control Node, or File (DV6) | 500 |
| Password, Control Node, or File (DV8) | 1000 |

## 6. Снаряжение

### Огнестрел

| Название | Цена | Урон | ROF | Маг. | Рук | Навык |
|---|---|---|---|---|---|---|
| Средний пистолет · _Medium Pistol_ | 50 | 2d6 | 2 | 12 | 1 | Handgun |
| Луки и арбалеты · _Bows & Crossbows_ | 100 | 4d6 | 1 |  | 2 | Archery |
| Тяжёлый пистолет · _Heavy Pistol_ | 100 | 3d6 | 2 | 8 | 1 | Handgun |
| Тяжёлый пистолет-пулемёт · _Heavy SMG_ | 100 | 3d6 | 1 | 40 | 1 | Handgun |
| Пистолет-пулемёт · _SMG_ | 100 | 2d6 | 1 | 30 | 1 | Handgun |
| Очень тяжёлый пистолет · _Very Heavy Pistol_ | 100 | 4d6 | 1 | 8 | 1 | Handgun |
| Штурмовая винтовка · _Assault Rifle_ | 500 | 5d6 | 1 | 25 | 2 | Shoulder Arms |
| Гранатомёт · _Grenade Launcher_ | 500 | 6d6 | 1 | 2 | 2 | Heavy Weapons |
| Ракетная установка · _Rocket Launcher_ | 500 | 8d6 | 1 | 1 | 2 | Heavy Weapons |
| Дробовик · _Shotgun_ | 500 | 5d6 | 1 | 4 | 2 | Shoulder Arms |
| Снайперская винтовка · _Sniper Rifle_ | 500 | 5d6 | 1 | 4 | 2 | Shoulder Arms |

### Холодное

| Название | Цена | Урон | ROF | Рук |
|---|---|---|---|---|
| Рукопашная · _Brawling_ |  | 1d6 / 2d6 / 3d6 / 4d6 (по BODY) | 2 |  |
| Единоборства · _Martial Arts_ |  | 1d6 / 2d6 / 3d6 / 4d6 (по BODY) | 2 |  |
| Бейсбольная бита · _Baseball Bat_ | 50 | 2d6 | 2 |  |
| Боевой нож · _Combat Knife_ | 50 | 1d6 | 2 |  |
| Лом · _Crowbar_ | 50 | 2d6 | 2 |  |
| Лёгкое холодное оружие · _Light Melee Weapon_ | 50 | 1d6 | 2 |  |
| Мачете · _Machete_ | 50 | 2d6 | 2 |  |
| Среднее холодное оружие · _Medium Melee Weapon_ | 50 | 2d6 | 2 |  |
| Томагавк · _Tomahawk_ | 50 | 1d6 | 2 |  |
| Тяжёлое холодное оружие · _Heavy Melee Weapon_ | 100 | 3d6 | 2 |  |
| Свинцовая труба · _Lead Pipe_ | 100 | 3d6 | 2 |  |
| Бита с шипами · _Spiked Bat_ | 100 | 3d6 | 2 |  |
| Меч · _Sword_ | 100 | 3d6 | 2 |  |
| Бензопила · _Chainsaw_ | 500 | 4d6 | 1 |  |
| Лопасти вертолёта · _Helicopter Blades_ | 500 | 4d6 | 1 |  |
| Нагината · _Naginata_ | 500 | 4d6 | 1 |  |
| Кувалда · _Sledgehammer_ | 500 | 4d6 | 1 |  |
| Очень тяжёлое холодное оружие · _Very Heavy Melee Weapon_ | 500 | 4d6 | 1 |  |

### Экзотическое оружие

| Название | Цена | Урон | ROF |
|---|---|---|---|
| Пневматический пистолет · _Air Pistol_ | 100 | 2d6 | 2 |
| Дротикомёт · _Dartgun_ | 100 | 4d6 | 1 |
| Электродубинка · _Stun Baton_ | 100 | 2d6 | 2 |
| Электрошокер · _Stun Gun_ | 100 | 3d6 | 2 |
| Огнемёт · _Flamethrower_ | 500 | 5d6 | 1 |
| СВЧ-излучатель · _Microwaver_ | 500 |  | 1 |
| Визгун · _Shrieker_ | 500 |  | 1 |
| Боевая перчатка · _Battleglove_ | 1000 |  |  |
| Constitution Arms Hurricane Assault Weapon | 5000 | 5d6 | 2 |
| Kendachi Mono-Three | 5000 | 4d6 | 1 |
| Militech "Cowboy" U-56 Grenade Launcher | 5000 | 6d6 | 2 |
| Rhinemetall EMG-86 Railgun | 5000 | 5d6 | 1 |
| Tsunami Arms Helix | 5000 | 2d6 | 1 |
| Malorian Arms 3516 | 10000 | 5d6 | 1 |

### Броня

| Название | Цена | SP | Штраф |
|---|---|---|---|
| Труп-щит · _Corpse_ |  |  |  |
| Кожанка · _Leathers_ | 20 | 4 |  |
| Kevlar® | 50 | 7 |  |
| Пуленепробиваемый щит · _Bulletproof Shield_ | 100 |  |  |
| Лёгкий армоджек · _Light Armorjack_ | 100 | 11 |  |
| Средний армоджек · _Medium Armorjack_ | 100 | 12 | -2 REF, DEX, and MOVE |
| Флак · _Flak_ | 500 | 15 | -4 REF, DEX, and MOVE |
| Тяжёлый армоджек · _Heavy Armorjack_ | 500 | 13 | -2 REF, DEX, and MOVE |
| Скинсьют · _Bodyweight Suit_ | 1000 | 11 |  |
| Metalgear® | 5000 | 18 | -4 REF, DEX and MOVE |

### Хром (Cyberware)

| Имплант | Подкатегория | Цена | HL | Требует | Суть |
|---|---|---|---|---|---|
| Искусственное плечевое крепление | Borgware | 1000 | 14 (4d6) |  | Владелец может установить 2 Cyberarms под первой парой рук. |
| Вживлённый экзокаркас ∑ (сигма) | Borgware | 1000 | 14 (4d6) | Grafted Muscle and Bone Lace | Усиленный скелет и опорная структура с гидравликой и миомерными… |
| Мультиоптическое крепление | Borgware | 1000 | 14 (4d6) |  | Владелец может установить в MultiOptic Mount до 5 дополнительных… |
| Сенсорный блок | Borgware | 1000 | 14 (4d6) | Cyberaudio Suite | Две сплюснутые антенны, торчащие из головы владельца и улучшающие его… |
| Вживлённый экзокаркас ß (бета) | Borgware | 5000 | 14 (4d6) | Grafted Muscle and Bone Lace | Сильно усиленный скелет и опорная структура с ещё большим количеством… |
| Радиосканер / плеер | Cyberaudio | 50 | 2 (1d6/2 Round up) | Cyberaudio Suite | Cyberaudio Option. Владелец может как Action просканировать все… |
| Усиленный слух | Cyberaudio | 100 | 3 (1d6) | Cyberaudio Suite | Cyberaudio Option. Владелец добавляет +2 к Skill Perception при… |
| Диктофон | Cyberaudio | 100 | 2 (1d6/2 Round up) | Cyberaudio Suite | Cyberaudio Option. Записывает звук на стандартный Memory Chip или на… |
| Детектор жучков | Cyberaudio | 100 | 2 (1d6/2 Round up) | Cyberaudio Suite | Cyberaudio Option. Пищит, когда владелец находится в пределах 2m/yds… |
| Маячок-пеленгатор | Cyberaudio | 100 | 2 (1d6/2 Round up) | Cyberaudio Suite | Cyberaudio Option. Позволяет следовать за связанным маячком на… |
| Встроенный агент | Cyberaudio | 100 | 3 (1d6) | Cyberaudio Suite | Cyberaudio Option. Полностью функциональный Agent, управляемый… |
| Ограничитель громкости | Cyberaudio | 100 | 2 (1d6/2 Round up) | Cyberaudio Suite | Cyberaudio Option. Автоматическая компенсация громкости. |
| Радиосвязь | Cyberaudio | 100 | 2 (1d6/2 Round up) | Cyberaudio Suite | Cyberaudio Option. Владелец может общаться по радио на дальность 1… |
| Шифратор / дешифратор | Cyberaudio | 100 | 2 (1d6/2 Round up) | Cyberaudio Suite | Cyberaudio Option. Позволяет владельцу скремблировать исходящие… |
| Анализатор стресса в голосе | Cyberaudio | 100 | 3 (1d6) | Cyberaudio Suite | Cyberaudio Option. Владелец добавляет +2 к Skills Human Perception и… |
| Кибераудиосистема | Cyberaudio | 500 | 7 (2d6) |  | Cyberaudio Suite незаметно устанавливается внутри черепа. |
| Детектор радаров | Cyberaudio | 500 | 2 (1d6/2 Round up) | Cyberaudio Suite | Cyberaudio Option. Пищит, если в радиусе 100m/yds присутствует… |
| Кастеты | Cyberlimb | 100 | 3 (1d6) |  | Cyberarm Option. Бронированные костяшки. |
| Кибернога | Cyberlimb | 100 | 3 (1d6) |  | Заменяющая нога. Не обязана быть парной. |
| Рука-кошка | Cyberlimb | 100 | 3 (1d6) | Cyberarm | Cyberarm Option. Владелец как Action может выстрелить реактивным… |
| Пластиковое покрытие | Cyberlimb | 100 | 0 (N/A) | Cyberarm or Cyberleg | Cyberlimb Option. Пластиковое покрытие для кибернетической конечности. |
| Быстросъёмное крепление | Cyberlimb | 100 | 7 (2d6) | Cyberarm | Cyberarm Option. Cyberarm можно установить в открытый разъём или… |
| Царапки | Cyberlimb | 100 | 2 (1d6/2 Round up) |  | Cyberarm Option. Искусственные ногти из карбо-стекла, режущие по… |
| Стандартная стопа | Cyberlimb | 100 | 2 (1d6/2 Round up) |  | Выглядит как обычная стопа. |
| Стандартная кисть | Cyberlimb | 100 | 2 (1d6/2 Round up) |  | Выглядит как обычная рука (кисть). |
| Подкожный захват | Cyberlimb | 100 | 3 (1d6) | Neural Link | Cyberarm Option и одновременно Neuralware Option. |
| Рука-инструмент | Cyberlimb | 100 | 3 (1d6) |  | Cyberarm Option. Пальцы содержат отвёртку, гаечный ключ, маленькую… |
| Киберрука | Cyberlimb | 500 | 7 (2d6) |  | Заменяющая рука. Не обязана быть парной. |
| Кибердека в киберруке | Cyberlimb | 500 | 3 (1d6) | Cyberarm | Cyberarm Option. Cyberdeck, навсегда вживлённый в Cyberarm владельца. |
| Цепкая стопа | Cyberlimb | 500 | 3 (1d6) | Cyberleg | Cyberleg Option. Стопы покрыты передовым материалом с повышенным… |
| Прыжковый усилитель | Cyberlimb | 500 | 3 (1d6) | Cyberleg | Cyberleg Option. Гидравлика в ногах. |
| Медсканер | Cyberlimb | 500 | 7 (2d6) | Cyberarm | Cyberarm Option. Сканер с внешними щупами и контактами диагностирует… |
| Выдвижной гранатомёт | Cyberlimb | 500 | 7 (2d6) | Cyberarm | Cyberarm Option. В Cyberarm вживляется One-Handed Grenade Launcher с… |
| Выдвижное холодное оружие | Cyberlimb | 500 | 7 (2d6) | Cyberarm | Cyberarm Option. Любое One-Handed Light, Medium или Heavy Melee… |
| Выдвижное огнестрельное оружие | Cyberlimb | 500 | 7 (2d6) | Cyberarm | Cyberarm Option. Любое One-Handed Ranged Weapon (которое не обязано… |
| Выдвижной щит | Cyberlimb | 500 | 7 (2d6) | Cyberarm | Cyberarm Option. Bulletproof Shield, скрытый в сложенном виде внутри… |
| Realskinn™ Covering | Cyberlimb | 500 | 0 (N/A) | Cyberarm or Cyberleg | Cyberlimb Option. Покрытие из искусственной кожи для кибернетической… |
| Рипперы | Cyberlimb | 500 | 3 (1d6) |  | Cyberarm Option. Выдвижные когти из карбо-стекла на пальцах. |
| Наплечная камера | Cyberlimb | 500 | 7 (2d6) | Cyberarm | Cyberarm Option. Камера в выдвижном модуле в плече владельца, которая… |
| Стопа-ролик | Cyberlimb | 500 | 3 (1d6) | Cyberleg | Cyberleg Option. Роликовые коньки, встроенные в стопы. |
| Slice ‘N Dice | Cyberlimb | 500 | 3 (1d6) |  | Cyberarm Option. Монофиламентный хлыст, вживлённый в большой палец… |
| Стопа-коготь | Cyberlimb | 500 | 3 (1d6) |  | Cyberleg Option. Клинок, вмонтированный в стопу. |
| Техсканер | Cyberlimb | 500 | 7 (2d6) | Cyberarm | Cyberarm Option. Сканер диагностирует широкий спектр механики и… |
| Перепончатая стопа | Cyberlimb | 500 | 3 (1d6) | Cyberleg | Cyberleg Option. Тонкие перепонки между пальцами ног. |
| Волверы | Cyberlimb | 500 | 7 (2d6) |  | Cyberarm Option. Выдвижные когти из карбо-стекла в костяшках. |
| Усиленное экранирование | Cyberlimb | 1000 | 3 (1d6) | Cyberarm or Cyberleg | Cyberlimb Option. Кибернетическая конечность и установленные в неё… |
| Superchrome® Covering | Cyberlimb | 1000 | 0 (N/A) | Cyberarm or Cyberleg | Cyberlimb Option. Блестящее металлическое покрытие для… |
| Антиблик | Cyberoptics | 100 | 2 (1d6/2 Round up) | Cybereye | Cybereye Option. Владелец получает иммунитет к ослеплению и другим… |
| Бегущая строка | Cyberoptics | 100 | 2 (1d6/2 Round up) | Cybereye | Cybereye Option. Проецирует крошечный субэкран в обычное поле зрения… |
| Смена цвета | Cyberoptics | 100 | 2 (1d6/2 Round up) | Cybereye | Cybereye Option. Косметическое улучшение, позволяющее неограниченно… |
| Киберглаз | Cyberoptics | 100 | 7 (2d6) |  | Искусственный глаз, заменяющий живой; в него устанавливаются все… |
| Микрооптика | Cyberoptics | 100 | 2 (1d6/2 Round up) | Cybereye | Cybereye Option. Микроскоп, дающий владельцу увеличение до 400x. |
| Виртуальность | Cyberoptics | 100 | 2 (1d6/2 Round up) | Cybereye | Cybereye Option. Проецирует образы киберпространства поверх обычного… |
| Дротикомёт | Cyberoptics | 500 | 2 (1d6/2 Round up) | Cybereye | Cybereye Option. Exotic Weapon Dartgun с единственным выстрелом в… |
| Улучшение изображения | Cyberoptics | 500 | 3 (1d6) | Cybereye | Cybereye Option. Владелец добавляет +2 к Skills Perception, Lip… |
| Ночное / инфракрасное / УФ зрение | Cyberoptics | 500 | 3 (1d6) | Cybereye | Cybereye Option. Снижает до 0 штрафы от темноты и другого… |
| Микровидео | Cyberoptics | 500 | 2 (1d6/2 Round up) | Cybereye | Cybereye Option. Камера в глазу записывает видео и аудио на… |
| Прицельный модуль | Cyberoptics | 500 | 3 (1d6) | Cybereye | Cybereye Option. Владелец получает +1 к Check при выполнении Aimed… |
| Телеоптика | Cyberoptics | 500 | 3 (1d6) | Cybereye | Cybereye Option. Владелец различает детали на расстоянии до 800m/yds. |
| Детектор радиации | Cyberoptics | 1000 | 3 (1d6) | Cybereye | Cybereye Option. Показания радиации в радиусе 100m/yds от владельца… |
| Подкожный карман | External Cyberware | 100 | 3 (1d6) |  | Полость 2"x4" (5cm x 10cm) под кожей с застёжкой-молнией Realskinn™. |
| Скрытая кобура | External Cyberware | 500 | 7 (2d6) |  | Кобура внутри тела владельца может хранить оружие, которое уже… |
| Кожное плетение | External Cyberware | 500 | 7 (2d6) |  | Тело и голова владельца защищены на SP7. |
| Подкожная броня | External Cyberware | 1000 | 14 (4d6) |  | Тело и голова владельца защищены на SP11. |
| ЭМИ-нити | Fashionware | 10 | 0 (N/A) |  | Популяризованные медиа-звездой UR тонкие серебряные линии, идущие по… |
| Биомонитор | Fashionware | 100 | 0 (N/A) |  | Подкожный имплант с постоянным LED-индикатором пульса, температуры,… |
| Химкожа | Fashionware | 100 | 0 (N/A) |  | Красители и пигменты, вживлённые в кожу, чтобы навсегда изменить её… |
| Светящаяся татуировка | Fashionware | 100 | 0 (N/A) |  | Подкожные пластины накапливают свет и проецируют под кожей цветные… |
| Линзы-хамелеоны | Fashionware | 100 | 0 (N/A) |  | Вживлённые в глаз линзы, меняющие цвет. |
| Часы под кожей | Fashionware | 100 | 0 (N/A) |  | Подкожный имплант с постоянным LED-индикатором текущего времени и… |
| Техволосы | Fashionware | 100 | 0 (N/A) |  | Искусственные волосы, испускающие цветной свет. |
| Контрацептивный имплант | Internal Cyberware | 10 | 0 (N/A) |  | Имплант предотвращает нежелательную беременность. |
| Midnight Lady™ Sexual Implant | Internal Cyberware | 100 | 7 (2d6) |  | «Будь Венерой, будь огнём. |
| Mr. Studd™ Sexual Implant | Internal Cyberware | 100 | 7 (2d6) |  | «Всю ночь, каждую ночь. |
| Носовые фильтры | Internal Cyberware | 100 | 2 (1d6/2 Round up) |  | Владелец получает иммунитет к эффектам токсичных газов, испарений и… |
| Связыватели токсинов | Internal Cyberware | 100 | 2 (1d6/2 Round up) |  | Владелец добавляет +2 к Skill Resist Torture/Drugs. |
| AudioVox | Internal Cyberware | 500 | 3 (1d6) |  | Вокальный синтезатор. |
| Усиленные антитела | Internal Cyberware | 500 | 2 (1d6/2 Round up) |  | После стабилизации владелец восстанавливает количество Hit Points,… |
| Вампиры | Internal Cyberware | 500 | 14 (4d6) |  | Клыки, вживлённые в рот владельца. |
| Киберзмея | Internal Cyberware | 1000 | 14 (4d6) |  | Кошмарное щупальце-оружие, вживлённое в горло/пищевод. |
| Жабры | Internal Cyberware | 1000 | 7 (2d6) |  | Владелец может дышать под водой. |
| Наращённые мышцы и костное плетение | Internal Cyberware | 1000 | 14 (4d6) |  | Владелец увеличивает BODY на 2. |
| Автономный запас воздуха | Internal Cyberware | 1000 | 2 (1d6/2 Round up) |  | Содержит 30 минут воздуха, после чего баллон нужно наполнить из… |
| Радар / сонар | Internal Cyberware | 1000 | 7 (2d6) |  | Постоянно сканирует местность в радиусе 50m/yds от владельца, в том… |
| Чип памяти | Neuralware | 10 | 0 (N/A) | Chipware Socket | Chipware. Стандарт хранения данных. |
| Усиленное обоняние | Neuralware | 100 | 7 (2d6) | Chipware Socket | Chipware. Пока чип установлен в Chipware Socket, обоняние владельца… |
| Усиленное осязание | Neuralware | 100 | 7 (2d6) | Chipware Socket | Chipware. Пока чип установлен в Chipware Socket, усиливается осязание… |
| Рекордер брейнданса | Neuralware | 500 | 7 (2d6) | Neural Link | Neuralware Option. Записывает braindance-контент от первого лица на… |
| Химический анализатор | Neuralware | 500 | 3 (1d6) | Chipware Socket | Chipware. Установленный в Chipware Socket, позволяет владельцу как… |
| Разъём для чипов | Neuralware | 500 | 7 (2d6) | Neural Link | Neuralware Option. Один разъём в задней части шеи, позволяющий быстро… |
| Интерфейсные разъёмы | Neuralware | 500 | 7 (2d6) | Neural Link | Neuralware Option. Разъёмы в запястье или голове, позволяющие… |
| Kerenzikov | Neuralware | 500 | 14 (4d6) | Neural Link | Neuralware Option. Постоянно работающая Speedware, дающая стабильно… |
| Нейролинк | Neuralware | 500 | 7 (2d6) |  | Проводная искусственная нервная система. |
| Sandevistan | Neuralware | 500 | 7 (2d6) | Neural Link | Neuralware Option. Speedware, дающая короткие всплески резко… |
| Чип навыка | Neuralware | 500 | 7 (2d6) | Chipware Socket | Chipware. Пока чип установлен в Chipware Socket, Skill Chip делает… |
| Редактор боли | Neuralware | 1000 | 14 (4d6) | Chipware Socket | Chipware. Пока чип установлен в Chipware Socket, Pain Editor… |

### Наркотики

| Название | Цена | Суть |
|---|---|---|
| Smash | 10 | Жёлтая пенистая дрянь, продаётся в банках повсюду. |
| Blue Glass | 20 | Primary Effect: длится 4 часа. |
| Synthcoke | 20 | Primary Effect: длится 4 часа. |
| Black Lace | 50 | Primary Effect: длится 24 часа. |
| Boost | 50 | Primary Effect: длится 24 часа. |

### Прочее (название и цена в eb)

- **Боеприпасы:** Обычные патроны 10; Резиновые патроны 10; Дымовые патроны 50; Патроны со слезоточивым газом 50; Бронебойные патроны 100; Экспансивные патроны 100; Светошумовые патроны 100; Зажигательные патроны 100; Отравленные патроны 100; Биотоксичные патроны 500; ЭМИ-патроны 500; Снотворные патроны 500; Умные патроны 500
- **Обвесы:** Штык 100; Удлинённый магазин 100; Снайперский прицел 100; Барабанный магазин 500; Подствольный гранатомёт 500; Инфракрасный прицел 500; Подствольный дробовик 500; Модуль смарт-оружия 500
- **Медицина:** Антибиотик; Быстрый детокс; Ускоритель заживления; Стим; Сурж; Аэроинъектор 50; Клонированная конечность 50; Сумка медтеха 100; Trauma Team (Silver), в месяц 500; Медсканер 1000; Trauma Team (Executive), в месяц 1000; Криопомпа 5000; Криокапсула 5000
- **Нетраннерское железо:** Чип памяти 10; Компьютер 50; Радиосканер / плеер 50; Агент 100; Резервный накопитель 100; ДНК-замок 100; Усиленная схемотехника 100; Изолированная проводка 100; Барьер KRASH 100; Радиосвязь 100; Усилитель дальности 100; Очки виртуальности 100; Шифратор / дешифратор 500; Умные очки 500
- **Кибердеки:** Кибердека (дешёвая) 100; Кибердека (обычная) 500; Кибердека в киберруке 500; Кибердека (отличная) 1000

## 7. Транспорт, жильё, услуги

### Транспорт

| Название | Цена | Тип |
|---|---|---|
| CINO RELaCS Cargo Sub |  | Mega Vehicles for Maximum Transport |
| Cybercars |  | Ground Transport |
| Delta 4 Spaceplane |  | Orbital Transport |
| K151 AeroZep |  | Mega Vehicles for Maximum Transport |
| Light Rail Lev Train |  | Mega Vehicles for Maximum Transport |
| OTEC Hammerhead Multipurpose Minisub |  | Sea Transport |
| Gyrocopter | 20000 | Air Vehicles |
| Jetski | 20000 | Sea Vehicles |
| Roadbike | 20000 | Land Vehicles |
| Aerozep | 30000 | Air Vehicles |
| Cabin Cruiser | 30000 | Sea Vehicles |
| Compact Groundcar | 30000 | Land Vehicles |
| Speedboat | 30000 | Sea Vehicles |
| Helicopter | 40000 | Air Vehicles |
| AV-4 Multipurpose Aerodyne | 50000 | Air Vehicles |
| High Performance Groundcar | 50000 | Land Vehicles |
| Yacht | 50000 | Sea Vehicles |
| AV-9 Super Aerodyne | 100000 | Air Vehicles |
| Super Groundcar | 100000 | Land Vehicles |
| Superbike | 100000 | Land Vehicles |

### Прочее (название и цена в eb)

- **Апгрейды транспорта:** AV-4 Engine Upgrade; Armored Chassis; Bulletproof Glass; Combat Plow; Communications Center; Deployable Spike Strip; Enhanced Interface Plug Integration; Heavy Chassis; Housing Capacity; Hover Upgrade; NOS; Onboard Flamethrower; Onboard Machine gun; Onboard Melee Weapon; Onboard Rocket Pod; Seating Upgrade; Security Upgrade; Smuggling Upgrade; Vehicle Heavy Weapon Mount; Replacement Spike Strips 10
- **Дроны:** Рой воздушных дронов 5000; Мини-дрон 5000; Наземный дрон 10000; Большой воздушный дрон 10000; Дрон-паук 10000
- **Жильё:** Corporate Conapt; Cube Hotel; Living on The Street; Living on The Street in a Vehicle; Hotel, Per Night 100; Hotel, Luxury, Per Night 500; Cargo Container 15000; Studio Apartment 25000; Two-Bedroom Apartment 35000; Upscale Conapt 85000; Luxury Penthouse 150000; Corporate Beaverville House 200000; Corporate Beaverville McMansion 500000
- **Образ жизни (в месяц):** Kibble 100; Generic Prepak 300; Good Prepak 600; Fresh Food 1500
- **Услуги:** Light Rail Lev Train Ticket 1; Data Term 10; Drink, Dive Bar 10; Drink, Good Bar 10; Restaurant Meal, Fast Food 10; Braindance 20; Drink, Excellent Bar 20; Movie 20; Restaurant Meal, Good 20; Taxi 20; Drink, Executive Bar 50; Hospital Treatment (DV10) 50; Interactive Braindance 50; Restaurant Meal, Excellent 50; Video Game 50; Found Cyberware Installation (Mall) 100; Hospital Treatment (DV13) 100; Live Concert / Sporting Event 100; Professional Services, Good, Per Hour 100; Bodysculpting (Standard) 500; Found Cyberware Installation (Clinic) 500; Hospital Treatment (DV15) 500; Professional Services, Excellent, Per Hour 500; Restaurant Meal, World Class 500; Therapy (Standard Humanity Loss) 500; Bodysculpting (Exotic) 1000; Found Cyberware Installation (Hospital) 1000; Hospital Treatment (DV17+) 1000; Therapy (Addiction) 1000; Therapy (Extreme Humanity Loss) 1000; Professional Services, World Class, Per Job 5000
- **Защита дома:** Камеры наблюдения 500; Потолочные и настенные бойки 1000; Электрический пол 1000; Липкая масса 1000; Скользкий пол 1000; Электрошоковые панели 1000; Липкий пол 1000; Опрокидывающийся пол 1000; Автоматическое холодное оружие 5000; Автоматическая турель 5000; Лазерная сетка 5000; Лифт со снотворным газом 5000; Боевой рой 10000

## 8. Таблицы лайфпаса (для быстрых NPC)

Бросок d10 (или выбор) по таблицам: Культурные корни; Характер; Стиль одежды; Причёска; Особые приметы; Что ты ценишь больше всего; Отношение к людям; Самый дорогой человек; Самая ценная вещь; Семья: происхождение; Детство: окружение; Кризис в семье; Друзья: кто он тебе; Враги: кто это; Враги: из-за чего; Враги: что могут бросить против тебя; Сладкая месть: что вы сделаете друг другу; Романтическая жизнь: как всё закончилось; Жизненная цель; Rockerboy: какой ты Rockerboy — Rockerboy; Rockerboy: группа или сольник — Rockerboy; Rockerboy: где ты выступаешь — Rockerboy; Rockerboy: кто на тебя охотится — Rockerboy; Rockerboy: был ли ты раньше в группе — Rockerboy; Rockerboy: почему ты ушёл из группы — Rockerboy; Solo: какой ты Solo — Solo; Solo: твоя рабочая территория — Solo; Solo: кто на тебя охотится — Solo; Solo: твой моральный компас — Solo; Netrunner: напарник или одиночка — Netrunner; Netrunner: кто твой напарник — Netrunner; Netrunner: какой ты раннер — Netrunner; Netrunner: как выглядит твоё рабочее место — Netrunner; Netrunner: кто твои остальные клиенты — Netrunner; Netrunner: где ты берёшь программы — Netrunner; Netrunner: кто на тебя охотится — Netrunner; Tech: какой ты Tech — Tech; Tech: напарник или одиночка — Tech; Tech: кто твой напарник — Tech; Tech: как выглядит твоя мастерская — Tech; Tech: кто твои основные клиенты — Tech; Tech: где ты берёшь детали — Tech; Tech: кто на тебя охотится — Tech; Medtech: какой ты Medtech — Medtech; Medtech: как выглядит твой кабинет — Medtech; Medtech: напарник или одиночка — Medtech; Medtech: кто твой напарник — Medtech; Medtech: кто твои основные клиенты — Medtech; Medtech: где ты берёшь медикаменты — Medtech; Media: какой ты Media — Media; Media: насколько ты этичен — Media; Media: как твои материалы доходят до людей — Media; Media: о чём ты хочешь рассказывать — Media; Exec: на какую корпорацию ты работаешь — Exec; Exec: в каком отделе ты работаешь — Exec; Exec: насколько твоя корпорация хороша или плоха — Exec; Exec: отношения с боссом сейчас — Exec; Exec: где базируется твоя корпорация — Exec; Exec: кто охотится на твою корпорацию — Exec; Lawman: твоя должность в подразделении — Lawman; Lawman: юрисдикция твоего подразделения — Lawman; Lawman: насколько ваше подразделение продажно — Lawman; Lawman: кто охотится на ваше подразделение — Lawman; Lawman: главная цель вашего подразделения — Lawman; Fixer: какой ты Fixer — Fixer; Fixer: как выглядит твой «офис» — Fixer; Fixer: напарник или одиночка — Fixer; Fixer: кто твой напарник — Fixer; Fixer: кто твои побочные клиенты — Fixer; Fixer: кто на тебя охотится — Fixer; Nomad: насколько велик твой Pack — Nomad; Nomad: суша, воздух или море — Nomad; Nomad: чем занимается сухопутный Pack — Nomad; Nomad: чем занимается воздушный Pack — Nomad; Nomad: чем занимается морской Pack — Nomad; Nomad: что ты делаешь для своего Pack — Nomad; Nomad: кто охотится на твой Pack — Nomad; Nomad: философия твоего Pack — Nomad. Содержимое: `data/md/mehanika/lifepath.md`.

Языки по регионам — `data/md/mehanika/yazyki.md`; шаблоны ролей (статы d10, навыки, стартовый набор) — `data/md/mehanika/shablony-roley.md`.

## 9. Где искать остальное

- `data/md/katalog/*.md` — все 559 предметов с описаниями (мода, гаджеты, брендовое оружие, ночной рынок, роль-снаряжение).
- `data/md/personazhi/*.md` — полные листы персонажей. `data/md/istoriya.md` — начисления, прокачка, терапия.
- `data/raw/*.json` — исходные таблицы. `tools/gen_md.py`, `tools/gen_summary.py` — генераторы.
