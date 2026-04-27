#include <stdio.h>

int main(void)
{
    int n, soma = 0;
    scanf("%d", &n);
    int p[n], g[n][3];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &p[i]);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            for (int h = 0; h < 3; h++)
            {
                if (p[i] >= p[j])
                {
                    g[i][h] = p[i];
                }
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        soma += g[i][0] + g[i][1];
    }

    printf("%d\n", soma);
    return 0;
}
