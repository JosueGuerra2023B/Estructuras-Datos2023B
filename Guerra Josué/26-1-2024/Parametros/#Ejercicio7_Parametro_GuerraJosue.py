#Guerra JoSUE
#EJEMPLO7

def llenarlista(lista, longitud):
    for i in range(longitud):
        elemento = int(input("Ingrese el elemento " + str(i + 1) + ": "))
        lista.append(elemento)

def mostrarlista(lista):
    print("Lista ingresada:", lista)

long_lista = int(input("Ingrese la longitud de la lista: "))

lista = []

llenarlista(lista, long_lista)

mostrarlista(lista)

"""
def llenarlista(lista):
    longitud = int(input("Ingrese la longitud de la lista: "))

    for i in range(longitud):
        i = int(input("Ingrese el elemento: "))
        lista.append(i)
    return(lista)

lista=[]
print("La lista es: ", llenarlista(lista))
"""