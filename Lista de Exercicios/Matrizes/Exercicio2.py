def criar_matriz(dimensao):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            if i == j:
                linha.append(1)  
            else:
                linha.append(0)  
        matriz.append(linha)
    return matriz


def main():
    dimensao = 5
    matriz = criar_matriz(dimensao)
    
    
    for linha in matriz:
        print(linha)


if __name__ == "__main__":
    main()
