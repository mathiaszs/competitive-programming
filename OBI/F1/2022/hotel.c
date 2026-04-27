#include <stdio.h>

int main(void)
{
    int d, a, n, p;
    scanf("%d", &d);    // dia 1
    scanf("%d", &a);    // aumento por dia
    scanf("%d", &n);    // dia de chegada

    // Calculo
    int x = 32 - n;
    p = x * (d + (n - 1) * a);

    if (n > 15)
    {
        p = (32 - 16) * (d + 14 * a);
    }

    printf("%d\n", p);
    return 0;
}
