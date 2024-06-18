def triangulo_de_pascal(n):
    triangulo = []
    for linha in range(n):
        linha_atual = [1]
        if linha > 0:
            for j in range(1, linha):
                linha_atual.append(triangulo[linha - 1][j - 1] + triangulo[linha - 1][j])
            linha_atual.append(1)
        triangulo.append(linha_atual)
    return triangulo

def imprimir_triangulo(triangulo):
    for linha in triangulo:
        print(" ".join(map(str, linha)))

def main():
    n = int(input("Digite um número inteiro positivo: "))
    if n <= 0:
        print("O número precisa ser positivo.")
        return
    resultado = triangulo_de_pascal(n)
    imprimir_triangulo(resultado)

if __name__ == "__main__":
    main()
