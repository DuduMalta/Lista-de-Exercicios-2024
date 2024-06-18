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

def buscar_valor_na_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

def main():
    dimensao = 5 
    matriz = ler_matriz(dimensao)
    
    valor_x = float(input("\nDigite o valor que deseja buscar na matriz: "))

    localizacao = buscar_valor_na_matriz(matriz, valor_x)
    
    if localizacao:
        print(f"\nO valor {valor_x} foi encontrado na posição {localizacao}.")
    else:
        print(f"\nO valor {valor_x} não foi encontrado na matriz.")

if __name__ == "__main__":
    main()
