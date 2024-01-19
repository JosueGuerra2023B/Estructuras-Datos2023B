# Ejercicio 3
# Se solicita al usuario que ingrese la cantidad deL ARREGLO
# Se ve si al número mayor es la suma de los otros o no 
#Ejercicio echo por Josué Guerra
import random
print("  ---Bienvenido al sistema---     ")
print(" Solicitud del rango del arreglo  ")
tamanio = int(input("Ingrese el tamaño del arreglo: "))
arreglo = []
suma = 0

# Llenar el arreglo con datos aleatorios
for i in range(tamanio):
    num = random.randint(1, 100)
    arreglo.append(num)
    suma += num
# Imprimir el arreglo generado
print("El arreglo generado es:")
print("|", end=" ")
for num in arreglo:
    print(num, "|", end=" ")
print()
# Encontrar el número mayor y menor en el arreglo
mayor = max(arreglo)
menor = min(arreglo)
print("El número mayor es:", mayor)
print("El número menor es:", menor)
# Verificar si existe un número que es la suma del resto
suma_encontrada = False
for num in arreglo:
    if num == suma - num:
        suma_encontrada = True
        print("El número que es la suma del resto es:", num, "y", suma - num)
        break

if not suma_encontrada:
    print("No existe un número que sea la suma del resto.")
