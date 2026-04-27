#include <stdio.h>

int main(void)
{
    // Limites para variáveis
    int h, m, s, T, SEC;

    scanf("%d%d%d%d", &h, &m, &s, &T);

    // Soma os segundos
    s += T;

    // Ajuste dos minutos e horas
    m += s / 60;  // Cada 60 segundos vira 1 minuto
    s = s % 60;   // Resto fica nos segundos

    h += m / 60;  // Cada 60 minutos vira 1 hora
    m = m % 60;   // Resto fica nos minutos

    h = h % 24;   // Ajuste para manter dentro de 24 horas

    printf("%d\n", h);
    printf("%d\n", m);
    printf("%d\n", s);
}
