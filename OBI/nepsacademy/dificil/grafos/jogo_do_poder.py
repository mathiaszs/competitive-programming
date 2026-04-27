def main():

    N, M = map(int, input().split())

    poder = [[] for _ in range(N)]

    for i in range(N):
        entrada = list(map(int, input().split()))

        poder[i].append(entrada)

    # Vamos jogar!
    direcoes = [0, 1], [0, -1], [1, 0], [-1, 0]


    for i in range(N):
        for j in range(M):

            # Nessas condições, vamos jogar!

            atual = (i, j)
            strenght = poder[i][j] # força do personagem
            move(poder, atual, direcoes, N, M)


def move(poder, atual, direcoes, N, M):

    # Se mais nenhum movimento for possível (de forma que derrote), paramos

    # Guardar informações sobre lugares que eu poderia ter ido...
    # E fazer um "sort" dessa lista
    # Pode talvez guardar informação de onde esta localizado e quanto é o poder do monstro

    for d in direcoes:

        cim_bax = d + atual[0]
        dir_esq = d + atual[1]

        if (cim_bax >= 0
            and cim_bax < N
            and dir_esq >= 0
            and dir_esq < M):

            possivelNovo = atual + d
            if poder[possivelNovo] >= forca:
                atual = possivelNovo


if __name__ == "__main__":
    main()
