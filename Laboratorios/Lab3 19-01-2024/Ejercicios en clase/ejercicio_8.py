# Contar de forma descendente hasta cero el número que ingrese por teclado l usuario. (Función recursiva)

def paresDecendente(numero):
    numero-=1
    if(numero>0):
        print(numero)
        paresDecendente(numero)
numero = int(input("Ingrese el número para para conocer sus anteriores pares: "))
numero+=1
paresDecendente(numero)

# Richard Soria, Josué Guerra, Carlos Pérez