#include <stdio.h>

int main(void)
{
    int n, c = 1;
    scanf("%d", &n);
    int x[n], y[n];
    x[0] = 0;
    y[0] = 0;

    for (int i = 1; i < n; i++)
    {
        scanf("%d %d", &x[i], &y[i]);
    }

    for (int i = 0; i < n - 2; i++)
    {
        if (x[i] - x[i - 1] + y[i] - y[i - 1] > x[i - 1] - x[i - 2] + y[i - 1] - y[i - 2])
        {
            c++;
        }
    }

    printf("%d\n", c);
    return 0;
}
