# Feladat: Kruskal (MST): Really Special Subtree (HackerRank)

## [Link](https://www.hackerrank.com/challenges/kruskalmstrsub/problem?isFullScreen=true)

## Leírás:
> Adott egy irányítatlan súlyozott összefüggő gráf, a feladat megtalálni a *'Nagyon Különleges Részfáját'* (továbbiakban röviden RST = Really Special Subtree).
> 
> Az **RST** egy olyan részgráf, ami tartalmazza az összes csúcsát az eredeti gráfnak és:
>
> * Két csúcsot csak és kizárólag egy út köt össze.
> * Ez a részgráf az összes közül a legkisebb súlyozású (az összes él súlya ennél a legkisebb).
> * Nincs benne kör.
>

> Az *RST* készítésekor mindig a kisebb súlyú élt kell választani.
> 
> Meg kell emellett vizsgálni, hogy az adott él hozzá adásakor nem kapunk-e kört. Ha így kört kapunk, akkor ezt az élt ki kell hagyni.
> Ha pedig két ugyanolyan súlyozású élről van szó:
>
> * Azt az élt kell választani, amelyik esetében az élhez tartozó két csúcs számozását összeadva kisebbet kapunk eredményül.
> * `pl: ha az 1-2 és a 3-1 élek súlyozása azonos, akkor az 1-2 élt kell választani ( 1 + 2 < 3 + 1)`
>
> A cél, hogy megadjuk, a fenti RST részgráfnak mekkora a teljes súlya.

**Konkrét példa:**
> Az alábbi input értékeket kapva (***u*** és ***v*** csúcsok azonosítója, ***wt*** az él súlyozása):
> 
>```
>  u  v  wt
>  1  2  2
>  2  3  3
>  3  1  5
>```
> Először kiválasztjuk az 1 → 2 élt, aminek 2 a súlya. Majd utána a 2 → 3 élt, aminek 3 a súlya. Így mindegy csúcsot érintettük körmentesen, a teljes súlya pedig **3 + 2 = 5**.
> 
**A függvény:**
> A "***kruskals***" függvénynek vissza kell adni egy egész számot, ami reprezentálja a létrehozott részgráf teljes súlyát.
>
> A függvény az alábbi paraméterekkel rendelkezik:
>
> * g_nodes: egész szám, a gráfban található csúcsok száma
> * g_from: egész számok tömbje, megadja az adott él kezdőpontját
> * g_to: egész számok tömbje, megadja az adott él végpontját
> * g_weight: egész számok tömbje, megadja az adott él súlyát
>
> **Input**
>
> Az első sor két szóközzel elválasztott egész számot tartalmaz: a csúcsok számát (**g_nodes**) és az élek számát (**g_edges**).
>
> A többi *g_edges* számú sor mindegyike 3 szóközzel elválaszott egész számot tartalmaz: az **irányítatlan** élek két végpontját (**g_from** és **g_to**), valamint az adott él súlyát (**g_weight**)
>
> **Korlátok**
> * 2 $\le$ *g_nodes* $\le$ 3000
> * 1 $\le$ *g_edges* $\le$ N*(N-1)2
> * 1 $\le$ *g_from, g_to* $\le$ N
> * 0 $\le$ *g_weight* $\le$ 10<sup>5</sup
>
> **Output**
> Egy egész számot ír ki, az *RST* gráf teljes súlyát.
