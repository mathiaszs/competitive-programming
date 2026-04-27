N, K = list(map(int, input().split()))

lista1, lista2, lista3, lista4 = [], [], [], []
possible = [[None] * 0 for _ in range(K)]

for a in range(K):
    X, Y, D = list(map(int, input().split()))

    # Transformar a distância em coordenadas reais. Tipo, distância 3:
    # [(0, 3), (3, 0), (1, 2), (2, 1), (0, -3), (-3, 0), (-1, -2), (-2, -1), ...]
    # A SOMA DOS MÓDULOS DAS COORDENADAS DEVE SER 3
    # JÁ SEI! uma lista de tudo positivo, outra do primeiro positivo, outra do segundo positivo e outra de nenhum positivo

    # Preciso encontrar dois números que somados são igual a D
    for i in range(D + 1):
        for j in range(D + 1):
            if i + j == D:
                lista1.append((i, j))
                lista2.append((-i, j))
                lista3.append((i, -j))
                lista4.append((-i, -j)) # PERFEITOOOOOOO!
    lista_unida = list(set(lista1) | set(lista2) | set(lista3) | set(lista4))

    # Depois dessa lista, pegamos cada elemento e somamos com x e y
    # e se não ultrapassar o quadriculado, então guardamos a coordenada (a lista delas)
    for i, j in lista_unida:
        if X + i >= 0 and X + i < N:
            if Y + j >= 0 and Y + j < N:
                possible[a].append((X + i, Y + j))

 # depois tentamos encontrar coordenadas que estão em todos os valores
# se tiver uma, agente printa, se tiver duas printa -1 -1
a = possible[0]
for i in range(K - 1):
    a = list(set(a) & set(possible[i + 1]))
final = a

if len(final) == 1:
    print(*final[0])
else:
    print("-1 -1")
