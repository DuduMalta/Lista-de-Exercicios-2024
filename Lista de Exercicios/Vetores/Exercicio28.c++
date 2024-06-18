#include <iostream>
using namespace std;

int main() {
    const int tamanho = 10;
    int v[tamanho];
    int v1[tamanho], v2[tamanho];
    int contador_v1 = 0, contador_v2 = 0;

    cout << "Digite 10 números inteiros:\n";
    for (int i = 0; i < tamanho; i++) {
        cout << "Número " << i + 1 << ": ";
        cin >> v[i];
    }

    for (int i = 0; i < tamanho; i++) {
        if (v[i] % 2 != 0) { // Ímpar
            v1[contador_v1++] = v[i];
        } else { // Par
            v2[contador_v2++] = v[i];
        }
    }

    cout << "\nElementos UTILIZADOS de v1 (ímpares):\n";
    for (int i = 0; i < contador_v1; i++) {
        cout << v1[i] << " ";
    }
    cout << endl;

    cout << "\nElementos UTILIZADOS de v2 (pares):\n";
    for (int i = 0; i < contador_v2; i++) {
        cout << v2[i] << " ";
    }
    cout << endl;

    return 0;
}