# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria
# Sume dos matrices

while (True):
    filas = int(input("Introduzca el número de filas de las matrices: "))
    columnas = int(input("Introduzca el número de columnas de la matrices: "))
    if (filas>0 and columnas>0):
        break
    else:
        print("Ingrese un número de filas y columnas válidas.")

matriz = []
print("Ingresar los elementos de la matriz 1")
# Lllenar matriz 1 con datos digitados por el usuario
for fila in range(filas):
    fila_arreglo = []
    for columna in range(columnas):
        fila_arreglo.append(int(input("Ingrese el número de la posición [" + str(fila) + "][" + str(columna) + "]: ")))
    matriz.append(fila_arreglo)

matriz_2 = []
print("Ingresar los elementos de la matriz 2")
# Lllenar matriz 2 con datos digitados por el usuario
for fila in range(filas):
    fila_arreglo = []
    for columna in range(columnas):
        fila_arreglo.append(int(input("Ingrese el número de la posición [" + str(fila) + "][" + str(columna) + "]: ")))
    matriz_2.append(fila_arreglo)

# Sumar matrices
matriz_suma = []
for fila in range(filas):
    fila_arreglo = []
    for columna in range(columnas):
        fila_arreglo.append(int(matriz[fila][columna]+matriz_2[fila][columna]))
    matriz_suma.append(fila_arreglo)
# Matriz
print("MATRIZ 1")
for i in matriz:
    for j in i:
        print(j, end=" ")
    print()
# Matriz 2
print("MATRIZ 2")
for i in matriz_2:
    for j in i:
        print(j, end=" ")
    print()

# Imprime la suma de las matrices
print("MATRICES SUMADAS")
for i in matriz_suma:
    for j in i:
        print(j, end=" ")
    print()
