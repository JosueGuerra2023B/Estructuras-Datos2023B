# Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese 
# un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. También 
# solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número 
# (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.

def numeroPrimo(numero):
    contador = 0
    for i in range(1,numero+1):
        if ((numero%i)==0):
            contador+=1
    return contador == 2
def calcularSuma(numero):
    suma = 0
    while(numero!=0):
        digito = numero%10
        suma += digito
        numero = numero//10
    return suma
def ocurrencias(numero, digito):
    cantidad_digitos = 0
    for i in str(numero):
        if i == str(digito):
            cantidad_digitos += 1
    return cantidad_digitos
def factorial(numero):
    factorial = 1
    for i in range(1, numero+1):
        factorial *= i
    return factorial

numeros_almacenados = []

while(True):
    numero = int(input("Ingrese el número a validar: "))
    numeros_almacenados.append(numero)
    if numeroPrimo(numero):
        print("El número es primo")
        print("La suma de los dígitos del número", numero,"es:", calcularSuma(numero))
        digito = int(input("Ingrese el dígito que desea conocer su ocurrencia: "))
        print("El digito se repite:",ocurrencias(numero,digito))
    else:
        print("El número no es primo")
        break
numero_mayor = max(numeros_almacenados)
print("El factorial del mayor número es:", factorial(numero_mayor))

# Richard Soria, Josué Guerra, Carlos Pérez