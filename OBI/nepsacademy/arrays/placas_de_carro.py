placa = input()

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(placa) == 8:
    if (placa[0] in alfabeto
        and placa[1] in alfabeto
        and placa[2] in alfabeto
        and placa[3] == '-'
        and int(placa[4]) in nums
        and int(placa[5]) in nums
        and int(placa[6]) in nums
        and int(placa[7]) in nums):
        print(1)
    else:
        print(0)

elif len(placa) == 7:
    if (placa[0] in alfabeto
        and placa[1] in alfabeto
        and placa[2] in alfabeto
        and int(placa[3]) in nums
        and placa[4] in alfabeto
        and int(placa[5]) in nums
        and int(placa[6]) in nums):
        print(2)
    else:
        print(0)

else:
    print(0)
