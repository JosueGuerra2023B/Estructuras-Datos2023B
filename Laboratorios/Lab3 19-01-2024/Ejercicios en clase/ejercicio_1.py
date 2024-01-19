# Pedir que el usuario ingrese valores hasta que ingrese el cero. Por cada valor, 
# mostrar la suma de sus dígitos. Mediante una función realice la suma.
#Funcion
def Calcularsuma(numero):
    suma = 0
    while(numero!=0):
        digito = numero%10
        suma += digito
        numero = numero//10
    return suma

#Programa Principal

numero = int(input("Ingrese el número a analizar: "))

while (numero!=0):
    print("La suma del número ingresado es:",Calcularsuma(numero))
    numero = int(input("Ingrese el número a analizar: "))

# Richard Soira, Josue Guerra, Carlos Pérez