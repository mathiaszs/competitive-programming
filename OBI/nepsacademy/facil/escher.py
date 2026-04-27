import sys

N = int(input())
nums = list(map(int, input().split()))

protagonista = nums[0] + nums[N - 1]

j = N - 1
for i in range(N):

    soma = nums[i] + nums[j]

    if soma != protagonista:
        print("N")
        sys.exit()

    j -= 1

print("S")
