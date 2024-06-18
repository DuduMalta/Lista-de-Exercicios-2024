#include <stdio.h>

void soma_vetores(int x[], int y[], int resultado[]) {
    for (int i = 0; i < 5; i++) {
        resultado[i] = x[i] + y[i];
    }
}

void produto_vetores(int x[], int y[], int resultado[]) {
    for (int i = 0; i < 5; i++) {
        resultado[i] = x[i] * y[i];
    }
}

void diferenca_vetores(int x[], int y[], int resultado[], int *tamResultado) {
    *tamResultado = 0;
    for (int i = 0; i < 5; i++) {
        int estaEmY = 0;
        for (int j = 0; j < 5; j++) {
            if (x[i] == y[j]) {
                estaEmY = 1;
                break;
            }
        }
        if (!estaEmY) {
            resultado[*tamResultado] = x[i];
            (*tamResultado)++;
        }
    }
}

void interseccao_vetores(int x[], int y[], int resultado[], int *tamResultado) {
    *tamResultado = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (x[i] == y[j]) {
                resultado[*tamResultado] = x[i];
                (*tamResultado)++;
                break;
            }
        }
    }
}

void uniao_vetores(int x[], int y[], int resultado[], int *tamResultado) {
    *tamResultado = 0;
    for (int i = 0; i < 5; i++) {
        resultado[*tamResultado] = x[i];
        (*tamResultado)++;
    }
    for (int i = 0; i < 5; i++) {
        int estaEmX = 0;
        for (int j = 0; j < 5; j++) {
            if (y[i] == x[j]) {
                estaEmX = 1;
                break;
            }
        }
        if (!estaEmX) {
            resultado[*tamResultado] = y[i];
            (*tamResultado)++;
        }
    }
}

int main() {
    int x[5], y[5];
    int resultado[10];
    int tamResultado;

    printf("Digite os elementos do vetor x:\n");
    for (int i = 0; i < 5; i++) {
        scanf("%d", &x[i]);
    }

    printf("Digite os elementos do vetor y:\n");
    for (int i = 0; i < 5; i++) {
        scanf("%d", &y[i]);
    }

    soma_vetores(x, y, resultado);
    printf("Soma entre x e y: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", resultado[i]);
    }
    printf("\n");

    produto_vetores(x, y, resultado);
    printf("Produto entre x e y: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", resultado[i]);
    }
    printf("\n");

    diferenca_vetores(x, y, resultado, &tamResultado);
    printf("Diferença entre x e y: ");
    for (int i = 0; i < tamResultado; i++) {
        printf("%d ", resultado[i]);
    }
    printf("\n");

    interseccao_vetores(x, y, resultado, &tamResultado);
    printf("Interseção entre x e y: ");
    for (int i = 0; i < tamResultado; i++) {
        printf("%d ", resultado[i]);
    }
    printf("\n");

    uniao_vetores(x, y, resultado, &tamResultado);
    printf("União entre x e y: ");
    for (int i = 0; i < tamResultado; i++) {
        printf("%d ", resultado[i]);
    }
    printf("\n");

    return 0;
}
