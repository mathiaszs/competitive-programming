N, M = map(int, input().split())

G, mod = [], []

for _ in range(N):
    sim = list(map(int, input().split()))
    G.append(sim)
    mod.append(sim)

count = 0
for i in range(N):
    for j in range(M):
        if i + 1 < N:
            if G[i][j] % 2 == 0 and G[i + 1][j] % 2 == 0:
                mod[i + 1][j] += 1
                count += 1
            if G[i][j] % 2 == 1 and G[i + 1][j] % 2 == 1:
                mod[i + 1][j] += 1
                count += 1

print(count)
for i in mod:
    print(i)

