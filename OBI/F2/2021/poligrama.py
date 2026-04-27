N = int(input())
P = input()

# Encontrar possiveis divisores de N
divisor = []
for i in range(N):
    if N % i == 0:
        divisor.append(i)

# Dividir a string por um divisor
for div in divisor:
    # x = 6 / 2
    x = len(P) / div

    part = []
    # Acessar primeiro [0][1][2], dps [3][4][5]
    # ir de parte em parte da string
    for n in range(div):
        for eita in range(x):
            part[n].append(P[eita])

    for i in range(div) - 1:

        if part[i] == part[i + 1]:
            count += 1

    if count == div:
# Identificar se a quantidade de  determinadas letras é igual

# Se for igual vamos pegar a primeira parte da string
