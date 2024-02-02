# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
# Suma elemntos de la lista

def sumarElementos (lista):
    contador = 0

    for elemento in lista:
        contador += elemento
    return contador

lista = [9,8,7,6]
print(lista)
print (sumarElementos (lista))