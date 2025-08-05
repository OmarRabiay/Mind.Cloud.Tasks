#include <iostream>

using namespace std;

int main() {
    int k2, k3, k5, k6;
    cin >> k2 >> k3 >> k5 >> k6;
    int total = 0;
    int n256 = min(k2, min(k5, k6));
    k2 = k2 - n256;
    int n32 = min(k3, k2);
    total = n256 * 256 + n32 * 32;
    cout << total << endl;
    return 0;
}