// g++ -o teleferico teleferico.cpp
// ./teleferico

//  g++ -g 10388.cpp -o 10388.exe

#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int C, A;
    cin >> C;
    cin >> A;

    int res;

    if (A % (C - 1) == 0) {
        res = A / (C - 1);
    }
    else {
        res = A / (C - 1) + 1;
    }

    cout << res << '\n';
    return 0;
}
