from math import sqrt


def dist(A, B):
    X = (A[1] - B[1]) ** 2
    Y = (A[0] - B[0]) ** 2

    d = sqrt(X + Y)
    return d


def main():
    N = int(input())

    coords = []

    for _ in range(N * 2):
        lista = input().split()
        X = int(lista[1])
        Y = int(lista[2])

        coords.append((X, Y))

    nums = []

    for i in range(N * 2):
        for j in range(N * 2): # diferente de i

            if i == j:
                continue

            distancia = dist(coords[i], coords[j])
            distancia = round(distancia, 2)
            nums.append((i, j, distancia))

            # se já existe...

    # Sortear pelas menores distancias
    nums.sort(key=lambda x: x[2])

    soma = 0
    usadas = []

    for i, j, d in nums:

        if i not in usadas and j not in usadas:
            soma += d
            usadas.append(i)
            usadas.append(j)

    print(f"{soma:.2f}")


if __name__ == "__main__":
    main()
