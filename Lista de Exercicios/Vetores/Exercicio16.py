def mostrar_vetor_direto(vetor):
    print("Vetor na ordem direta:", vetor)

def mostrar_vetor_inverso(vetor):
    print("Vetor na ordem inversa:", vetor[::-1])

vetor = []
for i in range(5):
    num = float(input(f"Digite o {i + 1}º número real: "))
    vetor.append(num)

codigo = int(input("Digite o código (0 para finalizar, 1 para ordem direta, 2 para ordem inversa): "))

if codigo == 0:
    print("Programa finalizado.")
elif codigo == 1:
    mostrar_vetor_direto(vetor)
elif codigo == 2:
    mostrar_vetor_inverso(vetor)
else:
    print("Código inválido.")