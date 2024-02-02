# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria
# Genere la matriz transpuesta de una matriz dada

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

# Mostrar Matriz original
print("MATRIZ ORIGINAL INGRESADA")

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()

# Mostar Matriz transpuesta
print("MATRIZ TRASNPUESTA")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[j][i], end=" ")
    print() 
