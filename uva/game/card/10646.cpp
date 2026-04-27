/* https://onlinejudge.org/external/106/10646.pdf
g++ -o 10646 10646.cpp
./10646
g++ -g 10646.cpp -o 10646.exe

verdict: Wrong Answer
*/

#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int N;
    cin >> N;

    vector<vector<string>> cartas(N, vector<string>(52));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 52; j++) {
            cin >> cartas[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        // Pegar os últimos 25 elementos e tirar da lista original
        vector<string> sub(cartas[i].begin() + 26, cartas[i].end());
        cartas[i].erase(cartas[i]begin() + 26, cartas[i].end());

        // Algorithm
        Y = 0;

        for (c = 0; c < 3; c++) {
            // Value of sub[0]
            int X;
            if (isdigit(sub[0][0]) && sub[0][0] != 0 && sub[0][0] != 0) {
                X = sub[0][0];
            }
            else {
                X = 10;
            }

            Y += X
            away = 10 - X
            // Tirar a carta e as próximas away

        }
    }
}


/* A WRONG IMPLEMENTATION
for (int n = 0; n < N; n++) {

        vector<std::string> hand(25);
        int c = 0;
        for (int a = 27; a < 52; a++) {
            hand[c] = numeros[n][a];
            numeros[n].erase(numeros[n].begin() + a);
            c += 1;
        }

        int Y = 0;
        for (int i = 0; i < 3; i++) {

            // Take the top card of the cards of the pile and determine its value.
            // Let the card value be X. Add X to Y.

            int X;
            if (isdigit(hand[0][0])) {
                X = hand[0][0] - '0';
            }
            else {
                X = 10;
            }

            Y += X;

            // Put this card and the top (10 − X) cards of the pile away

            moveTopToPosition(hand, 10 - X);

            numeros[n].insert(numeros[n].end(), hand.begin(), hand.end());
            cout << "Y =" << Y << "\n";
            cout << "Case " << n << ": " << numeros[n][52 - Y] << "\n";

        }
    }
*/
