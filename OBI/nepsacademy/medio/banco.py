C, N = map(int, input().split())

cliente = []

for _ in range(N):
    T, D = map(int, input().split())

    cliente.append((T, D, 0))

time = 0
caixa = [0 for _ in range(C)]

fila = []
atendimento = []
finalizado = []

count = 0

sofrido = [0 for _ in range(N)]

'''embutir isso no primeiro loop'''
# Criar uma variável para ir guardando a soma dos tempos que precisarão ser usadoss
'''soma_tempos = []

anterior = cliente[0][0]
for i in range(N):
    proximo += anterior + cliente[i][T] # proximo nn definido
    soma_tempos.append(proximo)

    anterior = proximo
'''

# Ir iterando sobre os clientes
while True:

    # SE TEM UM CLIENTE AINDA NÃO ATENDIDO que está no tempo, colocar na fila

    for i in range(N):

        adicionado = False

        # Só se ele não foi visitado ainda -> Visitado é quando entra na fila de atendimento

        if i not in atendimento and i not in finalizado:

                # CONTINUAMOS

            # Conferir se tem mais um cliente
            # Se tiver um caixa livre, o cliente é atendido e se o número de espera dele for maior que 20 então choramos
            if cliente[i][0] == time:

                fila.append(i)

                # Tem caixa disponível?

                for c in range(C):
                    if c == 0:
                        caixa[c] = cliente[i][1]
                        fila.remove(i) # Cliente nº i
                        atendimento.append(i)

                        # Se a espera dele foi maior ou igual a 20, senta e chora bebe
                        if sofrido[i] >= 20:
                            count += 1

                        break

                '''if adicionado:
                    continue'''

                # Mudar o tempo de todos os caixas


    # PRIMEIRO PASSAR PELO PASSA FOME QUE QUER ENTRAR NA PORRA DA FILA E SÓ DPS ISSO

    # Atualizar o tempo
        # De acordo com a soma dos tempos ou quem precisa ser atendido?
    # Atualizar o tempo dos caixas

    min_espera = min(caixa)

    time += min_espera

    # Encontrar esse cliente safado que terminou o atendimento e colocar como finalizado


    # Diminuir tempo de todas as filas
    for f in fila:
        f -= min_espera

    # Somar os sofridos que estão na espera
    for f in fila:
        sofrido[i] += min_espera


    # TALVEZ POSSO DIMINUIR O TEMPO MÍNIMO DA MINHA LISTA DE CAIXAS
    for c in range(C):
        caixa[c] -= min_espera

    # lista de finalizado pra descobrir quando acaba essa porra
    # Se o tamanho do finalizado for igual a N, acabar essa poha e imprimir count

    if len(finalizado) == N:
        break


print(count)
