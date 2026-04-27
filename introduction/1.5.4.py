T = input()

lista = []
new = []
for i in range(len(T)):
    if i == len(T) - 1:
        lista.append(T[i])
        new.append("".join(lista))
        break
    if T[i] != " ":
        lista.append(T[i])
    if T[i + 1] == " ":
        new.append("".join(lista))
        lista = []

new.sort()
print(new)
