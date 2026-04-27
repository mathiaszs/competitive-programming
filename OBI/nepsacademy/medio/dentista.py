N = int(input())
agenda = []

for _ in range(N):
    X, Y = map(int, input().split())

    agenda.append((X, Y))

agenda.sort(key=lambda x: x[1])

final = [agenda[0]]

count = 0
for i, j in agenda:

    ultimo = len(final) - 1

    if i >= final[ultimo][1]:
        final.append((i, j))

    count += 1

tamanho = len(final)
print(tamanho)

a = 0
