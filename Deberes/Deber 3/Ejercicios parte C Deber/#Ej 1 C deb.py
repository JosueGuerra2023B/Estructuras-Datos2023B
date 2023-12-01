# Ejercicio 1C del deber
# Programa de calculos

letra = input("Ingrese una letra: ")

if len(letra) == 1 and 'A' <= letra <= 'Z':
    print("La cadena ingresada es una letra mayúscula. ")
else:
    print("La cadena ingresada no es mayúscula. ")
#Se investigo un poco y se usa len, ya que es la función que 
#devuelve longitud o contar la cantidad de caracteres en un texto

print("Programa echo por Josue Eduard Guerra Lovato")