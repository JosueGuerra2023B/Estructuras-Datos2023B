# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria
# Copiar una matriz a otra matriz

# Pide el número de filas y columnas de la matriz
while (True):
    filas = int(input("Introduzca el número de filas de la matriz: "))
    columnas = int(input("Introduzca el número de columnas de la matriz: "))
    if (filas>0 and columnas>0):
        break
    else:
        print("Ingrese un número de filas y columnas válidas.")

matriz = []
# Matriz original
for fila in range(filas):
    fila_arreglo = []
    for columna in range(columnas):
        fila_arreglo.append(int(input("Ingrese el número de la posición [" + str(fila) + "][" + str(columna) + "]: ")))
    matriz.append(fila_arreglo)

# Matriz copia
matriz_copia = []
for fila in range(filas):
    fila_arreglo = []
    for columna in range(columnas):
        fila_arreglo.append(0)
    matriz_copia.append(fila_arreglo)

print("MATRIZ ORIGINAL INGRESADA")
for i in matriz:
    for j in i:
        print(j, end=" ")
    print()

print("MATRIZ VACÍA A COPIAR")
for i in matriz_copia:
    for j in i:
        print(j, end=" ")
    print()

# Limpiar la matriz 
matriz_copia.clear()
# Copiar los datos de la matriz original
for fila in range(filas):
    fila_arreglo = []
    for columna in range(columnas):
        fila_arreglo.append(matriz[fila][columna])
    matriz_copia.append(fila_arreglo)

print("MATRIZ COPIADA")
for i in matriz_copia:
    for j in i:
        print(j, end=" ")
    print()