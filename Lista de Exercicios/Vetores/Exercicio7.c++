#include <iostream>
using namespace std;

int main() {
    const int tamanho = 10;
    int vetor[tamanho];

    cout << "Digite 10 numeros inteiros:\n";
    for (int i = 0; i < tamanho; i++) {
        cout << "Numero " << i + 1 << ": ";
        cin >> vetor[i];
    }

    cout << "\nVetor: ";
    for (int i = 0; i < tamanho; i++) {
        cout << vetor[i] << " ";
    }
    cout << endl;

    int maior = vetor[0];
    int posicao_maior = 0;
    for (int i = 1; i < tamanho; i++) {
        if (vetor[i] > maior) {
            maior = vetor[i];
            posicao_maior = i;
        }
    }

    cout << "O maior elemento do vetor: " << maior << endl;
    cout << "Posicao do maior elemento: " << posicao_maior << endl;

    return 0;
}
