from math import sqrt
import sys


def primo(num):

    boundary = int(sqrt(num)) + 1

    for i in range(2, boundary):
        if num % i == 0:
            return False
    return True


def main():
    N = int(input())

    if N == 0 or N == 1:
        sys.exit()

    for i in range(2, N + 1):

        num = primo(i)

        if num:
            print(i, end=" ")

if __name__ == "__main__":
    main()
