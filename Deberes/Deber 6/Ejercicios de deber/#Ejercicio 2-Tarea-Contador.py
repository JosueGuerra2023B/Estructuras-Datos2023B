# Ejercicio 2
# Pedir al usuario una número al azar y contar cuantos caracteres tiene
# Ejercicio echo por Carlos Perez

print("Ejercicio 2: Contador")
def contar_digitos(numero):
    contador = 0
    while numero != 0:
        numero = numero // 10
        contador = contador + 1
    return contador

numero_a_contar = float (input ("Ingrese el numero que quiera: "))
print("El numero de digitos es de: ",contar_digitos(numero_a_contar))