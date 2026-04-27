#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char alfabeto[26] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z' };
    char p[30];
    scanf("%s", p);
    int a[6] = { 'a', 'e', 'i', 'o', 'u', 'a' };

    for (int i = 0; i < strlen(p); i++)
    {
        int x;
        if (p[i] != 'a' && p[i] != 'e' && p[i] != 'i' && p[i] != 'o' && p[i] != 'u')    // Se for consoante
        {
            // p[i] é qual letra no alfabeto?
            for (int j = 0; j < 26; j++)
            {
                if (p[i] == alfabeto[j])
                {
                    x = j;  // p[i] é a xº letra do alfabeto
                }
            }

            // Imprimir a primeira letra
            printf("%c", p[i]);

            // Segunda letra
            int y[6];
            int menor_dist = 999;
            int menor = 0;

            for (int k = 0; k < 6; k++)
            {
                int dist = abs(x - a[k]); // usando valor ASCII

                if (dist < menor_dist) {
                    menor_dist = dist;
                    menor = k;
                }
            }
            printf("%c", a[menor]);

            // Terceira letra
            int counter = 0;
            for (int oi = 0; oi < 6; oi++)
            {
                if (a[oi] == alfabeto[x + 1])
                {
                    counter++;
                }
            }
            if (counter > 0)
            {
                printf("%c", alfabeto[x + 2]);
            }
            if (counter == 0)
            {
                printf("%c", alfabeto[x + 1]);
            }
        }

        if (p[i] == 'a' && p[i] == 'e' && p[i] == 'i' && p[i] == 'o' && p[i] == 'u')
        {
            printf("%c", p[i]);
        }
    }

    printf("\n");
    return 0;
}
