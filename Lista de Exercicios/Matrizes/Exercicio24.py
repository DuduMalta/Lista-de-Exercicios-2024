def ler_tabuleiro():
    print("Digite o tabuleiro de jogo da velha (valores -1, 0, 1):")
    tabuleiro = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
            linha.append(valor)
        tabuleiro.append(linha)
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    print("Tabuleiro atual:")
    for linha in tabuleiro:
        print(linha)

def proxima_jogada(tabuleiro):
    melhor_jogada = None
    melhor_pontuacao = -1
  
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:

                tabuleiro[i][j] = -1
                pontuacao_jogada = avaliar_jogada(tabuleiro)
                tabuleiro[i][j] = 0
         
                if pontuacao_jogada > melhor_pontuacao:
                    melhor_pontuacao = pontuacao_jogada
                    melhor_jogada = (i, j)
    
    return melhor_jogada

def avaliar_jogada(tabuleiro):

    return 1

def main():
    tabuleiro = ler_tabuleiro()
    imprimir_tabuleiro(tabuleiro)
   
    jogada = proxima_jogada(tabuleiro)
    if jogada:
        print(f"Próxima jogada recomendada: {jogada}")
    else:
        print("Não foi possível determinar a próxima jogada.")

if __name__ == "__main__":
    main()
