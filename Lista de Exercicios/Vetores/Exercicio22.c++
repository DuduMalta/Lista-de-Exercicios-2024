#include <iostream>
using namespace std;

int main() {
    const int tamanho = 10;
    int vetorA[tamanho], vetorB[tamanho], vetorC[2 * tamanho];

    cout << "Digite os 10 valores inteiros para o vetor A:\n";
    for (int i = 0; i < tamanho; i++) {
        cout << "A[" << i << "]: ";
        cin >> vetorA[i];
    }

    cout << "\nDigite os 10 valores inteiros para o vetor B:\n";
    for (int i = 0; i < tamanho; i++) {
        cout << "B[" << i << "]: ";
        cin >> vetorB[i];
    }

    cout << "\nCriando o vetor C com valores intercalados...\n";
    for (int i = 0; i < tamanho; i++) {
        vetorC[2 * i] = vetorA[i]; // Posições pares
        vetorC[2 * i + 1] = vetorB[i]; // Posições ímpares
    }

    cout << "\nValores do vetor C:\n";
    for (int i = 0; i < 2 * tamanho; i++) {
        cout << "C[" << i << "]: " << vetorC[i] << endl;
    }

    return 0;
}