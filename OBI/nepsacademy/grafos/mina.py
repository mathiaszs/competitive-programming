from collections import deque

def bfs(grafo, lista):

    visitados = set()
    fila = deque([0, 0])
    visitados.add((0, 0))
    count = 0

    while fila:
        vertice = fila.popleft()  # Remove o primeiro da fila (FIFO)
        count += 1

        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return ordem_visita


def main():
    N = int(input())

    mina = []
    for _ in range(N):
        entrada = list(map(int, input().split()))
        mina.append(entrada)

    lista = []
    final = bfs(mina, lista)
    print(final)
