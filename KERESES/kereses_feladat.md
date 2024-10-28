# Feladat: Pairs (HackerRank)

## [Link](https://www.hackerrank.com/challenges/pairs/problem)

## Leírás:
> A feladat során egy egész számokból álló ***arr*** tömböt kapunk, valamint egy ***k*** egész számot.
> Az *arr* tömbből *k* elemből álló ***arr'*** résztömböket  kell létrehozni. Majd vesszük ezeknek a résztömböknek az "igazságtalanságát" (unfairness) és azok közül meg kell határozni a legkisebb értéket.
> 
> Egy tömb "igazságtalansága" így számítható ki: `max(arr') - min(arr')`
>
> ahol:
>   *  a *max(arr')* az *arr'* résztömb legnagyobb elemét (egész számot) jelöli
>   *  a *min(arr')* az *arr'* résztömb legkisebb elemét (egész számot) jelöli
> 
**Konkrét példa:**
> *arr* = [1,4,7,2]
> 
> *k* = 2
> 
>  Vesszük bármely két elemet, pl. ***arr' = [4,7]***
> 
>  Ekkor: ***unfairness = max(4,7) - min(4,7) = 7 - 4 = 3***  
>
>   Minden résztömbre letesztelve végül a megoldást az [1,2] résztömb adja (ennél az érték 1 lesz).
>
> ***Megjegyzés:*** az *arr* tömb nem csak különböző egész számokat tartalmazhat.

**A függvény:**
> maxMin() függvény paraméterei:
> * int k : egész szám (résztömbök elemszámát adja meg)
> * int arr[n] : egész számok tömbje
>
> A függvény **visszatér** a megadott értékek alapján a legkisebb "igazságtalansági" értékkel.
>
> Korlátok:
>   * n = ***arr*** tömb elemszáma
>   * 2 $\le$ k $\le$ n
>   * 0 $\le$ arr[i] $\le$ 10<sup>9</sup>
