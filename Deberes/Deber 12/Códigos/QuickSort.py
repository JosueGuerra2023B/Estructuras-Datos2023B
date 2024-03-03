# Ejercicios Diccionarios Joue Guerra, Carlos Perez, Richard Sorio
# QuickSort

lista = [8, 12, 3, 11, 5, 9, 10, 4, 15, 7]

def dividir(lista):

    pivote = lista[0]
    menores = []
    mayores = []

    for i in range(1, len(lista)):

        if lista[i] < pivote:
            menores.append(lista[i])

        else:
            mayores.append(lista[i])
    return menores, pivote, mayores

def quicksort(lista):

    if len(lista) < 2:
        return lista 

    menores, pivote, mayores = dividir(lista)
    return quicksort(menores) + [pivote] + quicksort(mayores)

print(quicksort(lista))