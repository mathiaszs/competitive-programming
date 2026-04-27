upp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

T = input()
uppercase, lowercase, digit = 0, 0, 0
new = []

for i in range(len(T)):
    if T[i] in low:
        lowercase += 1
        new.append(T[i])
    if T[i] in num:
        digit += 1
        new.append(T[i])
    if T[i] in upp:
        valor = upp.index(T[i])
        new.append(low[valor])
        uppercase += 1

resultado = "".join(new)
print(resultado)
print(digit)
print(lowercase)
print(uppercase)
