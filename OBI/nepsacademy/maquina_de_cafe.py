def main():
    A1 = int(input())
    A2 = int(input())
    A3 = int(input())

    A = [A1, A2, A3]

    soma = [0, 0, 0]

    for i in range(3):

        for j in range(3):
            if i == j:
                continue
            dif = abs(i - j)
            soma[i] += A[j] * dif * 2

    print(min(soma))

if __name__ == "__main__":
    main()
