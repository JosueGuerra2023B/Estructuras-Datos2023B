# Construya una función que devuelva el área y la longitud de una circunferencia de radio r que se introducirá como parámetro. 
# Si no se especifica ningún parámetro se entenderá que el radio es la unidad.

import math
def area_y_longitud (radio):
    area =  math.pi *  radio * 2
    longitud = math.pi * (radio**2)
    print(" El area es",round(area,2))
    print(" La longitud es ",round(longitud,2))

radio = float (input ("Ingrese el radio del circulo: "))

if radio == 0:
    radio = 1
    area_y_longitud (radio)
else:
    area_y_longitud (radio)
# Richard Soria, Josué Guerra, Carlos Pérez