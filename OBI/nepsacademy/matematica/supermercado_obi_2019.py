N = int(input())

preco = []

for i in range(N):
    a, b = map(float, input().split())
    div = a / b
    preco.append(div)

minimo = min(preco) * 1000
print(f"{minimo:.2f}")
