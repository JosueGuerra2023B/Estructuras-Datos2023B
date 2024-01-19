# Contar de forma descendente hasta cero los números pares a partir de un número ingresado por el usuario. (Función recursiva)

def paresDecendente(numero):
    numero-=2
    if(numero>0):
        print(numero)
        paresDecendente(numero)
numero = int(input("Ingrese el número para para conocer sus anteriores pares: "))
numero+=2
paresDecendente(numero)

# Richard Soria, Josué Guerra, Carlos Pérez