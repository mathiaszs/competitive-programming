import sys

N = int(input())

lista = list(map(int, input().split()))
lista.sort()

if lista[0] <= 8:

    for i in range(1, N):
        if lista[i] - lista[i - 1] > 8:
            print("N")
            sys.exit()
    print("S")
else:
    print("N")
