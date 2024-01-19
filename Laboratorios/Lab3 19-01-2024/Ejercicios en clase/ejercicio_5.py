# Imprimir en pantalla la cantidad de ocurrencias de un dígito que se encuentra
# en un número entero ingresado por el usuario.Nota: El usuario digitará tanto 
# el número entero como el dígito. Utilice una función que calcule la frecuencia.

def ocurrencias(numero, digito):
    cantidad_digitos = 0
    for i in str(numero):
        if i == str(digito):
            cantidad_digitos += 1
    return cantidad_digitos

numero = int(input("Ingrese el número: "))
digito = int(input("Ingrese el dígito que desea conocer su ocurrencia: "))
print("El digito se repite:",ocurrencias(numero,digito))

# Richard Soria, Josué Guerra, Carlos Pérez