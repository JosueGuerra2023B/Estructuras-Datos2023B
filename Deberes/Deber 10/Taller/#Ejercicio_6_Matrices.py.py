# Ejercicios Josue Guerra, Carlos Perez, Richard Soria
# Matrices
 
matriz = [[8,14,-6],[12,-7,4],[-11,3,21]]
print ("Impresion de la matriz: ")
print (matriz)
print ("\n")

# Mostrar todos los elementos de la matriz fila por fila

print ("Elementos de la fila: ")
for fila in matriz:
    print (fila)
print ("\n")

# Mostrar todos los elementos de la matriz elemento a elemento en columna

print ("Elementos en forma de columna: ")
for row in matriz:
    for elemento in row:
        print(elemento, end=" ")
    print()
print ("\n")

# Mostrar todos los elementos de la matriz en formato de matriz

print ("Elementos de forma ordenada")
for row in matriz:
    for elemento in row:
        print(elemento, end=" ")
    print()
print ("\n")

# Leer el ultimo elmento de cada fila

print ("Ultimo elemento de cada fila")
long= len(matriz)
for e in range(long):
    print(matriz[e][-1])
