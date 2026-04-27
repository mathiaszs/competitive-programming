N = int(input())

nums = []
soma = 0

for _ in range(N):
    num = int(input())
    nums.append(num)

nums.sort(reverse=True)

for i in range(0, N, 3):

    # Não sei se a partir de nums[i + 1] existe
    if i + 2 < N:
        new = [nums[i], nums[i + 1], nums[i + 2]]
    elif i + 1 < N:
        new = [nums[i], nums[i + 1]]
    else:
        new = [nums[i]]

    if len(new) == 3:
        maximo = min(new)
        new.remove(maximo)

        soma += new[0] + new[1]

    else:
        for i in new:
            soma += i

print(soma)
