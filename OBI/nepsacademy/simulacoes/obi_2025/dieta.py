# Reiniciar

N, M = map(int, input().split())

soma = 0

for i in range(N):
    P, G, C = map(int, input().split())

    P *= 4
    G *= 9
    C *= 4

    soma += P + G + C

diff = M - soma
print(diff)
