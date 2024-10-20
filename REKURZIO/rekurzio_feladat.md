# Feladat: Recursive Digit Sum (HackerRank)

## [Link](https://www.hackerrank.com/challenges/recursive-digit-sum/problem)

## Leírás:
Hozzunk létre egy függvényt, amivel megadható egy adott **x** egész szám *szuperszámjegye*.

Az **x** egész szám *szuperszámjegyét* az alábbi szabályok segítségével kell meghatározni:
- Ha az **x** 1 db számjegyből áll, akkor a *szuperszámjegye* önmagával egyenlő (x-szel)
- Egyéb esetben **x** *szuperszámjegye* egyenlő **x** számjegyeinek összegének *szuperszámjegyével*
- *pl. **9876** esetén*:
  ```
    superDigit(9876)  --> 4 számjegy, 9 + 8 + 7 + 6 = 30, ezért superDigit(30)-al tér vissza
    superDigit(30)    --> 2 számjegy, 3 + 0 = 3, ezért superDigit(3)-al tér vissza
    superDigit(3)     --> = 3
  ```
**Konkrét példa:**
> n = '9876'
> 
> k = 4
> 
> A **p** szám =  az *n* karatkerlánc összefűzése önmagával *k* alkalommal.
> A fenti értékek alapján: `p = 9876987698769876`
>
> ```
>   superDigit(p) = superDigit(9876987698769876)
>    // 9 + 8 + 7 + 6 + 9 + 8 + 7 + 6 + 9 + 8 + 7 + 6 + 9 + 8 + 7 + 6 = 120
>   superDigit(p) = superDigit(120)
>    // 1 + 2 + 0 = 3
>   superDigit(p) = superDigit(3) // = 3
> ```
>

**A függvény:**
> superDigit() függvény paraméterei:
> * string n : az egész szám sztring alakban
> * int k : hányszor fűzzük össze a kapott stringet önmagával
>
> A föggvény **visszatér** a megadott *n* szám szuperszámjegyének 'int'-ben megadott értékével.
>
> Beviteli formátuma: két egész szám szóközzel elválasztva (*n* és *k*)
>
> Korlátok:
>   * 1 $\le$ n $\le$ 10<sup>100000</sup>
>   * 1 $\le$ k $\le$ 10<sup>5</sup>
