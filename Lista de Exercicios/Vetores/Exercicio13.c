#include <stdio.h>

int main() {
    int valores[5];
    int maior, menor;
    int posicao_maior, posicao_menor;

    printf("Digite 5 valores:\n");
    for (int i = 0; i < 5; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &valores[i]);
    }

    maior = valores[0];
    menor = valores[0];
    posicao_maior = posicao_menor = 0;

    for (int i = 1; i < 5; i++) {
        if (valores[i] > maior) {
            maior = valores[i];
            posicao_maior = i;
        }
        if (valores[i] < menor) {
            menor = valores[i];
            posicao_menor = i;
        }
    }

    printf("\nPosicao do maior valor: %d\n", posicao_maior + 1);
    printf("Posicao do menor valor: %d\n", posicao_menor + 1);

    return 0;
}