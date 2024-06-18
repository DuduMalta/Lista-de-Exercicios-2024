#include <iostream>
using namespace std;

int main() {
    const int tamanho = 6;
    int vetor[tamanho];

    cout << "Digite 6 numeros inteiros:\n";
    for (int i = 0; i < tamanho; i++) {
        cout << "Valor " << i + 1 << ": ";
        cin >> vetor[i];
    }

    cout << "\nValores lidos na ordem inversa:\n";
    for (int i = tamanho - 1; i >= 0; i--) {
        cout << vetor[i] << " ";
    }
    cout << endl;

    return 0;
}
