N, M = map(int, input().split())

paises = [[0, 0, 0, i] for i in range(N + 1)]

for _ in range(M):
    O, P, B = map(int, input().split())

    paises[O][0] += 1
    paises[P][1] += 1
    paises[B][2] += 1

paises.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))

for p in paises:
    if p[3] != 0:
        print(p[3], end=" ")

