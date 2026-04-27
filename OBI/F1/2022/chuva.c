#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n, s, c = 0;
    scanf("%d", &n);
    scanf("%d", &s);
    int x[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &x[i]);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j  = 0; j < n; j++)
        {
            if (i != j)
            {
                if (abs(x[i] - x[j]) == s)
                {
                    c++;
                }
            }
        }
    }

    printf("%d\n", c);
}
