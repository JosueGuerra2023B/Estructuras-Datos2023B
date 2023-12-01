# Ejercicio 6 del deber
# PAR DE NUM

from math import sqrt

num1 = float (input ("Ingresa el punto 1: "))
num2 = float (input ("Ingresa el punto 2: "))

y = float (input ("Ingresa el punto y1: "))
y = float (input ("Ingresa el punto y2: "))

distancia = sqrt ( (num1 - num2)**2 + (y - y)**2 )

print ("La distancia entre puntos es: ",distancia,)

print("Programa echo por Josue Eduard Guerra Lovato")