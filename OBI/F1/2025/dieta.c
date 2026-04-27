#include <stdio.h>

int main(void)
{
    int n, m, soma = 0;
    scanf("%d %d", &n, &m);
    int p[n], g[n], c[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d %d %d", &p[i], &g[i], &c[i]);
        p[i] = p[i] * 4;
        g[i] = g[i] * 9;
        c[i] = c[i] * 4;
    }

    for (int i = 0; i < n; i++)
    {
        soma += p[i] + g[i] + c[i];
    }

    int x = m - soma;
    if (m < soma)
    {
        printf("0\n");
    }
    printf("%d\n", x);
    return 0;
}
