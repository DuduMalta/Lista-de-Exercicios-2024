#include <iostream>
using namespace std;

int main() {
    int a, b;
    
    cout << "Digite dois números positivos menores que 10000:\n";
    cin >> a >> b;
    
    int vetorA[4] = {0};
    int vetorB[4] = {0};
    
    for (int i = 0; a > 0; i++) {
        vetorA[i] = a % 10;
        a /= 10;
    }
    for (int i = 0; b > 0; i++) {
        vetorB[i] = b % 10;
        b /= 10;
    }
    
    int soma[5] = {0};
    
    for (int i = 0; i < 4; i++) {
        soma[i] += vetorA[i] + vetorB[i];
        if (soma[i] >= 10) {
            soma[i] -= 10;
            soma[i + 1] += 1;
        }
    }
    
    cout << "A soma de a e b é: ";
    bool startPrinting = false; 
    for (int i = 4; i >= 0; i--) {
        if (soma[i] != 0) {
            startPrinting = true;
        }
        if (startPrinting) {
            cout << soma[i];
        }
    }
    if (!startPrinting) {
        cout << 0;
    }
    cout << endl;
    
    return 0;