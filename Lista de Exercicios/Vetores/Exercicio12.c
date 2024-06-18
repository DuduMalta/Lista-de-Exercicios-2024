#include <stdio.h>

int main() {
    
    int valores[5];
    int maior, menor;
    float media;
    int soma = 0;

    printf("Digite 5 valores:\n");
    for (int i = 0; i < 5; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &valores[i]);
    
        soma += valores[i];
 
        if (i == 0 || valores[i] > maior) {
            maior = valores[i];
        }
        if (i == 0 || valores[i] < menor) {
            menor = valores[i];
        }
    }

    media = (float)soma / 5;

    printf("\nValores lidos:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", valores[i]);
    }

    printf("\nMaior valor: %d\n", maior);
    printf("Menor valor: %d\n", menor);
    printf("Media dos valores: %.2f\n", media);

    return 0;
}
