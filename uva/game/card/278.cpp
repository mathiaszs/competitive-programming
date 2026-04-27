/* UVa 278 - Chess
g++ -o 278 278.cpp
./278
g++ -g 278.cpp -o 278.exe

verdict: None
*/

#include <bits/stdc++.h>
using namespace std;

// Yes
int rook(int m, int n) {
    int maximo = min(m, n);
    return maximo;
}

// ?
int knight(int m, int n) {
    float maximo;

    if (m % 2 != 0) {
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                maximo += static_cast<int>(m / 2) + 1;
            }
            else {
                maximo += m / 2;
            }
        }
    }
    else maximo = (m / 2) * n;

    return maximo;
}

// Not sure
int queen(int m, int n) {
    int maximo = min(m, n);
    return maximo;
}

// Sure
int king(int m, int n) {
    int maximo;
    if (m % 2 == 0 && n % 2 == 0) {
        maximo = (m / 2) * (n / 2);
    }
    if (m % 2 == 0 && n % 2 != 0) {
        n = static_cast<int>(n / 2) + 1;
        m /= 2;
        maximo = m * n;
    }
    if (m % 2 != 0 && n % 2 == 0) {
        m = static_cast<int>(m / 2) + 1;
        n /= 2;
        maximo = m * n;
    }
    if (m % 2 != 0 && n % 2 != 0) {
        n = static_cast<int>(n / 2) + 1;
        m = static_cast<int>(m / 2) + 1;
        maximo = m * n;
    }
    return maximo;
}

int main(void) {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        // Input
        char c;
        int m, n;
        cin >> c >> m >> n;

        int quantity;

        if (c == 'r') quantity = rook(m, n);
        if (c == 'k') quantity = knight(m, n);
        if (c == 'Q') quantity = queen(m, n);
        if (c == 'K') quantity = king(m, n);

        cout << quantity << '\n';
    }
    cout << '\n';
    return 0;
}
