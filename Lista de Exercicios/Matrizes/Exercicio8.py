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

def calcular_soma_acima_diagonal_principal(matriz):
    soma = 0
    dimensao = len(matriz)
    for i in range(dimensao):
        for j in range(i + 1, dimensao):
            soma += matriz[i][j]
    return soma

def main():
    dimensao = 3
    matriz = ler_matriz(dimensao)
    
    soma_acima_diagonal = calcular_soma_acima_diagonal_principal(matriz)
    
    print(f"\nA soma dos elementos acima da diagonal principal é: {soma_acima_diagonal}")

if __name__ == "__main__":
    main()
