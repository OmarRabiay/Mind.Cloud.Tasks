#include <iostream>

using namespace std;

int main() {
    float n;
    cin >> n;
    float p;
    float sum = 0;

    for (int i = 0; i < n; i++){
        cin >> p;
        sum+= p;
    }
    double average = sum / n;
    cout << average << endl;
    return 0;
}