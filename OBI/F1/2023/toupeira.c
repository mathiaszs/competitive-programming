#include <stdio.h>

int main(void)
{
    int s, t, p, a = 0;
    int counter = 0;
    scanf("%d %d", &s, &t);
    int x, y, n;
    int array[20][20];

    // Receber as ligações
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d", &x, &y);
        array[x][y] = 1;
    }

    // Receber a trajetória
    scanf("%d", &p);
    int c[100][100];
    for (int i = 0; i < p; i++)
    {
        scanf("%d ", &n);
        for (int j = 0; j < n; j++)
        {
            int h = j + 1;
            c[j][h] = scanf("%d %d ", &j, &h);
        }
    }

    // Verificar se a trajetória é possível
    // c[j] + c[j+1] precisa ser valer em array[j][j+1]
    for (int i = 0; i < n; i++)
    {
        if (c[i][i + 1] == array[i][i + 1])
        {
            counter++;
        }
        if (counter == n)
        {
            a++;
        }
    }

    printf("%d", a);
    return 0;
}
