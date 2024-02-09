# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
# Ejercicios Tarea

def siguiente_mayor (lista):
    lista_nueva = []
    for i in range (len(lista)):
        siguiente_numero = (lista[i] + 1)
        lista_nueva.append(siguiente_numero)
    return lista_nueva
    
# Programa Principal
    
lista = []

longitud = int (input ("Ingresa la longitud de la lista: "))

for i in range (longitud):
    elemento = int (input ("Ingresa un numero entero: "))
    lista.append (elemento)
print ("La lista es: ", lista)
resultado = siguiente_mayor (lista)
print ("La lista modificada es: ",resultado)