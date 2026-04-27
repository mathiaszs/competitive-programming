// g++ -o tempo_de_viagem_em_segundos tempo_de_viagem_em_segundos.cpp
// ./tempo_de_viagem_em_segundos.exe

//  g++ -g tempo_de_viagem_em_segundos.cpp -o tempo_de_viagem_em_segundos.exe

#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int D1, H1, M1, D2, H2, M2;

    cin >> D1;
    cin >> H1;
    cin >> M1;
    cin >> D2;
    cin >> H2;
    cin >> M2;

    int dias = (D2 - D1) * 86400;
    int horas = (H2 - H1) * 3600;
    int minutos = (M2 - M1) * 60;

    int total = dias + horas + minutos;

    std::cout << total << '\n';
}
