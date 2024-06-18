#include <stdio.h>

int main() {
    const int tamanho = 20;
    int vetor[tamanho];
    int unicos[tamanho];
    int contador_unicos = 0;

    printf("Digite 20 numeros inteiros:\n");
    for (int i = 0; i < tamanho; i++) {
        printf("Elemento %d: ", i + 1);
        scanf("%d", &vetor[i]);
    }

    for (int i = 0; i < tamanho; i++) {
        int j;
        for (j = 0; j < contador_unicos; j++) {
            if (vetor[i] == unicos[j]) {
                break;
            }
        }
        if (j == contador_unicos) {
            unicos[contador_unicos++] = vetor[i];
        }
    }

    printf("\nElementos unicos:\n");
    for (int i = 0; i < contador_unicos; i++) {
        printf("%d ", unicos[i]);
    }
    printf("\n");

    return 0;
}
