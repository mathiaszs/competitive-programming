#include <stdio.h>

int main(void)
{
    char a[7], b[7];
    int p[7];

    for (int i = 0; i < 7; i++)
    {
        scanf(" %c%c", &a[i], &b[i]);
    }

    for (int i = 1; i < 7; i++)
    {
        if (b[i] == b[0])   // Naipe dominante
        {
            if (a[i] == 'A')
            {
                p[i] = 14;
            }
            if (a[i] == 'J')
            {
                p[i] = 15;
            }
            if (a[i] == 'Q')
            {
                p[i] = 16;
            }
            if (a[i] == 'K')
            {
                p[i] = 17;
            }
        }

        if (b[i] != b[0])   // Naipe N dominante
        {
            if (a[i] == 'A')
            {
                p[i] = 10;
            }
            if (a[i] == 'J')
            {
                p[i] = 11;
            }
            if (a[i] == 'Q')
            {
                p[i] = 12;
            }
            if (a[i] == 'K')
            {
                p[i] = 13;
            }
        }
    }

    int p1 = p[1] + p[2] + p[3];
    int p2 = p[4] + p[5] + p[6];

    if (p1 > p2)
    {
        printf("Luana\n");
    }
    if (p2 > p1)
    {
        printf("Edu\n");
    }
    if (p1 == p2)
    {
        printf("empate\n");
    }

    return 0;
}
