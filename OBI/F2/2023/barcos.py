N, B = map(int, input().split())

grafo = [[] for _ in range(N + 1)]

for _ in range(B):
    I, J, P = map(int, input().split())
    grafo[I].append((J, P))
    grafo[J].append((I, P))

C = int(input())
travel = []
for i in range(C):
    x, y = map(int, input().split)
    travel.append((x, y))

max_cap = 0
for i in range(1, N + 1):
    for vizinho, cap in grafo[i]:
        max_cap = max(max_cap, cap)

