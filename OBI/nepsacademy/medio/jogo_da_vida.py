import copy

N, Q = map(int, input().split())

nums = []

for _ in range(N):
    entrada = input()
    lista = [int(c) for c in entrada]
    nums.append(lista)

for _ in range(Q):
    new = copy.deepcopy(nums)

    for i in range(N):
        for j in range(N):

            vizinhas = 0 # vivas

            if i - 1 >= 0:
                if nums[i - 1][j] == 1:
                    vizinhas += 1
            if j - 1 >= 0:
                if nums[i][j - 1] == 1:
                    vizinhas += 1
            if i - 1 >= 0 and j - 1 >= 0:
                if nums[i - 1][j - 1] == 1:
                    vizinhas += 1
            if i + 1 < N:
                if nums[i + 1][j] == 1:
                    vizinhas += 1
            if j + 1 < N:
                if nums[i][j + 1] == 1:
                    vizinhas += 1
            if i + 1 < N and j + 1 < N:
                if nums[i + 1][j + 1] == 1:
                    vizinhas += 1
            if i + 1 < N and j - 1 >= 0:
                if nums[i + 1][j - 1] == 1:
                    vizinhas += 1
            if i - 1 >= 0 and j + 1 < N:
                if nums[i - 1][j + 1] == 1:
                    vizinhas += 1

            if vizinhas == 3 and nums[i][j] == 0:
                new[i][j] = 1
            if nums[i][j] == 1:
                if vizinhas != 2 and vizinhas != 3:
                    new[i][j] = 0

    nums = new

for i in range(N):
    print(*nums[i], sep='')
