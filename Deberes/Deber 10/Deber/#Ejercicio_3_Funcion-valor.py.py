# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria

# Crear varias funciones con el fin de que el usuario ingrese 
# por teclado la longitud de una lista, los valores de la lista 
# e imprima: la lista, la posición y el valor indicado por el usuario. 
# (Algoritmos de búsqueda lineal)

def crearLista(longitud):
    lista = []
    for i in range(longitud):
        valor = int (input("Ingrese un numero para la posicion {}: ".format(i)))
        lista.append(valor)
    return lista

def buscarValor(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def imprimirResultado (lista, posicion, valor):
    print("La lista es:", lista)
    if posicion != -1:
        print("El valor {} se encuentra en la posición {}.".format(valor, posicion))
    else:
        print("El valor {} no se encuentra en la lista.".format(valor))

# Programa Principal
        
longitud = int (input ("Ingrese la longitud de la lista: "))
lista = crearLista (longitud)
print ("La lista ingresada es: ",lista)

valor = int (input ("Ingrese el valor que desea buscar en la lista: "))
posicion = buscarValor (lista, valor)

imprimirResultado (lista, posicion, valor)