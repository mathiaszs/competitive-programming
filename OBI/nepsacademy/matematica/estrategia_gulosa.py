def main():
    N = int(input())
    S = [100, 50, 25, 10, 5, 1]

    count = 0
    for i in S:
        if i <= N:
            count += N // i
            N = N % i

    print(count)

if __name__ == "__main__":
    main()
