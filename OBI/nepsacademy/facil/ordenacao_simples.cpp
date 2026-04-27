// g++ -o ordenacao_simples ordenacao_simples.cpp
// ./ordenacao_simples

#include <bits/stdc++.h>
using namespace std;

int main(void) {
    std::vector<int> v(10);

    for (int i = 0; i < 10; i++) {
        cin >> v[i];
    }

    std::sort(v.begin(), v.end());

    for (int x : v) {
        std::cout << x << " ";
    }
    std::cout << "\n";

    std::sort(v.rbegin(), v.rend());

    for (int x : v) {
        std::cout << x << " ";
    }
    std::cout << "\n";
    return 0;
}
