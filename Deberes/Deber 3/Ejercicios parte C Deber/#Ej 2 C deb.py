# Ejercicio 2C del deber
# Programa de calculos

edad = int(input("Ingrese su edad: "))
nota = float(input("Ingrese su nota: "))
genero = input("Ingrese su género (F para femenino, M para masculino): ")

if edad >= 18 and nota >= 5 and genero.upper() == 'F':
    print("Aceptada")
elif edad >= 18 and nota >= 5:
    print("Posible")
else:
    print("No aceptada")

print("Programa echo por Josue Eduard Guerra Lovato")