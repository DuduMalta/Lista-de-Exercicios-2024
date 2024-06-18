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

def calcular_matriz_quadrado(matrizA):
    matrizB = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
   
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matrizB[i][j] += matrizA[i][k] * matrizA[k][j]
    
    return matrizB

def imprimir_matriz(matriz, nome):
    print(f"Matriz {nome}:")
    for linha in matriz:
        print(linha)

def main():

    print("Matriz A:")
    matrizA = ler_matriz()
 
    matrizB = calcular_matriz_quadrado(matrizA)

    imprimir_matriz(matrizB, "B = A^2")

if __name__ == "__main__":
    main()
