# Implementa una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base 10 de altura.

def area_rectangulo (base, altura):
    area = base * altura
    return area

print ("---Calculadora area de un rectangulo---")
base = float (input ("Ingrese la base: "))
altura = float (input ("Ingrese la altura: "))

print ("El area del rectangulo es",area_rectangulo (base,altura))
# Richard Soria, Josué Guerra, Carlos Pérez