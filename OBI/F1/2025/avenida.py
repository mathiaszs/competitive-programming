d = int(input())

ponto = [0, 400, 800, 1200, 1600, 2000]
x = []

for i in ponto:
    if d > i:
        x.append(d - i)
    if d == i:
        x.append(0)
    if d < i:
        x.append(i - d)

print(min(x))
