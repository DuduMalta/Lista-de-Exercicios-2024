#include <stdio.h>

int main() {
    int numeros[6];
    int pares[6];
    int impares[6];
    int somaPares = 0;
    int contPares = 0;
    int contImpares = 0;

    printf("Digite 6 números inteiros:\n");
    for(int i = 0; i < 6; i++) {
        scanf("%d", &numeros[i]);
    }

    for(int i = 0; i < 6; i++) {
        if(numeros[i] % 2 == 0) {
            pares[contPares] = numeros[i];
            somaPares += numeros[i];
            contPares++;
        } else {
            impares[contImpares] = numeros[i];
            contImpares++;
        }
    }

    printf("Números pares digitados: ");
    for(int i = 0; i < contPares; i++) {
        printf("%d ", pares[i]);
    }
    printf("\n");

    printf("Soma dos números pares digitados: %d\n", somaPares);

    printf("Números ímpares digitados: ");
    for(int i = 0; i < contImpares; i++) {
        printf("%d ", impares[i]);
    }
    printf("\n");

    printf("Quantidade de números ímpares digitados: %d\n", contImpares);

    return 0;
}