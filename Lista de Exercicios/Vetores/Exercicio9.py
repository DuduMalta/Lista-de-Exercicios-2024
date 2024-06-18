def eh_par(numero):
    return numero % 2 == 0

valores_pares = []
while len(valores_pares) < 6:
    valor = int(input("Digite um valor inteiro par: "))
    if eh_par(valor):
        valores_pares.append(valor)
    else:
        print("O valor digitado não é par. Digite um valor inteiro par.")

print("\nValores lidos na ordem inversa:")
for valor in reversed(valores_pares):
    print(valor)
