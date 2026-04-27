P = int(input())
LAB, count = [], []
for _ in range(P):
    l, a, b = list(map(int, input().split()))
    c, soma = 0, 0
    for i in range(a, b + 1):
        if soma < l:
            soma = soma + i
            c = c + 1
    count.append(c)
for i in count:
    print(i)
