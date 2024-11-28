# Megközelítés
A feladat leírásában szereplő függvényt jelölje a **Z(N)**, ahol *N* a vizsgálandó pozitív egész szám.
A faktoriális definícióját, annak szorzatalakját vizsgáltam meg először. N esetén:
>  ` N! = N * (N-1) * (N-2) * ... * 1 `

Ahhoz, hogy a kapott szám vége 0-ra végződjön, 10-el osztható kell, hogy legyen.
> 
> 10-et felbontjuk szorzatalakra: 10 = 2 * 5
> 
> Ha akármilyen egész számot megszorzunk 10-el, biztosan 0-ra végződik. Ha egy számot 2-vel megszorzunk, akkor páros számot kapunk.
> Ezek alapján, ha pl. 10-et megszorozzuk 3-mal : 3 * 10 = 3 * 2 * 5 = 6 * 5
> Vagyis, ha 5-t megszorzunk egy páros egész számmal, biztosan 0-ra végződő számot kapunk.

Páros szám egy adott pozitív egész szám faktoriálisának szorzatalakjában mindig több van, mint 5-tel osztható egész szám, vagyis az adott mennyiségű 5-tel osztható egész számnak mindig lesz párja, amivel 0-ra végződő számot kapunk.
A döntő tényező tehát, hogy hány darab 5-tel osztható szám van a sorozatban, ez határozza meg a kapott szám végén lévő nullák darabszámát.

>  Ez alapján  vizsgáltam pár konkrét esetet:
> *pl. ha N kisebb, mint 5, akkor nem lehet 0 végződésű a kapott szám:*
> 3! = 3 * 2 * 1 = 6
> 4! = 4 * 6 = 24
> 5! = 5 * 24 = 120
> 
> *pl. 12! esetén:*
> 12! = 12 * 11 * 10 * ... * 5 * ... * 1
> 
> **5-tel osztható számok: {5, 10}**
> 
> 2 db ilyen szám van, 2 db 0 van a kapott szám végén
>
> *pl. 26! esetén:*
> 26! = 26 * 25 * ... * 20 * ... * 15 * ... * 10 * ... * 5 * ... * 1
>
> **5-tel osztható számok: {5, 10, 15, 20, 25}**
>
> Fontos megjegyezni itt azonban, hogy a 25 = 5 * 5.
>
> Ez alapján:
>
> 26! = 26 * 5 * 5 * 24 * ... * 20 * ... * 15 * ... * 10 * ... * 5 * ... * 1
>
> Miután a 25 felbontható további 2 db 5 szorzóra, így további 1-gyel növeli a 0-k számát.
> Ez alapján: Z(26) = 6.
>

A fenti vizsgálat eredményeként megállapítható, hogy nemcsak az 5-tel való oszthatóságát kell vizsgálni az adott számnak, hanem 5 hatványaival való oszthatóságát is.

Először meg kell néznünk, hogy az adott *N* számban az 5 hányszor van meg.
Ezután, ha 24-nél nagyobb számról van szó, megnézzük, hogy 25-tel osztva az eredeti számot, milyen egész számot kapunk.
Ha 124-nél nagyobb számról van szó, megnézzük, hogy 125-tel osztva az eredeti számot, milyen egész számot kapunk és így tovább szorozzuk tovább 5-tel az osztót, amíg az osztó nem nagyobb, mint az eredeti *N* számunk.
A kapott egész értékeket összeadjuk, ez adja a végeredményt.

> *pl. 132! esetén:*
> int (132 / 5) = 26, 
> int (132 / 25) = 5, 
> int (132 / 125) = 1, 
>
> Miután 625 > 132, itt megállunk és összesítjük a kapott eredményeket: 26 + 5 + 1 = 32
>
> Vagyis 32 db "0" van egymás után a szám végén. "...0000000"
> 
