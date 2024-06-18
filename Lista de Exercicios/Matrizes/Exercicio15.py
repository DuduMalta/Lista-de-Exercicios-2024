matriz_respostas = [
    ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
    ['b', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
    ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
    ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
    ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
]

gabarito = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']

resultados = [0] * len(matriz_respostas)

for i in range(len(matriz_respostas)):
    pontuacao = 0
    for j in range(len(gabarito)):
        if matriz_respostas[i][j] == gabarito[j]:
            pontuacao += 1
    resultados[i] = pontuacao

print("Pontuações dos alunos:")
for i in range(len(resultados)):
    print(f"Aluno {i+1}: {resultados[i]} pontos")
