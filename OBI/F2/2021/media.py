A, B = map(int, input().split())

for mediana in [A, B, (A + B) // 2]:
    C = 3 * mediana - A - B
    if sorted([A, B, C])[1] == mediana:
        print(C)
        break
