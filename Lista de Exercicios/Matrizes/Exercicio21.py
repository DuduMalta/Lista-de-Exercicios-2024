def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 2x2:")
    for i in range(2):
        linha = []
        for j in range(2):
            elemento = float(input(f"Digite o elemento da posição [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def somar_matrizes(matriz1, matriz2):
    matriz_soma = []
    for i in range(2):
        linha_soma = []
        for j in range(2):
            soma_elementos = matriz1[i][j] + matriz2[i][j]
            linha_soma.append(soma_elementos)
        matriz_soma.append(linha_soma)
    return matriz_soma

def subtrair_matrizes(matriz1, matriz2):
    matriz_subtracao = []
    for i in range(2):
        linha_subtracao = []
        for j in range(2):
            subtracao_elementos = matriz2[i][j] - matriz1[i][j]
            linha_subtracao.append(subtracao_elementos)
        matriz_subtracao.append(linha_subtracao)
    return matriz_subtracao

def adicionar_constante(matriz, constante):
    for i in range(2):
        for j in range(2):
            matriz[i][j] += constante

def imprimir_matriz(matriz, nome):
    print(f"Matriz {nome}:")
    for linha in matriz:
        print(linha)

def main():
 
    print("Matriz A:")
    matrizA = ler_matriz()
    print("Matriz B:")
    matrizB = ler_matriz()
 
    while True:
        print("\nMenu de opções:")
        print("a) Somar as duas matrizes")
        print("b) Subtrair a primeira matriz da segunda")
        print("c) Adicionar uma constante às duas matrizes")
        print("d) Imprimir as matrizes")
        print("e) Sair")
        
        opcao = input("Escolha uma opção (a, b, c, d, e): ")
        
        if opcao == 'a':
  
            matriz_soma = somar_matrizes(matrizA, matrizB)
            imprimir_matriz(matriz_soma, "Soma A + B")
        
        elif opcao == 'b':

            matriz_subtracao = subtrair_matrizes(matrizA, matrizB)
            imprimir_matriz(matriz_subtracao, "B - A")
        
        elif opcao == 'c':

            constante = float(input("Digite a constante a ser adicionada: "))
            adicionar_constante(matrizA, constante)
            adicionar_constante(matrizB, constante)
            print(f"Constante {constante} adicionada às matrizes A e B.")
        
        elif opcao == 'd':

            imprimir_matriz(matrizA, "A")
            imprimir_matriz(matrizB, "B")
        
        elif opcao == 'e':
   
            print("Programa encerrado.")
            break
        
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
