# Python programozás a gyakorlatban - 1. beadandó

## Harcos

Készítsd el a **Harcos** absztrakt osztályt, melynek 3 darab absztrakt propertyje legyen.

- **nev**: a harcos neve (szöveg)
- **tapasztalat**: a harcos tapasztalata években (egész)
- **fenykardszin**: a fénykard színe (string)
- **pontszam** harci erő (egész)

Készíts egy **harcol** nevű függvényt (ez ne legyen absztrakt), ami egy Harcost vár paraméterül, és a győztes harcos nevével térjen vissza + a szöveggel, hogy "nyerte a harcot", és hogy milyen fénykarddal. Az a harcos nyer, akinek nagyobb a pontszáma. Ha ugyanannyi pontszáma van mindkét harcosnak, térjen vissza az "Elmenekültek" szöveggel(Tehát például, ha Obi-Wan-nak 700 a pontszáma, Anakin-nak pedig 600, akkor térjen vissza azzal, hogy "Obi-Wan nyerte a harcot kék fénykarddal")

Az osztály ne legyen példányosítható!

## Jedi

Készítsd el a **Jedi** osztályt (ami egy **Harcos** leszármazott), amely rendelkezzen az alábbi adattaggal:

- **egyensuly**: mennyire van egyensúlyban az erővel, ez egy szám 1-10 (egész)

Készíts egy inicializáló függvényt ami nevet, tapasztalatot és az egyensúlyt várja paraméterként.

Ha az egyensúly nagyobb mint 5, és kissebb vagy egyenlő mint 10, akkor a fénykard színét állítsd **zöld**-re. Ha az egyensúly kissebb vagy egyenlő mint 5, és nagyon vagy egyenlő mint 1, akkor a fénykard színét állítsd **kék**-re. Egyéb esetben a fénykard színét állítsd **lila**-ra.

Valósítsd meg a **pontszam** propertyt. Az értéke legyen egy egész szám, ha a fénykard színe **lila**, akkor a szám értéke 10 \* tapasztalat, egyéb esetben az **egyensuly** és a **tapasztalat** szorzata.

## Sith

Készítsd el a **Sith** osztályt (ami egy speciális **Harcos**), amely rendelkezzen az alábbi adattaggal:

- **harag**: mekkora benne a harag, ez egy szám 1-10 (egész)

Készíts egy inicializáló függvényt ami nevet, tapasztalatot és a haragot várja paraméterként. A név úgy kezdődjön, hogy **Darth**, és szóközzel elválasztva, illeszd hozzá a paraméterben kapott nevet.
A **fenykardszin** adattagot állítsuk **piros**-ra.

Valósítsd meg a **pontszam** propertyt. Az értéke legyen egy egész szám, a **harag** és a **tapasztalat** szorzata.

## SemlegesHarcos

Készítsd el a **SemlegesHarcos** osztályt, ami a Jedi, és a Sith leszármazottja.

Készíts egy inicializáló függvényt ami nevet, tapasztalatot, egyensúlyt, és haragot vár paraméterként.

Ha a harag nagyobb mint az egyensúly, a fénykard színe legyen **piros**, ha kissebb, legyen **kék**, ha egyenlő, legyen **fehér**.

Valósítsd meg a **pontszam** propertyt. Az értéke legyen egy egész szám, ha nagyobb a harag, akkor legyen a **harag** és a **tapasztalat** szorzata, ha kissebb vagy egyenlő, akkor az **egyensuly** és a **tapasztalat** szorzata.

