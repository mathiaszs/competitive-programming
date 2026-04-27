#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> casas(N);

    for (int i = 0; i < N; i++) {
        cin >> casas[i];
    }

    int K;
    cin >> K;

    int left = 0;
    int right = N - 1;

    while (true) {
        int soma = casas[left] + casas[right];
        if (soma == K) {
            cout << casas[left] << " ";
            cout << casas[right] << "\n";
            break;
        }
        if (soma < K) {
            left++;
        }
        if (soma > K) {
            right--;
        }
    }

    return 0;
}
