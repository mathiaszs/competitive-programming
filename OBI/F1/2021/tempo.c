#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int x[n];
    char c[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%c%d", &c[i], &x[i]);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (x[i] == x[j] && c[i] == 'R' && c[j] == 'E')
            {
                int tempo = 0;
                for (int h = i; h < j; h++)
                {
                    if (c[h] == 'T')
                    {
                        tempo += x[h];
                    }
                    if (c[h] != 'T')
                    {
                        tempo++;
                    }
                }
                printf("%c %d\n", c[i], tempo);
            }
        }
    }


    return 0;
}
