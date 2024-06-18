#include <stdio.h>

int main() {
    float vetorX[5], vetorY[5];
    float produto_escalar = 0;

    printf("Digite os 5 elementos do primeiro vetor (vetorX):\n");
    for (int i = 0; i < 5; i++) {
        printf("x%d: ", i + 1);
        scanf("%f", &vetorX[i]);
    }

    printf("\nDigite os 5 elementos do segundo vetor (vetorY):\n");
    for (int i = 0; i < 5; i++) {
        printf("y%d: ", i + 1);
        scanf("%f", &vetorY[i]);
    }

    for (int i = 0; i < 5; i++) {
        produto_escalar += vetorX[i] * vetorY[i];
    }

    printf("\nVetor X:");
    for (int i = 0; i < 5; i++) {
        printf(" %.2f", vetorX[i]);
    }

    printf("\nVetor Y:");
    for (int i = 0; i < 5; i++) {
        printf(" %.2f", vetorY[i]);
    }

    printf("\n\nProduto Escalar: %.2f\n", produto_escalar);

    return 0;
}