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

> Az *RST* létrehozatalakor mindig a kisebb súlyú élt kell választani.
> 
> Meg kell emellett vizsgálni, hogy az adott él hozzá adásakor nem kapunk-e kört. Ha így kört kapunk, akkor ezt az élt ki kell hagyni.
> Ha pedig két ugyanolyan súlyozású élről van szó:
>
> * Azt az élt kell választani, amelyik esetében az élhez tartozó két csúcs számozását összeadva kisebbet kapunk eredményül.
> * `pl: ha az 1-2 és a 3-1 élek súlyozása azonos, akkor az 1-2 élt kell választani ( 1 + 2 < 3 + 1)`
>
> A cél, hogy megadjuk, a fenti RST részgráfnak mekkora az össz súlya.

**Konkrét példa:**
> 
>

**A függvény:**
> 
