N, M = map(int, input().split())

barra = list(map(int, input().split()))
posicoes = list(map(int, input().split()))

somas = [[0 for _ in range(10)] for _ in range(N)]

# No momento i, qual a soma acumulada em tudo?
copia = False
for i in range(N):
    if copia:
        somas[i] = copia

    somas[i][barra[i]] += 1
    copia = somas[i].copy()

nums = [0 for _ in range(10)]

for i in range(1, M):

    # Pegar a diferença das duas listas -> indice mais alto - indice menos alto
    a = posicoes[i] - 1
    b = posicoes[i - 1] - 1

    anterior = min(a, b)
    proximo = max(a, b)

    # Fazer com um for
    for i in range(10):
        x = somas[proximo][i]
        y = somas[anterior][i]
        diff = x - y
        nums[i] += diff

    # Adicionar isso à lista principal

print(*nums)

a = 0
