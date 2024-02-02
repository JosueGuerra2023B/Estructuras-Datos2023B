# Ejercicios Josue Guerra, Carlos Perez, Richard Soria
# Busqueda binaria
def busqueda_binaria(lista, numero):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == numero:
            return medio
        elif lista[medio] < numero:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Ejemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13]
numero_buscar = int(input("Indique el valor a buscar: "))  
resultado = busqueda_binaria(lista, numero_buscar)

if resultado != -1:
    print("El número", numero_buscar, "se encuentra en el índice", resultado)
else:
    print("El número", numero_buscar, "no se encuentra en la lista")
