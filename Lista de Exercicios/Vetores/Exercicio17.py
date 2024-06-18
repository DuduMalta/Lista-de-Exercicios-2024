vetor = []
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(num)

for i in range(10):
    if vetor[i] < 0:
        vetor[i] = 0

print("Vetor com valores negativos substituídos por 0:", vetor)