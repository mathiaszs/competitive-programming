S, T, P = map(int, input().split())

A = []
A = list(map(int, input().split()))

i, j = [], []
for a in range(T):
    s, n = map(int, input().split())
    i.append(s)
    j.append(n)

count = 0
for x in A:
    if A[P - 1] > x:
        count += 1

print(count)
