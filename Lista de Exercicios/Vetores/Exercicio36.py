def main():
    vetor = []
    print("Digite 10 números reais:")
    for _ in range(10):
        numero = float(input())
        vetor.append(numero)

    vetor_ordenado = sorted(vetor)

    print("Vetor ordenado:")
    for numero in vetor_ordenado:
        print(numero)

if __name__ == "__main__":
    main()
