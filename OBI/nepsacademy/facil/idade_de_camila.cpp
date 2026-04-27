#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int A, B, C;
    cin >> A;
    cin >> B;
    cin >> C;

    std::vector v = {A, B, C};

    std::sort(v.begin(), v.end());

    cout << v[1] << "\n";

}

