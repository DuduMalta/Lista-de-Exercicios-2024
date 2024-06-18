matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_diagonal_principal = 0

for i in range(len(matriz)):
    soma_diagonal_principal += matriz[i][i]

print("Matriz:")
for linha in matriz:
    print(linha)

print(f"\nSoma dos elementos da diagonal principal: {soma_diagonal_principal}")
