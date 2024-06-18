def ler_matriz(dimensao):
    matriz = []
    print(f"Digite os elementos da matriz {dimensao}x{dimensao}:")
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            elemento = float(input(f"Matriz 1 - Elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def criar_terceira_matriz(matriz1, matriz2):
    dimensao = len(matriz1)
    matriz3 = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            maior_valor = max(matriz1[i][j], matriz2[i][j])
            linha.append(maior_valor)
        matriz3.append(linha)
    return matriz3

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def main():
    dimensao = 4
    print("Para a primeira matriz:")
    matriz1 = ler_matriz(dimensao)
    print("\nPara a segunda matriz:")
    matriz2 = ler_matriz(dimensao)
    
    matriz3 = criar_terceira_matriz(matriz1, matriz2)
    
    print("\nMatriz resultante (maiores valores de cada posição):")
    imprimir_matriz(matriz3)

if __name__ == "__main__":
    main()
