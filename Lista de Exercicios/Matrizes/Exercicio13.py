import random

def gerar_matriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            linha.append(random.randint(1, 20))
        matriz.append(linha)
    return matriz

def matriz_triangular_inferior(matriz):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            matriz[i][j] = 0
    return matriz
l
matriz_original = gerar_matriz()

matriz_transformada = matriz_triangular_inferior(matriz_original)

print("Matriz Original:")
for linha in matriz_original:
    print(linha)

print("\nMatriz Transformada (Triangular Inferior):")
for linha in matriz_transformada:
    print(linha)
