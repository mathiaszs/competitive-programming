dia, mes, ano = map(int, input().split())

# Quantos dias atrás isso foi?
passado = (365 * (ano - 1)) + ((ano - 1) // 4) + ((ano - 1) // 400) + ((mes - 1) * 30) + dia
atual = (365 * (2025)) + ((2025) // 4) + 103

diff = atual - passado - 2
result = diff % 7

lista = ["Quarta-feira", "Terça-feira", "Segunda-feira", "Domingo", "Sábado", "Sexta-feira", "Quinta-feira"]

print(lista[result])
