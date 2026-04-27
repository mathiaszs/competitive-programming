#include <stdio.h>

int main(void)
{
    int m, n, p, c = 0;

    scanf("%d %d", &m, &n);
    int mn[m][n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d ", &mn[i][j]);
        }
    }

    scanf("%d", &p);
    int I, J;
    for (int h = 0; h < p; h++)
    {
        scanf("%d %d", &I, &J);
        if (mn[I - 1][J - 1] > 0)
        {
            mn[I - 1][J - 1] -= 1;
            c++;
        }
    }

    printf("%d\n", c);
    return 0;
}
