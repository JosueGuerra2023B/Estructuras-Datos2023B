# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
#Crear tupla con números e indicar el número mayor y el menor
print("\nSegunda tupla")
tupla2 = (2, 5, 100, 7, 2, 6, 8, 35, 28)
mayor = tupla2[0]
menor = tupla2[0]
for num in tupla2:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
print("El mayor es:", mayor)
print("El menor es:", menor)