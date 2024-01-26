# Tarea Carlos Perez, Josue Guerra, Richard Soria

#Escribir un programa que pida 
#al usuario una palabra y muestre 
#por pantalla el número de veces 
#que contiene cada vocal.

def contar_vocales(palabra):
    contador_vocales = [0] * 5 
    for letra in palabra:
        letra = letra.lower()

        if letra in "aeiou":
            if letra == "a":
                contador_vocales[0] += 1
            elif letra == "e":
                contador_vocales[1] += 1
            elif letra == "i":
                contador_vocales[2] += 1
            elif letra == "o":
                contador_vocales[3] += 1
            elif letra == "u":
                contador_vocales[4] += 1


    print("-- La palabra repite la vocal 'a':", contador_vocales[0], "veces --")
    print("++ La palabra repite la vocal  'e':", contador_vocales[1], "veces ++")
    print("-/ La palabra repite la vocal  'i':", contador_vocales[2], "veces /-")
    print("/- La palabra repite la vocal  'o':", contador_vocales[3], "veces -/")
    print("** La palabra repite la vocal  'u':", contador_vocales[4], "veces **")

palabra_usuario = input("Ingrese una palabra: ")

contar_vocales(palabra_usuario)

