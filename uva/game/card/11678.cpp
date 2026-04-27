/* UVa 11678 - 
g++ -o 11678 11678.cpp
./11678
g++ -g 11678.cpp -o 11678.exe

verdict: Time Limit
*/

#include <bits/stdc++.h>
using namespace std;

int main(void) {

    while (true) {
        int A, B;
        cin >> A >> B;

        if (A == 0 && B == 0) break;

        vector<int> alice(A);
        for (int i = 0; i < A; i++) {
            cin >> alice[i];
        }
        vector<int> betty(B);
        for (int i = 0; i < B; i++) {
            cin >> betty[i];
        }

        int onlyAlice = 0;
        int onlyBetty = 0;
        int p1 = 0;
        int p2 = 0;

        while (true) {
            // Deixando os vetores únicos
            alice.erase(unique(alice.begin(), alice.end()), alice.end());
            betty.erase(unique(betty.begin(), betty.end()), betty.end());

            if (alice[p1] < betty[p2]) {
                if (p2 >= 1) {
                    if (alice[p1] != betty[p2 - 1]) onlyAlice++;
                }
                else {
                    if (alice[p1] != betty[p2]) onlyAlice++;
                }
                if (p1 < A - 1) p1++;
            }

            if (betty[p2] < alice[p1]) {
                if (p1 >= 1) {
                    if (betty[p2] != alice[p1 - 1]) onlyBetty++;
                }
                else {
                    if (betty[p2] != alice[p1]) onlyBetty++;
                }

                if (p2 < B - 1) p2++;
            }

            if (betty[p2] == alice[p1]) {
                p1++;
                p2++;
            }

            if (p1 == A - 1 && p2 == B - 1) {
                cout << min(onlyAlice, onlyBetty) << '\n';
                break;
            }
        }
    }
}



/*   SOLUÇÃO INCORRETA
if (alice[p1] >= betty[p2]) {
                if (p1 >= 1 and p2 >= 1) {
                    if (betty[p2] != betty[p2 - 1] && betty[p2] != alice[p1 - 1] && betty[p2] != alice[p1]) {
                        last += 1;
                    }
                }
                else {
                    if (betty[p2] != alice[p1]) {
                        last += 1;
                    }
                }

                if (p2 + 1 != B) {
                    p2 += 1;
                }
            }

            else {
                if (p1 >= 1 && p2 >= 2) {
                    if (alice[p1] != alice[p1 - 1] && alice[p1] != betty[p2 - 1] && betty[p2] != alice[p1]) { // a primeira condição
                        first += 1;
                    }
                }
                else {
                    if (betty[p2] != alice[p1]) {
                        first += 1;
                    }
                }

                if (p1 + 1 != A) {
                    p1 += 1;
                }
            }

            if (p1 == A - 1 && p2 == B - 1) {
                break;
            }

        }*/
