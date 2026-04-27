N = int(input())

tabuleiro = []

for _ in range(N):
    entrada = list(map(int, input().split()))
    tabuleiro.append(entrada)

for i in range(1, N):
    for j in range(1, N):
        pretas = 0
        brancas = 0

        if tabuleiro[i][j - 1] == 0:
            brancas += 1
        if tabuleiro[i - 1][j - 1] == 0:
            brancas += 1
        if tabuleiro[i - 1][j] == 0:
            brancas += 1

        if brancas >= 2:
            tabuleiro[i][j] = 1
        else:
            tabuleiro[i][j] = 0

print(tabuleiro[N - 1][N - 1])

