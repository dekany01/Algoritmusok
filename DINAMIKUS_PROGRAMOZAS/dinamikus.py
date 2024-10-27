#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

sys.set_int_max_str_digits(1000000)  # Megnöveljük a megjeleníthető számjegyek számát a magas függvényparaméterek miatt.
def fibonacciModified(t1, t2, n):
    
    fibList = [0] * (n + 1) # Létrehozunk egy 'n+1' elemű listát (az egyszerűbb indexelés miatt).

    # A sorozat megadott két első értéke a lista 1. és 2. indexű eleme lesz:
    
    fibList[1] = t1
    fibList[2] = t2
    
    # Az összes többi elemet szintén eltároljuk a listában (alulról felülre építkezve), hiszen az 'n'-nél kisebb indexű elemeket is többször felhasználjuk.
   
    i = 3 
    while i <= n: # 3. indextől kezdve nézzük a sorozat többi elemét.

        newNumber = fibList[i-2] + fibList[i-1]**2 # Kiszámoljuk a sorozat új elemét a feladatban megadott formula alapján.
        fibList[i] = newNumber # A lista i. indexű eleme a sorozat i. eleme lesz.
        
        i += 1 

    # Így kapunk egy 1 dimenziós táblázatot, melynek adott 'i.' indexű eleme a módosított Fibonacci sorozat 'i'. eleme lesz.
    
    return fibList[n] # A függvény visszaadja a sorozat n. elemét.
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
