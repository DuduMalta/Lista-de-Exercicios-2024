vetor = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    vetor.append(numero)

quantidade_negativos = 0
soma_positivos = 0

for num in vetor:
    if num < 0:
        quantidade_negativos += 1
    else:
        soma_positivos += num

print(f"\nQuantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")

