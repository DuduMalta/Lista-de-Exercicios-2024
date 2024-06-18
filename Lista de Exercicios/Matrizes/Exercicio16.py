gabarito = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']

num_alunos = 3

notas = []

for i in range(num_alunos):
    matricula = int(input(f"Digite a matrícula do aluno {i+1}: "))
    respostas_aluno = []
    for j in range(10):
        resposta = input(f"Digite a resposta do aluno {matricula} para a questão {j+1} (a, b, c, d ou e): ").lower()
        respostas_aluno.append(resposta)

    nota = 0
    for k in range(10):
        if respostas_aluno[k] == gabarito[k]:
            nota += 1
    
    notas.append((matricula, respostas_aluno, nota))

print("\nResultados:")
for aluno in notas:
    matricula, respostas, nota = aluno
    print(f"Matrícula: {matricula}")
    print(f"Respostas: {respostas}")
    print(f"Nota: {nota}")
    if nota >= 7.0:
        print("Situação: Aprovado\n")
    else:
        print("Situação: Reprovado\n")

aprovados = sum(1 for aluno in notas if aluno[2] >= 7.0)
percentual_aprovacao = (aprovados / num_alunos) * 100

print(f"Percentual de aprovação na turma: {percentual_aprovacao:.2f}%")
