def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 4x4:")
    for i in range(4):
        linha = []
        for j in range(4):
            elemento = float(input(f"Elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def contar_maiores_que_10(matriz):
    contador = 0
    for linha in matriz:
        for elemento in linha:
            if elemento > 10:
                contador += 1
    return contador


def main():
    matriz = ler_matriz()
    quantidade_maiores_que_10 = contar_maiores_que_10(matriz)
    print(f"A matriz possui {quantidade_maiores_que_10} valores maiores que 10.")


if __name__ == "__main__":
    main()
