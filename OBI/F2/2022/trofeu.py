N = 5
nota = []
for _ in range(N):
    entrada = input()
    nota.append(entrada)

maior = nota[0]
trofeu, placa, segundo = 0, 0, 0

for i in range(len(nota)):
    if nota[i] == maior:
        trofeu += 1
    if nota[i] != maior:
        segundo = nota[i]
        break

for i in range(N):
    if nota[i] == segundo:
        placa += 1

print(f"{trofeu}", end=" ")
print(placa)
