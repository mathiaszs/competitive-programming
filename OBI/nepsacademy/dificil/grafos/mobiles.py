from collections import deque

def main():
    N = int(input())

    pecas = {i: [] for i in range(N + 1)}

    for _ in range(N):
        a, b = map(int, input().split())

        # Peça B pendurada em A
        pecas[b].append(a)

    # Iterar no grafo, e ver se todas é igual ao len ou 0
    for key, values in pecas.items():
        resultados = []
        if values:
            for i in values:
                algo = bfs(pecas, i)
                resultados.append(algo)

            padrao = resultados[0]
            for i in resultados:
                if i != padrao:
                    print("mal")
                    return

    print("bem")


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        '''if node in visited:
            continue'''

        result = len(graph[node])
        return result

        '''visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)'''


if __name__ == "__main__":
    main()
