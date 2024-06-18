def compactar_vetor(vetor):
    vetor_compactado = []
    
    for elemento in vetor:
        if elemento != 0:
            vetor_compactado.append(elemento)
    
    return vetor_compactado

def main():
    vetor = []
    
    print("Digite os elementos do vetor:")
    for _ in range(15):
        elemento = int(input())
        vetor.append(elemento)
    
    vetor_compactado = compactar_vetor(vetor)
    
    print("Vetor compactado:", vetor_compactado)

if __name__ == "__main__":
    main()
