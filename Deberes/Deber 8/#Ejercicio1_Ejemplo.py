# Ejercicio 1
# Solicitar al usuario el tamaño del arreglo
# Llenar el arreglo con los datos del usuario
# Sumar los pares del arreglo
# Contar los impares
#Ejercicio echo por Josué Guerra
import random
print("---Bienvenido al sistema---")
print(" Muestra de números pares e impares ")
tamanio = int(input("Ingrese el tamaño del arreglo: "))
arreglo = []

for i in range(tamanio):
    arreglo.append(random.randint(1, 100))
    
print("El arreglo generado es:")
print(" | ".join(str(num) for num in arreglo))

suma_pares = sum(num for num in arreglo if num % 2 == 0)
impares = sum(1 for num in arreglo if num % 2 != 0)

print("La suma de los pares es:", suma_pares)
print("La cantidad de impares es:", impares)
