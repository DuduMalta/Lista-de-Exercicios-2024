def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Digite o elemento da posição [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def calcular_somas_colunas(matriz):
    vetor_somas = [0] * 3
    
    for j in range(3):
        soma_coluna = 0
        for i in range(3):
            soma_coluna += matriz[i][j]
        vetor_somas[j] = soma_coluna
    
    return vetor_somas

def imprimir_vetor_somas(vetor_somas):
    print("Vetor de somas das colunas da matriz:")
    for soma in vetor_somas:
        print(soma)

def main():

    matriz = ler_matriz()
    
    vetor_somas = calcular_somas_colunas(matriz)
    
  
    imprimir_vetor_somas(vetor_somas)

if __name__ == "__main__":
    main()
