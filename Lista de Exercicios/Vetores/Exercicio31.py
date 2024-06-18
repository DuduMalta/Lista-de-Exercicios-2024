def uniao(vetor1, vetor2):
    uniao = vetor1.copy()
    for elemento in vetor2:
        if elemento not in uniao:
            uniao.append(elemento)
    return uniao

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

    resultado = uniao(vetor1, vetor2)

    print("A união dos vetores é:", resultado)

if __name__ == "__main__":
    main()
