# Ejercicio 2
#  se solicita al usuario que ingrese la cantidad de nombres a ingresar.
# Para luego analizar si tiene más de 5 caracteres
#Ejercicio echo por Josué Guerra

print("         ---Bienvenido al sistema---            ")
print(" Solicitud de nombres ingresados por le usuario ")

n = int(input("Inserte la cantidad de nombres que desea: "))
# Inicializar un arreglo vacío
nombres = []
for i in range(n):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    if len(nombre) > 5:
        nombres.append(nombre)

# Imprimir los nombres con más de 5 caracteres del arreglo
print("Nombres con más de 5 caracteres ingresados:")
for nombre in nombres:
    print(nombre)
