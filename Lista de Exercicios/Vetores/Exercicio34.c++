#include <iostream>
using namespace std;

int main() {
    const int tamanho = 10;
    int vetor[tamanho];
    
    cout << "Digite 10 números diferentes:\n";
    
    for (int i = 0; i < tamanho; i++) {
        int numero;
        bool repetido;
        
        do {
            repetido = false;
            
            cin >> numero;
            
            for (int j = 0; j < i; j++) {
                if (vetor[j] == numero) {
                    repetido = true;
                    cout << "Número repetido! Digite outro número:\n";
                    break;
                }
            }
        } while (repetido);
        
        vetor[i] = numero;
    }
    
    cout << "Vetor final:\n";
    for (int i = 0; i < tamanho; i++) {
        cout << vetor[i] << " ";
    }
    cout << endl;
    
    return 0;
}