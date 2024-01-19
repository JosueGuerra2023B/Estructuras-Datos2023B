#Solicitar al usuario que ingrese un número entero e imprimir en 
#pantalla si es primo o no. Utilice una función booleana que lo decida.

def numeroPrimo(numero):
    contador = 0
    for i in range(1,numero+1):
        if ((numero%i)==0):
            contador+=1
    return contador == 2
numero = int(input("Ingrese el número a validad: "))
if numeroPrimo(numero):
    print("El número es primo")
else:
    print("El número no es primo")
 
print(numeroPrimo(numero))

# Richard Soria, Josué Guerra, Carlos Pérez