
# Feladat: Lego Blocks (HackerRank)

## [Link](https://www.hackerrank.com/challenges/lego-blocks/problem?isFullScreen=true)

## Leírás:
> Van végtelen számú, *1 egység* magas és *1 egység* mélységű (**4 fajta**)  `1, 2, 3 és 4 szélességű` Lego kockánk.
> 
> Ezeket az építő elemeket felhasználva egy ***'n'*** magas és ***'m'*** széles falat szeretnénk építeni az alábbi szabályokat betartva:
>
> * A fal nem tartalmazhat lyukakat (üres helyeket).
> * Az épített falnak tömörnek ('solid') kell lennie, vagyis nem tartalmazhat a fal összes során keresztül menő, egybefüggő vonalat.
> * Az építő elemeket csak vízszintesen lehet elhelyezni.
>
> A kérdés az, hogy hányféleképpen lehet így falat építeni?

**Konkrét példa:**
> *n* = 2 
> 
> *m* = 3 
>
> A fal magassága tehát *'2'* egység, szélessége *'3'* egység.
> Néhány helyes ("good layouts") és helytelen ("bad layouts) építési lehetőség:
>
> ![Példa!](https://s3.amazonaws.com/hr-assets/0/1526322298-72d127a6f7-bricks.png)
>
> A fenti kép csak néhány esetet mutat be az összes közül (az összes lehetőség ebben az esetben **9**)
>

**A függvény:**
> legoBlocks() függvény paraméterei:
> * int n : egész szám (a megépítendő fal magassága)
> * int m : egész szám (a megépítendő fal szélessége)
>
> A függvény **visszatér** a megadott értékek alapján az adott fal összes helyes építési lehetőségeinek számával (az értéket modulo '10<sup>9</sup>+7'-ben megadva).
>
> Korlátok:
>   * 1 $\le$ n, m $\le$ 1000
