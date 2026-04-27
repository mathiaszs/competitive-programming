#include <stdio.h>

int main(void)
{
    int a, b, c, d, leite, x = 0;
    scanf("%d", &a);    
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &d);

    for (int i = 1; i < 500; i++)
    {
        if (d * i <= (c - a) && d * i >= (c - b))
        {
            x = i;
        }
    }

    if (x == 0)
    {
        printf("N\n");
        return 0;
    }
    leite = c - (d * x);
        if (leite >= a && leite <= b)
        {
            printf("S\n");
            return 0;
        }
        printf("N\n");
        return 0;
}
