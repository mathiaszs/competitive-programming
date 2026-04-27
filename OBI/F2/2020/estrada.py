T = int(input())
N = int(input())

x = []
x.append(0)
for i in range(N):
    x.append(int(input()))
x.append(T)
x.sort()

area = []
for i in range(1, len(x) - 1):
    if i == 1:
        a = x[i] + ((x[i + 1] - x[i]) / 2)
    elif i == len(x) - 2:
        a = ((x[i] - x[i - 1]) / 2) + (x[i + 1] - x[i])
    else:
        a = ((x[i] - x[i - 1]) / 2) + ((x[i + 1] - x[i]) / 2)

    area.append(a)

print(f"{min(area):.2f}")
