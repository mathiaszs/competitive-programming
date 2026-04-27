#include <stdio.h>
#include <unistd.h>

int main(void)
{
    int s = 2;

    while (1)
    {
        printf("%02d\n", s);

        sleep(1);  // Espera 1 segundo
        s = s * s;
    }
    return 0;
}
