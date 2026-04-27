import sys

N = int(input())

contrario = []

if N % 2 == 0:
    limite = N // 2
else:
    limite =  N // 2 + 1

for i in range(1, limite + 1):


    nums  = []

    # Se i for 1, então haverá só um número repetindo N vezes
    # Se i for 2, então vai ter uma escala até 2, que vai se repetir até N // 2 + 1, e depois o contrário

    for j in range(1, N):


        # Se a escalinha já acabou:
        if j == i:

            verdadeiro = False

            while True:

                nums.append(j)

                if len(nums) == limite:
                    new = sorted(nums, reverse=True)

                    if N % 2 != 0:
                        del new[0]

                    for i in new:
                        nums.append(i)
                    verdadeiro = True

                    break

            if verdadeiro:
                print(*nums)
                contrario.append(nums)
                break

        nums.append(j)

if N % 2 != 0:

    ultimo = len(contrario) - 1
    del contrario[ultimo]

    for i in range(limite - 2, -1, -1):
        print(*contrario[i])
else:
    for i in range(limite, 0, -1):
        print(*contrario[i - 1])

# 67 lines of code

a = 0
