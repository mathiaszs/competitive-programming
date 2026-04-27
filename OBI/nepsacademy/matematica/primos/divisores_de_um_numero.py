import sys

def divisores(N):

    lista = [1, N]

    boundary = N // 2 + 1

    for b in range(2, boundary):
        if N % b == 0:
            lista.append(b)

    return lista


def main():
    # E se N = 0? e 1?
    N = int(input())

    if N == 1:
        print(f"1 divisor(es): 1")
        print(f"Soma de divisores = 1")
        print("Nao primo")
        sys.exit()

    lista = divisores(N)
    lista.sort()

    if len(lista) == 2:
        print(f"2 divisor(es): 1 { N }")
        print(f"Soma de divisores = { N + 1 }")
        print("Primo")
    else:
        print(f"{ len(lista) } divisor(es):", end=" ")
        sum, c = 0, 0
        for i in lista:
            c += 1
            sum += i
            if c == len(lista):
                print(i)
                break
            print(i, end=" ")

        print(f"Soma de divisores = { sum }")
        print("Nao primo")


if __name__ == "__main__":
    main()
