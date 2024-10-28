#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    arr.sort()  # Rendezzük növekvő számsorrendbe a lista elemeit.
    
    sumDiff = 0 # Az összes kritériumnak megfelelő párt számláló változó.
    
    for i in range(len(arr)): # Végig iterálunk a lista elemein.
        
        for j in range(i, len(arr)): # Megnézzük az adott elemtől jobbra lévő (tehát nagyobb) számokat a listában.
            
            if arr[j] == arr[i] + k:  # Ha az i. indexű elemtől jobbra lévő aktuális egész szám akkora, mint az i. indexű elem + a célzott különbség,
                                      # akkor megtaláltuk az i. indexű elem párját.

                sumDiff += 1            # Hozzáadunk a számlálóhoz 1-et, majd
                break                   # kilépünk a belső ciklusból.
           
            elif arr[j] > arr[i] + k:    # Ha az i. indexű elemtől jobbra lévő aktuális egész szám nagyobb, mint a különbség + az i. indexű elem, akkor nincs értelme tovább keresni az i. indexű elem párját.
                break
    
    return sumDiff         # A végén visszaadja a függvény a talált párok számát.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
