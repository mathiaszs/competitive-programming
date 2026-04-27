def main():
    # Seu código vai aqui
    N = int(input())
    fita = list(map(int, input().split()))

    new = [None for _ in range(N)]

    posicao = []

    for i in range(N):
        if fita[i] == 0:
            posicao.append(i)

    fim = len(posicao)

    for i in range(len(posicao)):

        # LEFT
        if i == 0:
            lim_left = posicao[i]
        else:
            diff = posicao[i] - posicao[i - 1]
            lim_left = diff // 2

        # RIGHT
        if i == fim - 1:
            lim_right = N - posicao[i] - 1 # será?
        else:
            diff =  posicao[i + 1] - posicao[i]
            lim_right = diff // 2

        max_left = posicao[i] - lim_left
        max_right = posicao[i] + lim_right + 1

        for p in range(max_left, max_right):

            new[p] = abs(posicao[i] - p)


    print(*new)

if __name__ == "__main__":
    main()
