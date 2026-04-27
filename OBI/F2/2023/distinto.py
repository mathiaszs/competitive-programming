N = int(input())
sequencia = []

for _ in range(N):
    linha = input()
    numeros = map(int, linha.split())
    sequencia.extend(numeros)

c, values = [], []
count = 0
for i in range(len(sequencia)):
    for j in range(i + 1, len(sequencia)):

        if sequencia[j] in values or j == len(sequencia) - 1:
            c.append(count)
            count = 0
            values.clear()

        if not sequencia[j] in values:
            count += 1
            values.append(sequencia[j])

if c:
    print(max(c))
