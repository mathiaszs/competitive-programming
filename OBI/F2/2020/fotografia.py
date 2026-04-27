A, L = map(int, input().split())
N = int(input())

x, y = [], []
for i in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

moldura = []
for i, (a, b) in enumerate(zip(x, y)):
    if a >= A and b >= L:
        moldura.append(i)

if not moldura:
    print("-1")
    exit()

print(min(moldura) + 1)
