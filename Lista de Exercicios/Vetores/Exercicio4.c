#include <stdio.h>

int main() {
    int vetor[8];
    int x, y;

    printf("Digite os valores do vetor de 8 posicoes:\n");
    for (int i = 0; i < 8; i++) {
        printf("Posicao %d: ", i);
        scanf("%d", &vetor[i]);
    }

    printf("\nDigite dois valores para X e Y (entre 0 e 7):\n");
    printf("X: ");
    scanf("%d", &x);
    printf("Y: ");
    scanf("%d", &y);

    if (x >= 0 && x < 8 && y >= 0 && y < 8) {
        
        int soma = vetor[x] + vetor[y];
        printf("\nA soma dos valores nas posicoes %d e %d eh: %d\n", x, y, soma);
    } else {

        printf("\nOs valores de X e Y devem estar entre 0 e 7.\n");
    }

    return 0;
}