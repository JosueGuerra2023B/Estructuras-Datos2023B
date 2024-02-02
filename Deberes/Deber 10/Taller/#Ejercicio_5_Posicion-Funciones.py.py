# Ejercicios Josue Guerra, Carlos Perez, Richard Soria
#Crear 3 funciones: sumar, encontrarMax, encontrarMin
def sumar(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    return suma
def encontrarMax(lista):
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo
def encontrarMin(lista):
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo
cantidad = int(input("Ingrese la cantidad de elementos en la lista: "))
lista = []
for i in range(cantidad):
    valor = int(input("Ingrese el valor del elemento: "))
    lista.append(valor)

print(lista)
print("La suma de los elementos de la lista es:", sumar(lista))
print("El mayor elemento de la lista es:", encontrarMax(lista))
print("El menor elemento de la lista es:", encontrarMin(lista))

