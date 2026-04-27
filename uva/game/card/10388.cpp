/*
g++ -o 10388 10388.cpp
./10388
g++ -g 10388.cpp -o 10388.exe

verdict: ACCEPTED!! (first)
*/

#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        if (i > 0) cout << '\n';
        std::string JA;
        std::string JO;
        cin >> JA;
        cin >> JO;

        bool possivel = false;

        std::vector<std::string> textos;

        std::vector<char> jane_down(JA.begin(), JA.end());
        std::vector<char> jane_up;
        std::vector<char> john_down(JO.begin(), JO.end());
        std::vector<char> john_up;

        // What if one element is different? No solution
        /* for (int a = 0; a < JA.size(); a++) {
            if (a + 1 < JA.size()) {
                int count = 0;
                for (int b = a + 1; b < JA.size(); b++) {
                    if (jane_down[a] != jown_down[b]) {
                        count += 1
                    }
                }

            }
        } */

        for (int j = 0; j < 500; j++) {
            // Se a lista não estiver vazia
            if (!jane_down.empty() && !john_down.empty()) {
                char A = jane_down[0];
                char B = john_down[0];
                jane_down.erase(jane_down.begin());
                john_down.erase(john_down.begin());

                jane_up.insert(jane_up.begin(), A);
                john_up.insert(john_up.begin(), B);

                if (A == B) {
                    // SNAP!!
                    if (random()/141%2 == 0) {
                        // Jane toma o up de John
                        // Insere v2 no final de v1
                        jane_up.insert(jane_up.begin(), john_up.begin(), john_up.end());
                        john_up.clear();

                        string s(jane_up.begin(), jane_up.end());
                        textos.push_back("Snap! for Jane: " + s);
                    }
                    else {
                        john_up.insert(john_up.begin(), jane_up.begin(), jane_up.end());
                        jane_up.clear();

                        string s(john_up.begin(), john_up.end());
                        textos.push_back("Snap! for John: " + s);
                    }
                }

                // Se depois disso nn tiver sobrado nada pra um, é o fim

                if (jane_up.empty() && jane_down.empty()) {
                    for (const auto& t : textos) {
                        cout << t << '\n';
                    }
                    cout << "John wins." << '\n';
                    possivel = true;
                    break;
                }
                if (john_up.empty() && john_down.empty()) {
                    for (const auto& t : textos) {
                        cout << t << '\n';
                    }
                    cout << "Jane wins." << '\n';
                    possivel = true;
                    break;
                }

            }
            // Se o vector estiver vazio -> Virar o vector ao contrário
            if (jane_down.empty()) {
                std::reverse(jane_up.begin(), jane_up.end());
                jane_down = jane_up;
                jane_up.clear();
            }
            if (john_down.empty()) {
                std::reverse(john_up.begin(), john_up.end());
                john_down = john_up;
                john_up.clear();
            }
        }

        if (!possivel) {
            cout << "Keeps going and going ..." << '\n';
        }

    }

    return 0;
}
