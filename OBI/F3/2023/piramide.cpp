// g++ -o piramide piramide.cpp
// ./piramide

// g++ -g piramide.cpp -o piramide.exe

#include <bits/stdc++.h>
using namespace std;

int main(void) {
    std::string linha;
    std::vector<int> v;
    int numero;

    // 1. Lê a linha toda
    std::getline(std::cin, linha);

    // 2. Transforma a linha em um stream
    std::stringstream ss(linha);

    // 3. Extrai os números um por um até o fim da linha
    while (ss >> numero) {
        v.push_back(numero);
    }

    if (v.size() == 1) {
        cout << "S" << '\n';
    }
    else if (v.size() == 3) {
        sort(v.begin(), v.end());

        if (v[0] + v[1] == v[2]) {
            cout << "S" << '\n';
        }
        else {
            cout << "N" << '\n';
        }
    }
    else if (v.size() == 5) {
        sort(v.begin(), v.end());

        if (v[0] + v[1] + v[2] + v[3] == v[4]) {
            cout << "S" << '\n';
        }
        else {
            cout << "N" << '\n';
        }
    }
    else if (v.size() == 6) {
        sort(v.begin(), v.end());
        int topo = v[5];
        v.erase(v.begin() + 5);

        bool possivel = false;

        for (int i = 0; i < 4; i++) {
            for (int j = i + 1; j < 5; j++) {
                if (v[i] + v[j] == topo) {
                    v.erase(v.begin() + i);
                    v.erase(v.begin() + j - 1);
                    possivel = true;
                    break;
                }
            }
            if (possivel) break;
        }

        int soma = v[0] + v[1] + v[2];
        if (soma == topo) {
            cout << "S" << '\n';
        }
        else {
            cout << "N" << '\n';
        }
    }
    else {
        cout << "N" << '\n';
    }
}
