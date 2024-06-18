matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        transposta[j][i] = matriz[i][j]

print("Matriz original:")
for linha in matriz:
    print(linha)

print("\nTransposta da matriz:")
for linha in transposta:
    print(linha)
