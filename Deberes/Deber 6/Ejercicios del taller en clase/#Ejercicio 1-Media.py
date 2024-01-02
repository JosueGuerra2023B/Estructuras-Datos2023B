#Ejercicio 1
# Pedir al usuario un número
# Realizar la suma de dichos números /Sacar el promedio
# Ejercicio echo por Carlos Perez

print("Ejercicio 1:\npromedio de un número")
numeros = []
while True:
    try:
        numero = float(input("Ingrese una nota: "))
        print("Ingrese 0 para salir\n")
        if numero == 0:
            break
        numeros.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")
if not numeros:
    print("No se ingresaron notas.")
else:
    suma_numero = sum(numeros)
    cantidad_numeros = len(numeros)
    promedio = suma_numero / cantidad_numeros
    print("Notas ingresadas: ", numeros )
    print("Cantidad de notas: ", cantidad_numeros)
    print("Suma de notas: ", suma_numero)
    print("Promedio de notas: ",round(promedio, 2))
print("Creado por Carlos perez")