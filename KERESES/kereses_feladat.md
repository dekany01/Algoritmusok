# Feladat: Pairs (HackerRank)

## [Link](https://www.hackerrank.com/challenges/pairs/problem)

## Leírás:
> A feladat során egy egész számokból álló ***arr*** tömböt és egy **k** célszámot kapunk, utóbbi megadja, hogy egymástól milyen távolságra lévő számmal ( a két szám különbsége tehát a *'k'*) alkothatnak a tömb elemei egy párt.

**Konkrét példa:**
> *arr* = [1,2,3,4]
> 
> *k* = 1
> 
>  Ebben az esetben összesen 3 pár van, aminek különbsége pontosan **k = 1** :
>
> * 2 - 1 = 1, 3 - 2 = 1 és 4 - 3 = 1
>
> * az eredmény tehát **3**

**A függvény:**
> pairsn() függvény paraméterei:
> * int k : egész szám (a célzott különbség)
> * int arr[n] : egész számok tömbje
>
> A függvény **visszatér** a megadott értékek alapján a fenti kritériumoknak megfelelő párok számával.
>
> Korlátok:
>   * n = ***arr*** tömb elemszáma
>   * 2 $\le$ n $\le$ 10<sup>5</sup>
>   * 0 $\le$ k $\le$ 10<sup>9</sup>
>   * 0 $\le$ arr[i] $\le$ 2<sup>31</sup>-1 

