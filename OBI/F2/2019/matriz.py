L, C = map(int, input().split())

matriz = [list(map(int, input().split())) for _ in range(L)]

count = 0
for i in range(L):
    for j in range(C):
        x = matriz[0][0] + matriz[i][j]
        y = matriz[0][j] + matriz[i][0]
        if x >= y:
            count += 1

print(count)
