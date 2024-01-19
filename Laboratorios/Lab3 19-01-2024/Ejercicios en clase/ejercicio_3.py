#Solicitar al usuario que ingrese valores hasta que ingrese el cero. Por cada 
#valor ingresado sumar sus dígitos y mostrarlos en pantalla. Al finalizar, 
#calcular la suma total de todos los valores ingresados y la suma de sus dígitos. 

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

suma_numero = 0
total_digitos = 0
while (numero!=0):
    suma_numero+=numero
    digitos = Calcularsuma(numero)
    total_digitos += digitos
    print("La suma del número ingresado es:",Calcularsuma(numero))
    print("La suma de los números ingresado es:", suma_numero)
    print("La suma de todos los dígitos es:", total_digitos)
    numero = int(input("Ingrese el número a analizar: "))

# Richard Soria, Josué Guerra, Carlos Pérez