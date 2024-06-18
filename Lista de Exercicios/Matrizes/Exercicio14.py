import random

def gerar_cartela():
    cartela = []

    while len(cartela) < 5:
        linha = set()
        while len(linha) < 5:
            numero = random.randint(0, 99)
            linha.add(numero)
        cartela.append(sorted(linha))

    return cartela

def imprimir_cartela(cartela):
    print("Cartela de Bingo:")
    for linha in cartela:
        print(linha)

cartela = gerar_cartela()

imprimir_cartela(cartela)
