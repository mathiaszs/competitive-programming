#include <stdio.h>

int main(void)
{
    int n = 0, k = 0, C = 0;

    scanf("%d %d", &n, &k);
    int notas[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &notas[i]);
    }

    for (int i = 0; i < n - 1; i++)
    {
        int max_idx = i;
        for (int j = i + 1; j < n; j++)
        {
            if (notas[j] > notas[max_idx])
            {
                max_idx = j;
            }
        }
        // Troca
        int temp = notas[i];
        notas[i] = notas[max_idx];
        notas[max_idx] = temp;
    }

    // O k-ésimo maior número
    int C = notas[k - 1];

    printf("%i\n", C);

    return 0;
}
