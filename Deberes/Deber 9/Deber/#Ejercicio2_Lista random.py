# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Programa que inicialice una lista con 10 valores aleatorios 
#(del 1 al 10) y posteriormente muestre en pantalla cada 
#elemento de la lista junto con su cuadrado. 

import random

lista = [random.randint(1, 10) for i in range(10)]

for i in lista:
    print(f"{i} al cuadrado es {i**2}")