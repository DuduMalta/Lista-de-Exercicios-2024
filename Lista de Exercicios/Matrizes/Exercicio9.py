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

def calcular_soma_abaixo_diagonal_principal(matriz):
    soma = 0
    dimensao = len(matriz)
    for i in range(dimensao):
        for j in range(dimensao):
            if i > j:
                soma += matriz[i][j]
    return soma

def main():
    dimensao = 3
    matriz = ler_matriz(dimensao)
    
    soma_abaixo_diagonal = calcular_soma_abaixo_diagonal_principal(matriz)
    
    print(f"\nA soma dos elementos abaixo da diagonal principal é: {soma_abaixo_diagonal}")

if __name__ == "__main__":
    main()
