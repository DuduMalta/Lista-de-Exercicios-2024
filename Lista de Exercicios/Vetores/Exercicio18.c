#include <stdio.h>

int main() {
    const int tamanho = 10;
    int vetor[tamanho];
    int x;

    printf("Digite 10 numeros:\n");
    for (int i = 0; i < tamanho; i++) {
        printf("Numero %d: ", i + 1);
        scanf("%d", &vetor[i]);
    }

    printf("\nDigite um numero inteiro x: ");
    scanf("%d", &x);

    int count = 0;
    printf("\nMultiplos de %d no vetor:\n", x);
    for (int i = 0; i < tamanho; i++) {
        if (vetor[i] % x == 0) {
            printf("%d ", vetor[i]);
            count++;
        }
    }

    printf("\nTotal de multiplos de %d: %d\n", x, count);

    return 0;
}