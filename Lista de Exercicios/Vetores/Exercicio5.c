#include <stdio.h>

int main() {
    int vetor[10];
    int pares = 0;

    printf("Digite os valores do vetor de 10 posicoes:\n");
    for (int i = 0; i < 10; i++) {
        printf("Posicao %d: ", i + 1);
        scanf("%d", &vetor[i]);
    }

    for (int i = 0; i < 10; i++) {
        if (vetor[i] % 2 == 0) {
            pares++;
        }
    }

    printf("\nO vetor possui %d valores pares.\n", pares);

    return 0;
}
