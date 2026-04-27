def main():
    N, K = map(int, input().split())

    bancos = {i: [] for i in range(N + 1)}


    for _ in range(K):
        entrada = list(input().split())

        type = entrada[0]
        former = int(entrada[1])
        latter = int(entrada[2])

        if type == "F":
            # todas as conxeões de um e do outro são passadas
            bancos[former].append(latter)
            bancos[latter].append(former)

        if type == "C":
            # Fazer uma busca insana (DFS)

            visited = set()
            if dfs(bancos, former, latter, visited) == True:
                print("S")
            else:
                print("N")


def dfs(graph, node, goal, visited):
    if node in visited:
        return False

    if node == goal:
        return True

    visited.add(node)

    for neighbor in graph.get(node, []):
        if dfs(graph, neighbor, goal, visited):
            return True

    return False


if __name__ == "__main__":
    main()

