#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    n = (n - 5) % 8;
    printf("%d\n", n);
}
