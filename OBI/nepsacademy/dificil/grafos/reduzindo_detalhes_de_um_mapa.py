5 6
1 2 15
1 3 10
2 3 1
3 4 3
2 4 5
4 5 20'''import copy

def main():
    N, M = map(int, input().split())

    grafo = {i: [] for i in range(N + 1)}
    total = 0

    for _ in range(M):
        U, V, C = map(int, input().split())

        total += C

        grafo[U].append((V, C))
        grafo[V].append((U, C))

    # Anotações iniciais:

    # O(n) -> n
    # O(n2)
    # O(N log N)

    # Cada cidade deve estar conectada às outras (mesmo indiretamente)
    # Tenho que encontrar a menor soma, desde que as cidades estejam conectadas

    # Inicialmente, a maior dificuldade será ter confirmação que todos ainda estão conectados

    # Eu teria que iterar s

    # O que eu pensei é fazer um O(n²) -> eu itero sobre uma distância e vejo quantas outras eu posso elimitar e aí somo

    # Primeiro uma pergunta: tem um caminho mais rápido entre A e B? (indireto)
        # Se sim, se eu removesse, o caminho entre a rapaziada existiria?
            # Se sim, então removemos essa bagaça

            # RESOLVENDO ASSIM, TEM UM PROBLEMA QUE EU PODERIA ME PREOCUPAR, mas não sei se se materializa

            # Ter um outro grafo (copiado) que guarda a menor distância entre A e B

    # Vi um vídeo e tive um insight:

    # Vou iterar sobre os pontos do mapa, tirando o pior
    # Eliminando os outros
    # Desde que todas se conectem (talvez criar uma função de CONECTADOS - usando visiteds)

    for i, (vizinho, peso) in enumerate(listas):

            grafoDiferente = copy.deepcopy(grafo)
            del grafoDiferente[g][i]

            visited = [1]
            aura = conectados(grafoDiferente, 1, M, visited)

            if aura:
                del grafo[g][i]
                # del grafo[vizinho]
                total -= peso

    # Sorting a graph by PESO
    for no in grafo:
        grafo[no].sort(key=lambda x: x[1], reverse=True)

    for g in range(1, N + 1):
        i = 0

        while i < len(grafo[g]):

            vizinho, peso = grafo[g][i]

            grafoDiferente = copy.deepcopy(grafo)

            # remove nos dois lados
            del grafoDiferente[g][i]

            for j, (v, p) in enumerate(grafoDiferente[vizinho]):
                if v == g:
                    del grafoDiferente[vizinho][j]
                    break

            start = g
            goal = vizinho
            visited = [1, goal]
            aura = conectados(grafoDiferente, start, N, goal, visited)

            if aura:
                # remove no grafo original
                del grafo[g][i]

                for j, (v, p) in enumerate(grafo[vizinho]):
                    if v == g:
                        del grafo[vizinho][j]
                        break

                total -= peso
            else:
                i += 1

    print(total)


def conectados(grafo, start, N, goal, visited):

    for i, p in grafo[start]:

        if i == goal:
            return True
        elif i not in visited:
            visited.append(i)
            start = i
            if conectados(grafo, start, N, goal, visited):
                return True

    return False


if __name__ == "__main__":
    main()'''


def main():

    N, M = map(int, input().split())

    grafo = {i: [] for i in range(N + 1)}
    rodovias = [[] for _ in range(M + 1)]

    for i in range(M):
        U, V, C = map(int, input().split())

        grafo[U].append((V, C))
        grafo[V].append((U, C))

        rodovias[i].append((U, V, C))


    a = 0




if __name__ == "__main__":
    main()
