# ISSO É IMPOSSIVEL!
# Matheus de 2026 fala:
# "Tudo é possível ao que crê"

N, M = map(int, input().split())

matriz = [[None for _ in range(M)] for _ in range(N)]
poder = [[None for _ in range(M)] for _ in range(N)]
update = [[None for _ in range(M)] for _ in range(N)]
for i in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for i in range(N):
    for j in range(M):
        poder[i][j] = matriz[i][j]
        power = poder[i][j]

        if i + 1 < N and power >= poder[i + 1][j]:
            poder[i + 1][j] += power
            power = poder[i + 1][j]
            poder[i][j] = 0

        if i - 1 < N and power >= poder[i - 1][j]:
            poder[i - 1][j] += power
            power = poder[i - 1][j]
            poder[i][j] = 0

        if j + 1 < M and power >= poder[i][j + 1]:
            poder[i][j + 1] += power
            power = poder[i][j + 1]
            poder[i][j] = 0

        if j - 1 < M
        and power >= poder[i][j - 1]:
            poder[i][j - 1] += power
            power = poder[i][j - 1]
            poder[i][j] = 0





        if poder[i]
        for a in range(-1, 2):
            for b in range(-1, 2):

                if poder[i][j] >= poder[i + a][j + b] and poder[i + a][j + b]:


