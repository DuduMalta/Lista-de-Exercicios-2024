def interseccao(vetor1, vetor2):
    interseccao = []
    for elemento in vetor1:
        if elemento in vetor2 and elemento not in interseccao:
            interseccao.append(elemento)
    return interseccao

def main():
    vetor1 = []
    vetor2 = []

    print("Digite os elementos do primeiro vetor:")
    for _ in range(10):
        elemento = int(input())
        vetor1.append(elemento)

    print("Digite os elementos do segundo vetor:")
    for _ in range(10):
        elemento = int(input())
        vetor2.append(elemento)

    resultado = interseccao(vetor1, vetor2)

    print("A interseção dos vetores é:", resultado)

if __name__ == "__main__":
    main()
