# Ejercicios Josue Guerra, Carlos Perez, Richard Soria
# Algoritmo de búsqueda lineal

def buscar_posicion(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i  
    return -1

lista = [2, 5, 3, 6, 8, 7, 4, 9, 1, 0]
print(lista)
posicion = int(input("Ingrese el elemento que desea buscar: "))

resultado = buscar_posicion(lista, posicion)

if resultado != -1:
    print("El elemento", posicion, "se encuentra en la posición", resultado, "de la lista.")
else:
    print("El elemento", posicion, "no está en la lista.")
    