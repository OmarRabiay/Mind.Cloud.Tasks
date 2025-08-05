#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int p[100000];
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        p[i] = x / 2;
    }
    for (int i = 0; i < n; i++) {
        cout << p[i] << endl;
    }
}