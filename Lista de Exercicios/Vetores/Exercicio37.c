#include <stdio.h>
#include <stdlib.h>

void merge(int vetor[], int inicio, int meio, int fim) {
    int tamanho_esquerdo = meio - inicio + 1;
    int tamanho_direito = fim - meio;

    int *vetor_esquerdo = (int *)malloc(sizeof(int) * tamanho_esquerdo);
    int *vetor_direito = (int *)malloc(sizeof(int) * tamanho_direito);

    for (int i = 0; i < tamanho_esquerdo; i++)
        vetor_esquerdo[i] = vetor[inicio + i];
    for (int j = 0; j < tamanho_direito; j++)
        vetor_direito[j] = vetor[meio + 1 + j];

    int i = 0, j = 0, k = inicio;
    while (i < tamanho_esquerdo && j < tamanho_direito) {
        if (vetor_esquerdo[i] <= vetor_direito[j]) {
            vetor[k] = vetor_esquerdo[i];
            i++;
        } else {
            vetor[k] = vetor_direito[j];
            j++;
        }
        k++;
    }

    while (i < tamanho_esquerdo) {
        vetor[k] = vetor_esquerdo[i];
        i++;
        k++;
    }

    while (j < tamanho_direito) {
        vetor[k] = vetor_direito[j];
        j++;
        k++;
    }

    free(vetor_esquerdo);
    free(vetor_direito);
}

void mergeSort(int vetor[], int inicio, int fim) {
    if (inicio < fim) {
        int meio = inicio + (fim - inicio) / 2;

        mergeSort(vetor, inicio, meio);

        mergeSort(vetor, meio + 1, fim);

        merge(vetor, inicio, meio, fim);
    }
}

int main() {
    int vetor[11] = {1, 2, 3, 4, 5, 6, 11, 10, 9, 8, 7};

    printf("Vetor original:\n");
    for (int i = 0; i < 11; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    mergeSort(vetor, 0, 10);

    printf("Vetor ordenado:\n");
    for (int i = 0; i < 11; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    return 0;
}