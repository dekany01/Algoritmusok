# Megközelítés

 A faktoriális definícióját, annak szorzatalakját vizsgáltam meg először. Egy adott pozitív egész szám esetén:
>  ` n! = n * (n-1) * (n-2) * ... * 1 `

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
> 26!
