ano_atual = int(input())

halley = []
halley.append(1986)

for i in range(1500):
    halley.append(int(halley[i]) + 76)

for i in range(1500):
    if ano_atual >= halley[i - 1] and ano_atual < halley[i]:
        print(halley[i])
