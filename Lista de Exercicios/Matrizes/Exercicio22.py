def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = float(input(f"Digite o elemento da posição [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def multiplicar_matrizes(matrizA, matrizB):
    matrizC = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
    
    return matrizC

def imprimir_matriz(matriz, nome):
    print(f"Matriz {nome}:")
    for linha in matriz:
        print(linha)

def main():

    print("Matriz A:")
    matrizA = ler_matriz()
    print("Matriz B:")
    matrizB = ler_matriz()
    
    if len(matrizA[0]) != len(matrizB):
        print("Não é possível multiplicar as matrizes A e B. O número de colunas de A não é igual ao número de linhas de B.")
        return
    
    matrizC = multiplicar_matrizes(matrizA, matrizB)
  
    imprimir_matriz(matrizC, "C")

if __name__ == "__main__":
    main()
