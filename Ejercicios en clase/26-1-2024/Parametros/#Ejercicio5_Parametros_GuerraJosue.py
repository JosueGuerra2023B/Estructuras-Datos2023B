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
#Guerra JoSUE
#EJEMPLO5
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

lista = [1, 5, 8, 7, 2, 6, 9, 4]
print(sumar(lista))
print("El mayor 1 es:", encontrarMax(lista))
print("El mayor 2 es:", encontrarMax2(lista))
print("El menor 1 es:", encontrarMin(lista))
print("El menor 2 es:", encontrarMin2(lista))
