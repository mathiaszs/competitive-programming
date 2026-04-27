import sys
from math import sqrt

def main():

    N, M = map(int, input().split())

    for i in range(M, 1, -1):

        aura = primo(i)
        if aura:
            print(i)
            sys.exit()

    print(1)

def primo(i):

    limite = int(sqrt(i)) + 1

    for s in range(2, limite + 1):
        if i % s == 0:
            return False

    return True


if __name__ == "__main__":
    main()
