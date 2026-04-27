#include <stdio.h>

int main(void)
{
    int n, H;
    scanf("%d", &n);
    int x[n];
    H = x[0];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &x[i]);
        if (i > 0)
        {
            if (x[i] > H)
            {
                H = x[i];
            }
        }
    }

    int barras[H][n];

    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < n; j++)
        {
            barras[i][j] = 2;
        }
    }

    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            if (H - x[i] - j - 1 >= 0)
            {
                barras[H - x[i] - j - 1][i] = 0;
            }
        }
    }

    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (barras[i][j] != 0)
            {
                barras[i][j] = 1;
            }
            printf("%d", barras[i][j]);
        }
        printf("\n");
    }
    return 0;
}
