#include <stdio.h>

int main(void)
{
    int E, D, x;
    scanf("%d", &E);
    scanf("%d", &D);

    // Restrições
    if (E > 5 || D > 5 || E < 0 || D < 0 || E == D)
    {
        return 1;
    }

    if (E > D)
    {
        x = E + D;
    }

    if (E < D)
    {
        x = 2 * (D - E);
    }

    printf("%d\n", x);
    return 0;
}
