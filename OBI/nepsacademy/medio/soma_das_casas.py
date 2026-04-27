import sys

N = int(input())

nums = []
for _ in range(N):
    entrada = int(input())
    nums.append(entrada)

K = int(input())

right = N - 1
for left in range(N):
    sum = nums[left] + nums[right]

    if sum == K:
        print(nums[left], nums[right])
        break

    if sum < K:
        left += 1

    if sum > K:
        right -= 1

