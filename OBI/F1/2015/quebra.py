N = int(input())
word = []

for i in range(N):
    word.append(list(input().split())) # talvez não precisa do map

# encontrar a primeira letra
for i, j, k in word:
    for a, b, c in word:
        count = 0
        if i[0] != c[0]:
            count += 1
        if count == (N - 1):
            first = j
            print(first)


# seguir a sequência

