#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n = 0;

    // Struct definition
    struct person
    {
        char pessoa[11];
        int lance;
    };
    struct person maior;

    // Getting variables
    struct person one[10000];

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%s", one[i].pessoa);
        scanf("%d", &one[i].lance);
    }

    // Comparing values
    maior = one[0];
    for (int i = 1; i < n; i++)
    {
        if(one[i].lance > maior.lance)
        {
            maior = one[i];
        }
    }

    printf("%s\n", maior.pessoa);
    printf("%d\n", maior.lance);

    return 0;
}
