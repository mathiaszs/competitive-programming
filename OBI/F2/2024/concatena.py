entrada = list(map(int, input().split()))
N = entrada[0]
Q = entrada[1]
valores = list(input().split())

perguntas = []
for _ in range(Q):
    a, b = map(int, input().split())
    perguntas.append((a, b))

# Ir sobre as perguntas
sum = []
for x, y in perguntas:
    s = 0
    x = x - 1
    y = y - 1
    for i in range(x, y + 1):
        for j in range(x, y + 1):
            if i != j:
                s += int(valores[i] + valores[j])
    sum.append(s)

for i in sum:
    print(i)

