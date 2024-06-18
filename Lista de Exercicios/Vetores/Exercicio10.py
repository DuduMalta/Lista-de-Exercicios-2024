def calcular_media(notas):
    total = sum(notas)
    return total / len(notas)


notas = []
for i in range(1, 16):
    nota = float(input(f"Digite a nota da prova do aluno {i}: "))
    notas.append(nota)

media_geral = calcular_media(notas)

print("\nMédia geral das notas:", media_geral)
