# Feladat: Fibonacci Modified (HackerRank)

## [Link](https://www.hackerrank.com/challenges/fibonacci-modified/problem?isFullScreen=true)

## Leírás:
Implementálni kell a módosított Fibonacci sorozatot az alábbi definíció szerint:
> Ha adott a t[i] és t[i+1] számok, ahol i 1 és végtelen közötti egész szám, akkor t[i+2] esetén
>
> **t<sub>i+2</sub> = t<sub>i</sub> + (t<sub>i+1</sub>)<sup>2</sup>**
>

A feladat kiszámítani 3 egész szám, *t1*, *t2* és *n* alapján a módosított Fibonacci sorozat n-edik elemét.
> 
**Konkrét példa:**
> *t1* = 0
> 
> *t2* = 1
> 
>* t3 = 0 + 1<sup>2</sup> = 1
>* t4 = 1 + 1<sup>2</sup> = 2
>* t5 = 1 + 2<sup>2</sup> = 5
>* t6 = 2 + 5<sup>2</sup> = 27 
>
> eredmény = 27


**A függvény:**
> fibonacciModified() függvény paraméterei:
> * int t1 : egész szám (a sorozat első eleme)
> * int t2 : egész szám (a sorozat második eleme)
> * int n : egész szám (a sorozat 'n'-dik eleme)
>
> A függvény **visszatér** a megadott értékek alapján a módosított Fibonacci sorozat *n*-dik elemével.
>
> Beviteli formátuma: három egész szám szóközzel elválasztva (*t1*,*t2* és *n*)
>
> Korlátok:
>   * 0 $\le$ t1, t2 $\le$ 2
>   * 3 $\le$ n $\le$ 20
