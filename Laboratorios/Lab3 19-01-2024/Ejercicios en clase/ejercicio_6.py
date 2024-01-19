#Calcular el factorial de un numero ingresado por el usuario. Nota: Utilice una o 
#más funciones, según sea necesario. Utilice una función que calcule la frecuencia.

def factorial(numero):
    factorial = 1
    for i in range(1, numero+1):
        factorial *= i
    return factorial

numero = int(input("Ingrese el número para conocer su factorial: "))
print("El factorial de su número es:", factorial(numero))
        
# Richard Soria, Josué Guerra, Carlos Pérez