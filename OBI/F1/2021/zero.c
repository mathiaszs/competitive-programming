#include <stdio.h>

int main(void)
{
    int N, x, topo = 0, pilha[100000];
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &x);
        if (x != 0) {
            pilha[topo++] = x; // empilha
        } else if (topo > 0) {
            topo--; // desempilha o último número
        }
    }

    int soma = 0;
    for (int i = 0; i < topo; i++) {
        soma += pilha[i];
    }

    printf("%d\n", soma);
    return 0;
}
