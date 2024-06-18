def gerar_matriz():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            if i < j:
                valor = 2*i + 7*j
            elif i == j:
                valor = 3*i**2
            else:
                valor = 4*i**3 + 5*j**2 + 1
            linha.append(valor)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:5}", end=" ")
        print()

def main():
    matriz = gerar_matriz()
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()
