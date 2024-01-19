# Escribir un programa que pida números al usuario, mostrar el factorial de cada uno y, 
# al finalizar, la cantidad total de números leídos en total.
# Nota: Utilice una o más funciones, si es necesario.

def factorial(numero):
    factorial = 1
    for i in range(1, numero+1):
        factorial *= i
    return factorial
def continuar(opcion):
    while(True):
        if(opcion=="salir"):
            return True
        elif(opcion=="si"):
            return False
    
contador = 0
while(True):
    numero = int(input("Ingrese el número que desea conocer su factorial: "))

    if (numero>0):
        print("El factorial de", numero, "es igual a: ",factorial(numero))
        contador+=1
        opcion = str(input("¿Desea continuar (Escriba salir para finalizar)?\n"))
        if (continuar(opcion)==True):
            break
    elif (numero==0):
        print("El factorial de 0 es igual a: 1")
        contador+=1
        opcion = str(input("¿Desea continuar (Escriba salir para finalizar)?\n"))
        if (continuar(opcion)==True):
            break
    else:
        print("Ingrese una cantidad mayor y diferente de 0.")
    
print("Ha ingresado un total de", contador,"números")
# Richard Soria, Josué Guerra, Carlos Pérez