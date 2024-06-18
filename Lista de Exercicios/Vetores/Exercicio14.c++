#include <iostream>
using namespace std;

int main() {
    const int tamanho = 10;
    int vetor[tamanho];

    cout << "Digite 10 valores:\n";
    for (int i = 0; i < tamanho; i++) {
        cout << "Valor " << i + 1 << ": ";
        cin >> vetor[i];
    }

    bool existem_iguais = false;
    cout << "\nValores iguais:\n";
    for (int i = 0; i < tamanho; i++) {
        for (int j = i + 1; j < tamanho; j++) {
            if (vetor[i] == vetor[j]) {
                cout << vetor[i] << endl;
                existem_iguais = true;
                break;
            }
        }
    }

    if (!existem_iguais) {
        cout << "Nenhum valor igual encontrado.\n";
    }

    return 0;
}
