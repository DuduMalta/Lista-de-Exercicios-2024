#include <stdio.h>

int main() {
    int A[10], B[10], C[10];

    printf("Digite os 10 valores inteiros para o vetor A:\n");
    for (int i = 0; i < 10; i++) {
        printf("A[%d]: ", i);
        scanf("%d", &A[i]);
    }

    printf("\nDigite os 10 valores inteiros para o vetor B:\n");
    for (int i = 0; i < 10; i++) {
        printf("B[%d]: ", i);
        scanf("%d", &B[i]);
    }

    printf("\nCalculando o vetor C = A - B...\n");
    for (int i = 0; i < 10; i++) {
        C[i] = A[i] - B[i];
    }

    printf("\nValores do vetor C:\n");
    for (int i = 0; i < 10; i++) {
        printf("C[%d]: %d\n", i, C[i]);
    }

    return 0;
}
