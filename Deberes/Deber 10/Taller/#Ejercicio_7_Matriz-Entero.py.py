# Ejercicios Josue Guerra, Carlos Perez, Richard Soria
# Generar una matriz con elementos enteros desde el 
# teclado que el usuario especifique el numero de 
# filas y columnas y mostrar en formato matriz

matriz = []
filas = int (input ("Ingrese el numero de filas: "))
columnas = int (input ("Ingrese el numero de columnas: "))

for fila in range (filas):
    fila = []
    for elemento in range (columnas):
        elemento = int (input ("Ingrese el elemento: "))
        fila.append (elemento)
    matriz.append (fila)

print ("La matriz generada es: ")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()