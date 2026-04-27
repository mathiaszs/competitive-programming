L, C = map(int, input().split())

# Matrizes para armazenar variáveis e somas
variaveis = []     # matriz L x C com nomes das variáveis
somas_linha = []   # lista com a soma de cada linha

# Ler cada linha do passatempo
for _ in range(L):
    partes = input().split()
    linha_vars = partes[:-1]             # todas menos a última: variáveis
    soma = int(partes[-1])               # último valor: soma da linha
    variaveis.append(linha_vars)
    somas_linha.append(soma)

# Ler soma das colunas
somas_coluna = list(map(int, input().split()))

