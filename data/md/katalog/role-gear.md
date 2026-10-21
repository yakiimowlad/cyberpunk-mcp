# Role Gear

Предметов: 12. Источник: таблица `Katalog` (Grist).

| Название | Name | Подкатегория | Цена, eb | Ценовая кат. | Стр. |
|---|---|---|---|---|---|
| Материалы для бодискульптинга (экзотика) | Bodysculpting Materials (Exotic) | Bodysculpting | 500 | Expensive | 227 |
| Материалы для бодискульптинга (обычные) | Bodysculpting Materials (Standard) | Bodysculpting | 100 | Premium | 227 |
| Материалы для изготовления (дешёвая вещь) | Fabrication Materials (Cheap Item) | Maker (Tech Role Ability) | 5 |  | 148 |
| Апгрейд машины автопарка Family (Moto 10) | Family Motorpool Vehicle Upgrade (Moto Rank 10) | Moto (Nomad Role Ability) | 1000 |  | 162 |
| Ремонт машины Family | Family Vehicle Repair | Moto (Nomad Role Ability) | 500 |  | 162 |
| Фармацевтические материалы | Pharmaceutical Materials | Medicine (Medtech Role Ability) | 200 |  | 149 |
| Бонус или льгота члену команды | Team Member Bonus or Perk | Teamwork (Exec Role Ability) | 200 |  | 154 |
| Плата за найм в команду | Team Member Hiring Fee | Teamwork (Exec Role Ability) | 200 |  | 154 |
| Материалы для терапии (зависимость) | Therapy Materials (Addiction) | Therapy | 500 | Expensive | 230 |
| Материалы для терапии (тяжёлая потеря Человечности) | Therapy Materials (Extreme Humanity Loss) | Therapy | 500 | Expensive | 230 |
| Материалы для терапии (обычная потеря Человечности) | Therapy Materials (Standard Humanity Loss) | Therapy | 100 | Premium | 230 |
| Материалы для апгрейда машины | Vehicle Upgrade Materials | Maker (Tech Role Ability) | 1000 | Very Expensive | 148 |

## Описания

### Материалы для бодискульптинга (экзотика) · _Bodysculpting Materials (Exotic)_

Материалы для Exotic Bodysculpting, когда операцию делает сам Medtech (DV17 Surgery). Процедура занимает 4 часа; при провале материалы уничтожаются и теряется 2 часа операционного времени.

**Примечание:** Только для Medtech'а, делающего Bodysculpting самостоятельно. Оплата услуги в госпитале — отдельная позиция Bodysculpting (Exotic) 1,000eb (V. Expensive). Exotic Bodysculpting даёт Humanity Loss 4d6. Делать Bodysculpting самому себе нельзя.

### Материалы для бодискульптинга (обычные) · _Bodysculpting Materials (Standard)_

Материалы для Standard Bodysculpting, когда операцию делает сам Medtech (DV15 Surgery). Процедура занимает 4 часа; при провале материалы уничтожаются и теряется 2 часа операционного времени.

**Примечание:** Только для Medtech'а, делающего Bodysculpting самостоятельно. Оплата услуги в клинике — отдельная позиция Bodysculpting (Standard) 500eb (Expensive). Standard Bodysculpting не даёт Humanity Loss. Делать Bodysculpting самому себе нельзя.

### Материалы для изготовления (дешёвая вещь) · _Fabrication Materials (Cheap Item)_

Материалы для изготовления предмета Price Category Cheap через Fabrication Expertise.

**Примечание:** Единственная явно названная цена материалов в правилах Maker: «Fabricating a Cheap item costs 5eb». Для остальных категорий Tech покупает материалы той же Price Category, что и изготавливаемый или улучшаемый предмет. Цены в eb для этих категорий книга здесь не даёт — см. таблицу Market Price (стр. 385).

### Апгрейд машины автопарка Family (Moto 10) · _Family Motorpool Vehicle Upgrade (Moto Rank 10)_

Покупка любого Nomad Vehicle Upgrade за фиксированную цену, доступная Nomad'у, достигшему 10-го ранга Role Ability Moto: он становится лидером в семье, может держать все свои Family Vehicles на руках одновременно, покупает будущие Family Vehicles по рыночной цене, а любые будущие апгрейды — по 1,000eb за штуку.

**Примечание:** Название записи составное: в книге это описано текстом, без Price Category. Именно этот механизм даёт Vehicle Upgrade'ам цену в eb — до Rank 10 они выдаются по Moto Rank бесплатно, а на открытом рынке встречаются редко (Very Expensive для доступных с Rank 1, Luxury для остальных).

