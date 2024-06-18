#include <stdio.h>

void insercao(int vetor[], int tamanho) {
    int i, chave, j;
    for (i = 1; i < tamanho; i++) {
        chave = vetor[i];
        j = i - 1;

        
        while (j >= 0 && vetor[j] > chave) {
            vetor[j + 1] = vetor[j];
            j = j - 1;
        }
        vetor[j + 1] = chave;
    }
}

int main() {
    int vetor[10];
    
    printf("Digite dez valores numéricos:\n");

    for (int i = 0; i < 10; i++) {
        scanf("%d", &vetor[i]);
        insercao(vetor, i + 1); 
    }

    printf("Valores em ordem crescente:\n");
    for (int i = 0; i < 10; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    return 0;
}