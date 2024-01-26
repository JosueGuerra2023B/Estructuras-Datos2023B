# Tarea Carlos Perez, Josue Guerra, Richard Soria

# funcion de pytho para ordenar la lista

enteros = [5,4,3,2,1,6,7,8,9]
enteros.sort ()
print (enteros)

# Realizar un algoritmo que orde los elementos de la lista
n = len(enteros)
def ordenar_lista (enteros):
    for i in range (n):
        for j in range (0, n-i-1):
            if enteros[j] > enteros[j+1]:
                enteros[j], enteros[j+1] = enteros[j+1], enteros[j]

ordenar_lista(enteros)
print (enteros)


