import random

matriz_notas = []
for _ in range(10):
    linha = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
    matriz_notas.append(linha)

pior_nota_prova1 = 0
pior_nota_prova2 = 0
pior_nota_prova3 = 0

for aluno in matriz_notas:
    nota1, nota2, nota3 = aluno
    pior_nota = min(nota1, nota2, nota3)

    if pior_nota == nota1:
        pior_nota_prova1 += 1
    elif pior_nota == nota2:
        pior_nota_prova2 += 1
    elif pior_nota == nota3:
        pior_nota_prova3 += 1

print("Número de alunos cuja pior nota foi:")
print(f"Prova 1: {pior_nota_prova1}")
print(f"Prova 2: {pior_nota_prova2}")
print(f"Prova 3: {pior_nota_prova3}")
