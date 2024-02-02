# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria

# Crea un función “ConvertirEspaciado”, que reciba como 
# parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. 
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
# Crea un programa principal donde se use dicha función.

def ConvertirEspaciado(texto):
    resultado = ""
    for letra in texto:
        resultado += letra + " "
    return resultado

texto = input("Ingrese un texto: ")
resultado = ConvertirEspaciado(texto)
print("El resultado es:", resultado)
