#include <iostream>
using namespace std;

int main() {
    const int tamanho = 10;
    int vetor[tamanho];

    cout << "Digite os valores do vetor de 10 posicoes:\n";
    for (int i = 0; i < tamanho; i++) {
        cout << "Posicao " << i + 1 << ": ";
        cin >> vetor[i];
    }

    int maior = vetor[0];
    int menor = vetor[0];
    for (int i = 1; i < tamanho; i++) {
        if (vetor[i] > maior) {
            maior = vetor[i];
        }
        if (vetor[i] < menor) {
            menor = vetor[i];
        }
    }

    cout << "\nO maior elemento do vetor: " << maior << endl;
    cout << "O menor elemento do vetor: " << menor << endl;

    return 0;
}