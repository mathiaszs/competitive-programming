E, M, D = map(int, input().split())

sim, uv, grupo = [], [], []

for _ in range(M):
    est = list(map(int, input().split()))
    sim.append((est[0], est[1]))
for _ in range(D):
    u, v = list(map(int, input().split()))
    uv.append((u, v))
for _ in range(int(E / 3)):
    i, j, k = list(map(int, input().split()))
    grupo.append((i, j, k))

geral = 0
for u, v in uv:
    for i, j, k in grupo:
        count = 0
        if u == i or u == j or u == k:
            count += 1
        if v == i or v == j or v == k:
            count += 1
        if count == 2:
            geral += 1

c = 0
for x, y in sim:
    for i, j, k in grupo:
        if x == i or x == j or x == k:
            if y == i or y == j or y == k:
                c += 1

if c != M:
    c = M - c

geral += c

print(geral)
