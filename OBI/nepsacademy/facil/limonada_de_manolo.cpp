#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int N, C;
    cin >> N >> C;

    int soma = 0;
    for (int i = 0; i < N; i++) {
        int num = C - i;
        if (num < 1) num = 1;
        soma += num;
    }

    cout << soma << '\n';
}
