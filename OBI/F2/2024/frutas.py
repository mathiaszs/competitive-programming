R, N = map(int, input().split())

tp = []
for _ in range(N):
    entrada = list(map(int, input().split()))
    tp.append([entrada[0], entrada[1]])

tp = sorted(tp)
count = 0
for _ in range(5):
    for i, j in tp:
        if i > 0:
            if R > j:
                count += 1
                i -= 1
                R = R - j
print(count)
