#include <stdio.h>
#include <stdlib.h>

#define MAX 1001  // Número máximo de salões (ajuste se necessário)

int grafo[MAX][MAX]; // Matriz de adjacência
int main() {
    int S, T;
    scanf("%d %d", &S, &T);

    // Inicializa a matriz de adjacência
    for (int i = 1; i <= S; i++) {
        for (int j = 1; j <= S; j++) {
            grafo[i][j] = 0;
        }
    }

    // Lê os túneis e preenche a matriz
    for (int i = 0; i < T; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        grafo[x][y] = 1;
        grafo[y][x] = 1; // bidirecional
    }

    int P;
    scanf("%d", &P);
    int possiveis = 0;

    for (int i = 0; i < P; i++) {
        int N;
        scanf("%d", &N);

        int passeio[N];
        for (int j = 0; j < N; j++) {
            scanf("%d", &passeio[j]);
        }

        int valido = 1;
        for (int j = 0; j < N - 1; j++) {
            int atual = passeio[j];
            int proximo = passeio[j + 1];
            if (!grafo[atual][proximo]) {
                valido = 0;
                break;
            }
        }

        if (valido) {
            possiveis++;
        }
    }

    printf("%d\n", possiveis);
    return 0;
}
