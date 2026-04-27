#include <stdio.h>

int main(void)
{
    int v;
    int afp[4];
    int menor = 0, maior = 0, counter = 0, segundo = 0;

    // Receber Variáveis
    scanf("%d", &v);
    scanf("%d", &afp[0]);
    scanf("%d", &afp[1]);
    scanf("%d", &afp[2]);
    afp[3] = afp[0];

    // Menor, maior e segundo
    for (int i = 0; i < 3; i++)
    {
        if (afp[i] < afp[i - 1])
        {
            menor = afp[i];
        }
        if (afp[i] > afp[i - 1])
        {
            maior = afp[i];
        }
    }
    
    for (int i = 0; i < 3; i++)
    {
        if (afp[i] != menor && afp[i] != maior)
        {
            segundo = afp[i];
        }
    }

    // Se V paga a menor, atualizamos o valor de V
    if (v >= menor)
    {
        v = v - menor;
        counter++;
    }

    if (v >= segundo)
    {
        v = v - segundo;
        counter++;
    }

    if (v >= maior)
    {
        v = v - maior;
        counter++;
    }

    printf("%d\n", counter);
    return 0;
}
