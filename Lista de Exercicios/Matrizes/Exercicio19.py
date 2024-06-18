def ler_matriz():
    matriz = []
    print("Digite as informações dos alunos:")
    for i in range(5):
        linha = []
        matricula = int(input(f"Matrícula do aluno {i+1}: "))
        media_provas = int(input(f"Média das provas do aluno {i+1}: "))
        media_trabalhos = int(input(f"Média dos trabalhos do aluno {i+1}: "))
        linha.append(matricula)
        linha.append(media_provas)
        linha.append(media_trabalhos)
        matriz.append(linha)
    return matriz

def calcular_e_identificar_maior_nota(matriz):
    maior_nota = float('-inf')
    matricula_maior_nota = None
    
    for aluno in matriz:
        matricula = aluno[0]
        media_provas = aluno[1]
        media_trabalhos = aluno[2]
        
        nota_final = media_provas + media_trabalhos
     
        if nota_final > maior_nota:
            maior_nota = nota_final
            matricula_maior_nota = matricula
    
    return matricula_maior_nota, maior_nota

def calcular_media_notas_finais(matriz):
    total_alunos = len(matriz)
    soma_notas_finais = sum(aluno[1] + aluno[2] for aluno in matriz)
    
    if total_alunos > 0:
        media = soma_notas_finais / total_alunos
    else:
        media = 0
    
    return media

def main():

    matriz_alunos = ler_matriz()

    matricula_maior_nota, maior_nota = calcular_e_identificar_maior_nota(matriz_alunos)
 
    media_notas_finais = calcular_media_notas_finais(matriz_alunos)
  
    print(f"Matrícula do aluno com maior nota final: {matricula_maior_nota}")
    print(f"Maior nota final: {maior_nota}")
    print(f"Média aritmética das notas finais: {media_notas_finais}")

if __name__ == "__main__":
    main()
