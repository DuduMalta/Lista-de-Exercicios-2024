def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

vetor = []
print("Digite 10 números inteiros:")
for i in range(10):
    vetor.append(int(input()))

print("\nNúmeros primos e suas respectivas posições no vetor:")
for i in range(len(vetor)):
    if eh_primo(vetor[i]):
        print("Número:", vetor[i], "| Posição:", i)
