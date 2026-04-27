N = int(input())
suditos = [for _ in range(1, N + 1)]
M = int(input())

div = []
for _ in range(M):
    entrada = int(input())
    div.append(entrada)

for i in range(N): # Pode ser até 1B
    for j in div:   # Pode ser até 5000

        removidas = []
        while True:


