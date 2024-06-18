#include <stdio.h>

int main() {
    float conjunto_original[10];
    float conjunto_quadrado[10];

    printf("Digite 10 numeros reais:\n");
    for (int i = 0; i < 10; i++) {
        printf("Numero %d: ", i + 1);
        scanf("%f", &conjunto_original[i]);
    }

    for (int i = 0; i < 10; i++) {
        conjunto_quadrado[i] = conjunto_original[i] * conjunto_original[i];
    }

    printf("\nConjunto original:\n");
    for (int i = 0; i < 10; i++) {
        printf("%.2f ", conjunto_original[i]);
    }

    printf("\nConjunto com quadrados:\n");
    for (int i = 0; i < 10; i++) {
        printf("%.2f ", conjunto_quadrado[i]);
    }

    return 0;