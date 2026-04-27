#include <stdio.h>

int soma(int x)
{
    int soma = 0;
    while (x > 0)
    {
        soma += x % 10;
        x /= 10;
    }
    return soma;
}
int main(void)
{
    int n, m, s, r = -1;
    scanf("%d", &n);
    scanf("%d", &m);
    scanf("%d", &s);

    for (int i = m; i >= n; i--)
    {
        if (soma(i) == s)
        {
            printf("%d\n", i);
            return 0;
        }
    }

    printf("-1\n");
    return 0;
}
