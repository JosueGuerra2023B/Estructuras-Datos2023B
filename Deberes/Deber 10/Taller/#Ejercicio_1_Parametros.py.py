# Ejercicios Josue Guerra, Carlos Perez, Richard Soria
# Ejercicios con funciones

def pasarParametro (referencia, valor):
    referencia *= 2
    valor *= 2
    print ("Mensaje de la funcion: ",referencia, " ", valor)

lista = ["a","b","c"]
dato = "abc"

print ("Mensaje original: ",lista, " ",dato)
pasarParametro (lista, dato)
print ("Mensaje modificado: ",lista, " ",dato)
