# Encontrar cidade mais longe da cidade START
def dijkstra(graph, start, N):
    INF = 10 ** 18

    visited = {v: False for v in range(N)}
    distances = {v: INF for v in range(N)}
    distances[start] = 0

    queue = []
    queue.append(0, start)
    while queue:



    return max(distances)


def main():
    N, M = map(int, input().split())

    grafo = []

    for _ in range(M):
        U, V, W = map(int, input().split())
        grafo[U].append((V, W))
        grafo[V].append((U, W))

    lista = []
    distancias = [{i}: for i in range(N)]

    for start in range(N):
        distancias[i][i] = 0
        # MAIOR DISTÂNCIA se a cidade START for escolhida
        maximo = dijkstra(grafo, start, N)
        lista.append(maximo)

    print(min(lista))


if __name__ == "__main__":
    main()
