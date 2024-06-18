def preencher_vetor():
    vetor = []
    numero = 1
    while len(vetor) < 100:
        if numero % 7 != 0 and numero % 10 != 7:
            vetor.append(numero)
        numero += 1
    return vetor

vetor = preencher_vetor()

print("Os 100 primeiros números que não são múltiplos de 7 ou terminam com 7:")
print(vetor)
