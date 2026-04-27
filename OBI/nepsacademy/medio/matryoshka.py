import sys

N = int(input())

bonecas = list(map(int, input().split()))

count = 0
anterior = bonecas[0]
lista = []

for i in range(1, N):

    if bonecas[i] > anterior:
        lista.append(bonecas[i])
        count += 1
    else:
        anterior = bonecas[i]

if count == 0:
    print("0")
    sys.exit()

print(count)
print(*lista)
