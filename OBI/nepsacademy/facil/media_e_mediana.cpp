// g++ -o media_e_mediana media_e_mediana.cpp
// media_e_mediana media_e_mediana.cpp

#include <bits/stdc++.h>
using namespace std;

int main(void) {
    // (A + B + C) / 3 == B
    int B, C;
    cin >> B;
    cin >> C;

    int diff = C - B;
    cout << B - diff << "\n";
}

