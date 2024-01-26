#Guerra JoSUE
#EJEMPLO6
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

def encontrarMax2(lista):
    lista.sort()
    return lista[-1]

def encontrarMin2(lista):
    lista.sort()
    return lista[0]

# Solicitar al usuario que ingrese el tamaño de la lista y la lista en sí
tamanio_lista = int(input("Ingrese el tamaño de la lista: "))
lista = []
for i in range(tamanio_lista):
    elemento = int(input(f"Ingrese el elemento {i+1}: "))
    lista.append(elemento)

# Mostrar los resultados de las funciones
print("Lista ingresada:", lista)
print("La suma es:", sumar(lista))
print("El mayor 1 es:", encontrarMax(lista))
print("El mayor 2 es:", encontrarMax2(lista))
print("El menor 1 es:", encontrarMin(lista))
print("El menor 2 es:", encontrarMin2(lista))