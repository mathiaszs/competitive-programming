N, L = map(int, input().split())

T = []

for _ in range(L):
    t = int(input())
    T.append(t)

# Se o seller i for 0, ele está oficialmente inativo
seller = [0 for _ in range(N)]
inativos = [i for i in range(N)]
count = [0 for _ in range(N)]

while True:

    # Iterar sobre jogadores ativos
    for i in range(len(inativos)):

        # Iterar sobre as calls que precisam ser passadas
        for j in range(len(T)):

            a = inativos[0]

            seller[a] = T[j]
            count[a] += 1
            del inativos[0]

            del T[j]

            break

        continue

    # O tempo está passando...
    # Ver o tempo maximo que posso diminuir pra alguem ficar 0
    o_minimo_maximo = min(seller)

    for i in range(len(seller)):
        seller[i] -= o_minimo_maximo

        if seller[i] == 0:
            inativos.append(i)

    if len(T) == 0:
        break

# pintar tudo
for i in range(N):

    print(f"{ i + 1 } { count[i] }")

a = 0
