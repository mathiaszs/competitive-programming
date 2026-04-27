#include <stdio.h>

int main(void)
{
    int n;
    int s1 = 0, s2 = 0;
    scanf("%d", &n);
    int t[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &t[i]);
        if (t[i] == 1)
        {
            s1++;
        }
        if (t[i] == 2)
        {
            s2++;
        }
    }
    int p, m;
    scanf("%d", &p);
    scanf("%d", &m);

    if (p >= s1 && m >= s2)
    {
        printf("S\n");
        return 0;
    }

    printf("N\n");
    return 0;
}
