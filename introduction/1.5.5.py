T = input()

words = {}

for i in range(len(T)):
    if i == len(T) - 1:
        lista.append(T[i])
        new.append("".join(lista))
        break
    if T[i] != " " and T[i] == "," and T[i] == ".":
        lista.append(T[i])

    if T[i + 1] == " " or T[i + 1] == "," or T[i + 1] == ".":
        new = "".join(lista)

        if new in words:
            words[new] += 1
