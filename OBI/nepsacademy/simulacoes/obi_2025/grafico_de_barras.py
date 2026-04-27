N = int(input())

nums = list(map(int, input().split()))

maior = max(nums)
lista_invertida = []

for n in nums:


    temp = []
    for i in range(maior):
        if i < n:
            temp.append(1)
        else:
            temp.append(0)

    lista_invertida.append(temp[::-1])

new = []
for i in range(maior):
    for j in range(len(lista_invertida)):

        aura = lista_invertida[j][i]
        if j == len(lista_invertida) - 1:
            print(aura)
        else:
            print(aura, end=" ")

a = 0
