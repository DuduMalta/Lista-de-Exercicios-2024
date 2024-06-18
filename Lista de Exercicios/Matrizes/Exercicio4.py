def ler_matriz(dimensao):
    matriz = []
    print(f"Digite os elementos da matriz {dimensao}x{dimensao}:")
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            elemento = float(input(f"Elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def encontrar_maior_valor(matriz):
    maior_valor = matriz[0][0]
    localizacao = (0, 0)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                localizacao = (i, j)
    
    return localizacao

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)


def main():
    dimensao = 4
    matriz = ler_matriz(dimensao)
    
    print("\nMatriz inserida:")
    imprimir_matriz(matriz)
    
    localizacao_maior_valor = encontrar_maior_valor(matriz)
    print(f"\nO maior valor está localizado na posição {localizacao_maior_valor}.")

if __name__ == "__main__":
    main()
