# Ejercicios Josue Guerra, Carlos Perez, Richard Soria
# Ejemplo2 
# Busqueda Binaria

def busqueda_binaria_recursiva(lista, valor, izq, der):
    if izq > der:
        return -1

    medio = (izq + der) // 2

    if lista[medio] == valor:
        return medio
    elif lista[medio] < valor:
        return busqueda_binaria_recursiva(lista, valor, medio + 1, der)
    else:
        return busqueda_binaria_recursiva(lista, valor, izq, medio - 1)

# Ejemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13]
while True:
    valor = int(input("Inserte el valor a encontrar (0 para salir): "))  # Convertir la entrada a entero

    if valor == 0:
        break
    resultado = busqueda_binaria_recursiva(lista, valor, 0, len(lista) - 1)
    if resultado != -1:
        print("El valor", valor, "se encuentra en el índice", resultado)
    else:
        print("El valor", valor, "no se encuentra en la lista")

