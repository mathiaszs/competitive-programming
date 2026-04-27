#include <stdio.h>

int main(void)
{
    int n, f, array[9][9], copy[9][9];
    scanf("%d %d", &n, &f);

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            scanf("%d", &array[i][j]);
        }
    }

    if (f > array[0][0])
    {
        copy[0][0] = f;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    if (copy[i][j] >= array[x][y])
                    {
                        copy[x][y] = f;
                    }
                }
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (copy[i][j] == f)
            {
                printf("*");
            }
            if (copy[i][j] != f)
            {
                printf("%d", array[i][j]);
            }
        }
        printf("\n");
    }
    return 0;
}

// O(8)
