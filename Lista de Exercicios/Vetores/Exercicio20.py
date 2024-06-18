primeiro_vetor = []

print("Digite 10 números inteiros no intervalo [0, 50]:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))

    if 0 <= numero <= 50:
        primeiro_vetor.append(numero)
    else:
        print("Número fora do intervalo. Tente novamente.")


segundo_vetor = [numero for numero in primeiro_vetor if numero % 2 != 0]

print("\nPrimeiro vetor:")
for i in range(0, len(primeiro_vetor), 2):
    print(primeiro_vetor[i], end=" ")
    if i + 1 < len(primeiro_vetor):
        print(primeiro_vetor[i + 1], end=" ")
    print()

print("\nSegundo vetor:")
for i in range(0, len(segundo_vetor), 2):
    print(segundo_vetor[i], end=" ")
    if i + 1 < len(segundo_vetor):
        print(segundo_vetor[i + 1], end=" ")
    print()
