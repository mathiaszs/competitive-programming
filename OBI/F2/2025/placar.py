entrada = list(map(int, input().split()))

P = entrada[0]
p = []
for i in range(len(entrada)):
    if i != 0:
        p.append(entrada[i])

input = list(map(int, input().split()))

C = input[0]
c = []
for i in range(len(input)):
    if i != 0:
        c.append(input[i])

placar, lista = [], []
count_c, count_p = 0, 0

for i in p:
    placar.append(i)

for i in c:
    placar.append(i)

placar = sorted(placar)

for i in placar:
    for a in p:
        if i == a:
            count_p += 1
            lista.append((count_p, count_c))
    for b in c:
        if i == b:
            count_c += 1
            lista.append((count_p, count_c))

print("0 0")
for i, j in lista:
    print(f"{i} {j}")

