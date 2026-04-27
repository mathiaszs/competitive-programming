#include <stdio.h>

int main(void)
{
    int e, s, l, soma;
    int maior, menor, segundo;
    int x1, x2, x3;
    int p[4];
    scanf("%d", &p[0]);
    scanf("%d", &p[1]);
    scanf("%d", &p[2]);
    p[3] = p[0];
    maior = p[0];
    menor = p[0];
    segundo = p[0];

    for (int i = 1; i < 4; i++)
    {
        if (p[i] > p[i - 1])
        {
            maior = p[i];
        }
        if (p[i] < p[i - 1])
        {
            menor = p[i];
        }
    }

    for (int i = 1; i < 4; i++)
    {
        if (p[i] != maior && p[i] != menor)
        {
            segundo = p[i];
        }
    }

    x1 = maior - segundo;
    x2 = segundo - menor;
    x3 = maior - menor;

    soma = x1 + x2 + x3;

    printf("%d\n", soma);
}

