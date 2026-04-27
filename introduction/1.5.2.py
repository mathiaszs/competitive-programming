T = 'I love CS3233 Competitive Programming. i also love AlGoRiThM'
P = 'love'

tamanho = len(P)
final = []
find = False

for i in range(len(T)):
    fim = tamanho + i
    if T[i:fim] == P:
        final.append(i)
        find = True

if not find:
    print("{-1}")
else:
    print(*final)
