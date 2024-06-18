def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 3x6:")
    for i in range(3):
        linha = []
        for j in range(6):
            elemento = float(input(f"Digite o elemento da posição [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def calcular_soma_colunas_impares(matriz):
    soma_colunas_impares = 0
    for i in range(3):
        for j in range(1, 6, 2):
            soma_colunas_impares += matriz[i][j]
    return soma_colunas_impares

def calcular_media_colunas_2_e_4(matriz):
    soma_coluna_2 = 0
    soma_coluna_4 = 0
    for i in range(3):
        soma_coluna_2 += matriz[i][1]
        soma_coluna_4 += matriz[i][3]
    
    media_colunas_2_e_4 = (soma_coluna_2 + soma_coluna_4) / 3
    return media_colunas_2_e_4

def substituir_coluna_6(matriz):
    for i in range(3):
        soma_coluna_1_2 = matriz[i][0] + matriz[i][1]
        matriz[i][5] = soma_coluna_1_2

def imprimir_matriz(matriz):
    print("Matriz modificada:")
    for linha in matriz:
        print(linha)

def main():
 
    matriz = ler_matriz()
    
    soma_impares = calcular_soma_colunas_impares(matriz)
    print(f"Soma dos elementos das colunas ímpares (1, 3, 5): {soma_impares}")
 
    media_colunas_2_e_4 = calcular_media_colunas_2_e_4(matriz)
    print(f"Média aritmética dos elementos das colunas 2 e 4: {media_colunas_2_e_4}")

    substituir_coluna_6(matriz)

    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()
