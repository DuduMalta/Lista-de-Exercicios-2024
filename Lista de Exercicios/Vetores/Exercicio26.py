import math

def calcular_media(vetor):
    return sum(vetor) / len(vetor)

def calcular_desvio_padrao(vetor):
    media = calcular_media(vetor)
    diferenca_quadrada = [(x - media) ** 2 for x in vetor]
    variancia = sum(diferenca_quadrada) / len(vetor)
    desvio_padrao = math.sqrt(variancia)
    return desvio_padrao

vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

desvio_padrao = calcular_desvio_padrao(vetor)

print("O desvio padrão do vetor é:", desvio_padrao)