#Ejercicio 8
#if-else
# Ingresar dos números e imprimir el número mayor 

num1 = float(input(" Ingrese un número:"))
num2 = float(input(" Ingrese un número:"))

    
if(num1 != num2):
    if(num1>num2):
        print("El", num1, "mayor que ",num2)
    else:
        print("El", num1, "mayor que ",num2)
else:
    print("Ambos números son iguales no se puede ejecutar")