#include <stdio.h>

int main(void)
{
    int n, m, I[500], r;
    scanf("%d %d", &n, &m);
    scanf("%d %d", &I[0], &r); //amigo que foi infectado e o número da primeira reunião em que ele participou infectado
    int a[n];   // Number of people in class
    int p[m][n];   //
    int counter = 0;

    for (int i = 1; i < m; i++)
    {
        scanf("%d", &a[i]);
        for (int j = 0; j < a[i]; j++)
        {
            scanf("%d", &p[i][j]);
        }
    }

    for (int i = r; i < m; i++)
    {
        for (int j = 0; j < a; j++)
        {
            if (I[0] == p[i][j])
            {
                for (int h = 1; h < a; h++)
                {
                    if (p[i][h] != I[0])
                    {
                        p[i][h] = I[h];
                    }
                }
            }
            if (I[j] == p[i][j])
            {
                for (int h = 1; h < a; h++)
                {
                    if (p[i][h] != I[0])
                    {
                        p[i][h] = I[h];
                    }
                }
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (p[i] == I[j])
            {
                counter++;
            }
        }
    }

    printf("%d", counter);
    return 0;
}
