N, M, K = map(int, input().split())

# declarar lista bidimensional, tudo valendo 0, tamanho N, M:
exp = [[0 for _ in range(N)] for _ in range(M)]

coli, direcao = [], []
for _ in range(K):
    a, b, c = input().split()
    C = int(a)
    L = int(b)
    D = c[0]
    coli.extend([C, L])
    direcao.append(D)

for (c, l), d in zip(coli, direcao):
    if d == 'N':
        for i, j in exp:
            if i <= c:
                exp[i][l] = 1
    if d == 'S':
        for i, j in exp:
            if i >= c:
                exp[i][l] = 1
    if d == 'L':
        for i, j in exp:
            if j >= l:
                exp[c][j] = 1
    if d == 'O':
        for i, j in exp:
            if j <= l:
                exp[c][j] = 1

print(exp)
