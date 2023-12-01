# Ejercicio 1 del deber
# Programa de calculos
import math

pi = math.pi
print ("/-/-/-/-/ Perimetro y Area de un circulo y un rectángulo /-/-/-/-/")
print ("/-/-/-/-/ Perimetro y Area de un rectángulo /-/-/-/-/")

b = float (input ("Ingrese la base: "))
h = float (input ("Ingrese la altura: "))

per = 2 * h + 2 * b
alt = b * h

print ("El perimetro es ",per,"")
print ("El area es ",alt,"")

print (" Perimetro y area de un circulo ")
ra = float (input ("Ingrese el radio: "))
p = 2 * pi * ra
a =  pi * ra**2

print ("El perimetro es ",p,"")
print ("El area es ",a,"")

print("Programa echo por Josue Eduard Guerra Lovato")