#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
   
    if len(n) == 1 and k == 1:        # Alapeset, amikor a megadott sztring (szám) 1 karakterhosszú (1 számjegyből áll) és a 'k' szorzó értéke 1:
        return int(n)                 # ekkor magát a számjegyet (egy 0-9 közötti egész számot) adja vissza
        
    else:                                                                  # Ha 1-nél több karakterhosszú a sztring: 
        s1, s2 = n[:len(n)//2], n[len(n)//2:]                              # akkor a sztringet ketté választom s1 és s2 részre(ha n páros, akkor s1 és s2 ugyanakkora, len(n)/2 nagyságú sztring,
                                                                           # ha páratlan, akkor egy (len(n)-1/2) és egy (len(n-1)/2 + 1) nagyságú részre tagolja a sztringet).
        
        return superDigit(str(k*(superDigit(s1,1)+superDigit(s2,1))),1)    # Ezután rekurzívan meghívja a 'superDigit()' függvényt mindkét részre külön-külön. 
                                                                           # A kapott értékeket összeadja és megszorozza k-val, majd az így kapott új sztring (szám) superDigit-jét adja vissza.
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