### Ремонт машины Family · _Family Vehicle Repair_

Ремонт уничтоженной Family Vehicle силами Nomad Family. Семья полностью восстанавливает машину, но это займёт неделю, и Nomad должен заплатить за услугу 500eb.

**Примечание:** Название записи составное: в книге это описано текстом, без Price Category и без строки прайса. Платят даже Family Heads — так принято сохранять лицо после порчи семейного имущества. Оплату могут простить, если Nomad разорён, но репутация пострадает. Мелкий ремонт вроде выковыривания пуль — забота самого Nomad'а.

### Фармацевтические материалы · _Pharmaceutical Materials_

Материалы для синтеза фармацевтики Medtech'ом. Medtech с Medicine Specialty «Medical Tech (Pharmaceuticals)» может из 200eb материалов за 1 час сделать столько доз, сколько у него уровней Medical Tech Skill, бросая DV13 Medical Tech Check; при провале материалы пропадают.

**Примечание:** Доступно только Medtech'ам через Role Ability Medicine. Синтезировать Street Drugs через Medical Tech (Pharmaceuticals) нельзя. Доступные препараты: Antibiotic, Rapidetox, Speedheal, Stim, Surge. В книге цена дана текстом («200eb of materials»), без Price Category — поэтому price_category = null.

### Бонус или льгота члену команды · _Team Member Bonus or Perk_

Премия или иная плюшка стоимостью минимум 200eb, которую Exec даёт своему Team Member. Даёт +4 к Loyalty.

**Примечание:** Название записи составное: в книге это строка таблицы Gaining Loyalty («Give them a bonus or other perk of at least 200eb in value»), без Price Category. Не выполнить обещанную премию — минус 6 Loyalty.

### Плата за найм в команду · _Team Member Hiring Fee_

«Плата за наём» (по факту — взятка) отделу HR, когда Exec'у нужно заменить потерянного Team Member. HR изымает снаряжение погибшего и присылает замену на следующей игровой сессии; у новичка новые STAT'ы, а стартовый Loyalty снижен до 1.

**Примечание:** Название записи составное: в книге это описано текстом («an additional 200eb in "hiring fees" (bribes) to HR»), без Price Category и без отдельной строки прайса. Относится только к Exec'ам с Role Ability Teamwork Rank 3+.

### Материалы для терапии (зависимость) · _Therapy Materials (Addiction)_

Материалы для недельной терапии от зависимости, если её проводит сам Medtech (DV15 Medical Tech).

**Примечание:** Материалы контролируются Biotechnica и покупаются напрямую у корпорации. Medtech не может проводить Therapy на себе. Оплата услуги — отдельная позиция Therapy (Addiction) 1,000eb. Если пациент ночует в госпитале, это ещё 100eb за ночь.

### Материалы для терапии (тяжёлая потеря Человечности) · _Therapy Materials (Extreme Humanity Loss)_

Материалы для недельной терапии Extreme Humanity Loss, если её проводит сам Medtech (DV17 Medical Tech).

**Примечание:** Материалы контролируются Biotechnica и покупаются напрямую у корпорации. Medtech не может проводить Therapy на себе. Оплата услуги — отдельная позиция Therapy (Extreme Humanity Loss) 1,000eb. Если пациент ночует в госпитале, это ещё 100eb за ночь.

### Материалы для терапии (обычная потеря Человечности) · _Therapy Materials (Standard Humanity Loss)_

Материалы для недельной терапии Standard Humanity Loss, если её проводит сам Medtech (DV15 Medical Tech).

**Примечание:** Материалы полностью контролируются Biotechnica и покупаются напрямую у корпорации. Терапия занимает целую неделю, в течение которой врач и пациент не могут заниматься ничем другим; при провале Check неделя и материалы потеряны. Medtech не может проводить Therapy на себе. Оплата услуги — отдельная позиция Therapy (Standard Humanity Loss) 500eb. Если пациент ночует в госпитале, это ещё 100eb за ночь.

### Материалы для апгрейда машины · _Vehicle Upgrade Materials_

Материалы, которые Tech тратит, устанавливая апгрейд на транспорт через Upgrade Expertise. Для этой цели любой vehicle upgrade считается предметом стоимостью 1,000eb (Very Expensive) вне зависимости от его реальной цены.

**Примечание:** Единственное исключение из общего правила «материалы той же Price Category, что и улучшаемый предмет». Tech с Upgrade Expertise может поставить на транспорт апгрейд, требующий Nomad Role Ability Rank 1. При провале Check материалы теряются, но улучшаемый предмет не страдает. DV и время установки берутся по Price Category предмета: Very Expensive = DV24, 2 недели.
