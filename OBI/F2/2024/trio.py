N = int(input())
tri = list(map(int, input().split()))

count = 0
for a in range(len(tri)):
    for b in range(len(tri)):
        for c in range(len(tri)):
            if a != b and a != c and b != c:
                m = [tri[a], tri[b], tri[c]]
                m = sorted(m)
                if m[0] + m[1] > m[2]:
                    count += 1

count = count // 6
print(count)
