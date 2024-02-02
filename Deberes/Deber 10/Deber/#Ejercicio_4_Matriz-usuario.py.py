# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria

# Imprimir una matriz cuyos valores sean ingresados por 
# el usuario, además, se deberá ingresar las filas y las columnas.

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = input("Ingrese el valor: ")
        fila.append(valor)
    matriz.append(fila)

print("La matriz ingresada es:")
for fila in matriz:
    print(fila)