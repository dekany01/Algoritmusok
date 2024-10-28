#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    
    minUnfair = 10**9  # Ebben a változóban tároljuk el a legkisebb értéket, amit a függvény később visszaad.
                       # Miután a megengedett legkisebb szám 0, a legnagyobb pedig 10^9 lehet, 
                       # ezért a várható legkisebb érték 10^9-nél nem lehet nagyobb.
            
    
    arr.sort()         # Szám szerint növekvő sorrendbe tesszük a lista elemeit.
                       # Ezáltal a nagyságrendileg hasonló méretű számok egymáshoz közelebb lesznek.
    
    for i in range(len(arr)-k+1):    # A rendezett lista elemeit végig iteráljuk úgy, hogy a lista utolsó elemétől visszaszámolunk 'k+1' darabot.

        minArr = arr[i+k-1] - arr[i]  # Felesleges résztömbökre (részlistákra python esetében) bontanunk a teljes tömböt, hiszen
                                      # a rendezett listában egy adott elemtől jobbra lévő számok mindig nagyobbak,
                                      # ezért az aktuális elemet tekinthetjük minimumnak és az attól jobbra 'k-1' távolságra lévő elemet a maximumnak.
                                      # ('k-1', mert egy k elemszámú tömb első eleme a 0. indexű, akkor a k-1. az utolsó)
                                      # A fentiek miatt is kell csak a lista utolsó elemétől visszaszámolni k+1 távolságot.
        
        if minArr < minUnfair:        # Megnézzük, hogy az aktuálisan vizsgált elem kisebb-e, mint az eddigi legkisebb "igazságtalansági" érték.
            minUnfair = minArr        # Ha igen, akkor az lesz az új legkisebb "igazságtalansági" érték.
            
    return minUnfair

        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
