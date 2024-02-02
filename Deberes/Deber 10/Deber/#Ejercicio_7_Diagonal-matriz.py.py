# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria
# Crear una matriz dada por el usuario y mostrar la diagonal principal de una matriz

# Pide el número de filas y columnas de la matriz
while (True):
    filas = int(input("Introduzca el número de filas de la matriz: "))
    columnas = int(input("Introduzca el número de columnas de la matriz: "))
    if (filas>0 and columnas>0):
        break
    else:
        print("Ingrese un número de filas y columnas válidas.")

matriz = []

# Lllenar matriz con datos digitados por el usuario
for fila in range(filas):
    fila_arreglo = []
    for columna in range(columnas):
        fila_arreglo.append(int(input("Ingrese el número de la posición [" + str(fila) + "][" + str(columna) + "]: ")))
    matriz.append(fila_arreglo)

print("MATRIZ ORIGINAL INGRESADA")

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()

print("DIAGONAL DE LA MATRIZ PRINCIPAL ")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if (i == j):
            print(matriz[i][j], end=" ")
        else:
            print(" ", end=" ")
    print() 
