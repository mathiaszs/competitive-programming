#include <stdio.h>

int main(void)
{
    int n, q, counter = 0;
    scanf("%d %d", &n, &q);

    int array[n][n];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &array[i][j]);

            for (int m = -1; m < 2; m++)
            {
                for (int f = -1; f < 2; f++)
                {
                    if (array[m][f] == 1)
                    {
                        counter++;
                    }
                }
            }
            if (array[i][j] == 0)
            {
                if (counter == 3)
                {
                    array[i][j] = 1;
                }
            }
            if (array[i][j] == 1)
            {
                if (counter == 2 || counter == 3)
                {
                    array[i][j] = 1;
                }
                else
                {
                    array[i][j] = 0;
                }
            }
        }
    }
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < q; j++)
        {
            printf("%p\n", (void *)&array[i][j]);
        }
    }
    return 0;
}
