# Tarea Carlos Perez, Josue Guerra, Richard Soria

#solicite cuáles son los 8 equipos que serán 
#cabezas de serie, asigne aleatoriamente (y sin repeticiones) 
#los 24 equipos restantes, al final muestre el listado de las series resultantes.

import random

def sorteo():
    equipos = []


    print("Ingrese los números de los equipos que serán cabezas de serie:")
    equipos = [int(input("Equipo {}: ".format(i + 1))) for i in range(8)]

    equipos_resto = [equipo for equipo in range(1, 33) if equipo not in equipos]
    random.shuffle(equipos_resto)

    print("\nListado de las series resultantes:")
    for i in range(8):
        cabeza_serie = equipos[i]
        equipos_serie = [cabeza_serie] + equipos_resto[i * 3 : (i + 1) * 3]
        print("Serie {}: {}".format(i + 1, equipos_serie))

sorteo()
