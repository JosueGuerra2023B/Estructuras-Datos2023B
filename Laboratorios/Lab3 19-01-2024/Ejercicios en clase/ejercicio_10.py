# Calcular el factorial de un número ingresado por el usuario. (Función recursiva)

def factorial(numero):
    
    if(numero==0 or numero==1):
        return 1
    elif(numero>0):
        numero_factorial = factorial(numero-1)*numero
    return numero_factorial

numero = int(input("Ingrese el número para conocer su factorial: "))
print("El factorial de ese número es:", factorial(numero))

# Richard Soria, Josué Guerra, Carlos Pérez