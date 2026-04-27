N = int(input())
L = list(map(int, input().split()))

count = 0
for i in range(N - 1):
    if L[i] != L[N - i - 1]:
        x = L[i] + L[N - i - 1]
        L[i] = x
        L[N - i - 1] = x
        count += 1

print(count)
