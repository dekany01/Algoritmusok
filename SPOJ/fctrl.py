import sys

def Z(number):
    # Alapeset, ha 5-nél kisebb a szám
    if number < 5:
        return 0

    # A visszatérési értéket inicializáljuk azzal a számmal,  hányszor szerepel 5-tel osztható szám a faktoriális szorzatalakjában
    numberOfZeros = int (number / 5)

    # Ha 24-nél nagyobb számról van szó:
    if number > 24:

        test = 25
        while test <= number:
            numberOfZeros += int (number / test)
            test *= 5

    return numberOfZeros

def main():
    input = sys.stdin.readlines()
    T = int(input[0]) # Beolvassa, hogy hány db teszteset lesz

    for i in range (1,T + 1):

        N = int(input[i])
        print(Z(N))     # Adott tesztesetre elvégezi a számítást és kiírja a standard outputra

if __name__ == "__main__":
    main()
