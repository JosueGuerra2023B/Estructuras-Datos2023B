# Guerra JoSUE
# EJEMPLO1
#matrices
print("\nMatriz en fila: ")
matriz = [[1,2],[3,4]]
for fila in matriz:
    print(fila)

print("\nLos elementos de la matriz: ")
for fila in matriz:
    for elemento in fila:
        print(elemento)

print("\nLos elementos de la matriz ordenada: ")
for row in matriz:
    for elemento in row:
        print(elemento, end=" ")
    print()
