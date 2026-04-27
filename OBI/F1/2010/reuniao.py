import heapq

def main():
    N, M = list(map(int, input().split()))

    # LISTA DE ADJACÊNCIA
    grafo = []
    for i in range(N):
        grafo.append([])

    for i in range(M):
        u, v, w = list(map(int, input().split()))

        grafo[u].append((v, w))
        grafo[v].append((u, w))

    # "No dijkstra, para cada i encontramos a distância de todas as cidades" GPT
    resposta = 10**9

    for i in range(N):
        dist = dijkstra(i, grafo, N)
        pior = max(dist)
        resposta = min(resposta, pior)

    print(resposta)

def dijkstra(inicio, grafo, N):

    '''INF representa “distância infinita”
    No começo, não sabemos a distância para nenhuma cidade'''

    INF = 10**9
    dist = [INF] * N

    # A distância da cidade pra ela mesma é 0
    dist[inicio] = 0

    '''A fila guarda pares (distância, cidade)
    Começamos com a cidade inicial'''

    fila = []
    heapq.heappush(fila, (0, inicio))

    while fila:
        dist_atual, cidade = heapq.heappop(fila)

        if dist_atual > dist[cidade]:
            continue

        for vizinho, peso in grafo[cidade]:
            nova_dist = dist_atual + peso
            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist
                heapq.heappush(fila, (nova_dist, vizinho))

    return dist

if __name__ == "__main__":
    main()
