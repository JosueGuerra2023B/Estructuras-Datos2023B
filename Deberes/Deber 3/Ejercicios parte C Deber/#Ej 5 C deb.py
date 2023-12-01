# Ejercicio 5C del deber
#Ganancia obtenida

precio = float(input("Ingrese el precio de la uva: "))

print("Seleccione el tipo de uva ")
print("1. Tipo A")
print("2. Tipo B")
uva = int(input("Ingrese la opción: "))

print("Seleccione el tamaño de la uva")
print("1. Tamaño 1")
print("2. Tamaño 2")
tamaño = int(input("Ingrese la opción: "))

if uva == 1:
    valor = precio * (0.20 if tamaño == 1 else 0.30)
elif uva == 2:
    valor = precio * (0.30 if tamaño == 1 else 0.50)

print("El valor es:", precio + valor)

print("Programa echo por Josue Eduard Guerra Lovato")