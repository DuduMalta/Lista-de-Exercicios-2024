#include <stdio.h>

int main() {
    int numero_aluno, aluno_mais_baixo, aluno_mais_alto;
    float altura, altura_mais_baixa = 1000.0, altura_mais_alta = 0.0;

    for (int i = 0; i < 10; i++) {
        printf("Digite o numero do aluno e sua altura (em metros), separados por um espaco:\n");
        scanf("%d %f", &numero_aluno, &altura);

        if (altura < altura_mais_baixa) {
            altura_mais_baixa = altura;
            aluno_mais_baixo = numero_aluno;
        }

        if (altura > altura_mais_alta) {
            altura_mais_alta = altura;
            aluno_mais_alto = numero_aluno;
        }
    }

    printf("\nAluno mais baixo: Numero %d, Altura %.2fm\n", aluno_mais_baixo, altura_mais_baixa);
    printf("Aluno mais alto: Numero %d, Altura %.2fm\n", aluno_mais_alto, altura_mais_alta);

    return 0;
}
