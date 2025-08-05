#include <iostream>

using namespace std;

int main() {
    int s, t, a, b, m, n, location;
    cin >> s >> t >> a >> b >> m >> n;
    int apple[m], orange[n];
    int apples = 0, oranges = 0;
    for (int i = 0; i < m; i++) {
        cin >> apple[i];
        location = a + apple[i];
        if (location >= s && location <= t) {
            apples++;
        }
    }
    for (int i = 0; i < n; i++) {
        cin >> orange[i];
        location = b + orange[i];
        if (location >= s && location <= t) {   
            oranges++;
        }
    }
    cout << apples << endl;
    cout << oranges << endl;
    return 0;
}