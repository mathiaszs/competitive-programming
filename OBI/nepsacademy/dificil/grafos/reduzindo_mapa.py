from collections import defaultdict

def main():

    N, M = map(int, input().split())

    rodovias = []

    for _ in range(M):
        U, V, C = map(int, input().split())

        rodovias.append((U, V, C))

    rodovias.sort(key=lambda x: x[2])

    total = 0
    novoGrafo = defaultdict(list)
    for u, v, peso in rodovias:

        # Já existe um caminho entre U e V?
            # Se sim: ir pra próxima
            # Se não: adicionar aresta

            # Se em um momento todos já tiverem conectados, perfeito, vamos acabar o programa

        visited, completo = [], []
        aura = caminho(novoGrafo, u, v, visited, completo) # Grafo novo, cidades, visitados, completo

        if aura == False:
            # Adicionar no grafo
            novoGrafo[u].append(v)
            novoGrafo[v].append(u)
            total += peso

        if len(completo) == N:
            break

    print(total)


def caminho(novoGrafo, start, goal, visited, completo):
    visited.append(start)

    completo.append(start)

    for i in novoGrafo[start]:
        if i == goal:
            return True

        if i not in visited:
            if caminho(novoGrafo, i, goal, visited, completo):
                return True

    return False


if __name__ == "__main__":
    main()
