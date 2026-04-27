def change(shelf, i, j, N, M):

        if i + 1 >= N:
            return

                    if shelf[i + 1][j] == "#":

                            if j - 1 >= 0 and shelf[i][j - 1] == '.':
                                        shelf[i][j - 1] = "o"
                                                    change(shelf, i, j - 1, N, M)

                                                            if j + 1 < M and shelf[i][j + 1] == '.':
                                                                        shelf[i][j + 1] = "o"
                                                                                    change(shelf, i, j + 1, N, M)

                                                                                        elif shelf[i + 1][j] == ".":
                                                                                                shelf[i + 1][j] = "o"
                                                                                                        change(shelf, i + 1, j, N, M)

                                                                                                            elif shelf[i + 1][j] == "o":
                                                                                                                    return


                                                                                                                    def main():

                                                                                                                        N, M = map(int, input().split())

                                                                                                                            shelf = []

                                                                                                                                for _ in range(N):
                                                                                                                                        entrada = list(input())

                                                                                                                                                shelf.append(entrada)

                                                                                                                                                    for j in range(M):

                                                                                                                                                            if shelf[0][j] == "o":

                                                                                                                                                                        change(shelf, 0, j, N, M)

                                                                                                                                                                            for a in range(N):
                                                                                                                                                                                    print(*shelf[a])


                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                        main()
