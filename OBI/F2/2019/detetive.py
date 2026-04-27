def main():
    E, I, V = map(int, input().split())

    AB = []
    for _ in range(I):
        entrada = list(map(int, input().split()))
        AB.extend([entrada[0], entrada[1]])

    X = list(map(int, input().split()))

    # v, c = [], []
    maior = max(AB)
    for i in range(maior):
        print(f"{ i }", end=" ")

'''    recursion(X, AB, v, c)

def recursion(x, ab, verdadeiro, causa):
    count = 0

    # recursão
    for n in x:
        for i, j in ab:
            if n == j:
                verdadeiro.append(j)
                causa.append(i)
                count += 1

    if count == 1:
        verdadeiro = verdadeiro.sort
        for i in range(len(verdadeiro)):
            print(f"{ verdadeiro[i] }", end="")
'''
