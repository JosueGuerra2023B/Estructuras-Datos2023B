# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria
def LongitudPila(pila):
    return len(pila)

def EstaVaciaPila(pila):
    return len(pila) == 0

def EstaLlenaPila(pila, tamano_maximo):
    return len(pila) == tamano_maximo

def AddPila(cadena, pila, tamano_maximo):
    if not EstaLlenaPila(pila, tamano_maximo):
        pila.append(cadena)
    else:
        print("La pila está llena. No se puede añadir más elementos.")

def SacarDeLaPila(pila):
    if not EstaVaciaPila(pila):
        return pila.pop()
    else:
        print("La pila está vacía. No se puede sacar ningún elemento.")

def EscribirPila(pila):
    print("Los elementos de la pila son:")
    for elemento in pila:
        print(elemento)

# Programa Principal
# Realiza un programa que permita
# usar las funciones anterior, que
# muestre un menú, con las siguientes opciones:
# Añadir elemento a la pila
# Sacar elemento de la pila
# Longitud de la pila
# Mostrar pila
# Salir

tamano_maximo = int (input ("Ingrese el tamaño maximo de la pila: "))
pila = []

op = 0
while op != 5:
    print("Menú:")
    print("1. Añadir elemento a la pila")
    print("2. Sacar elemento de la pila")
    print("3. Longitud de la pila")
    print("4. Mostrar pila")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        cadena = input ("Introduce una cadena: ")
        AddPila(cadena, pila, tamano_maximo)
        
    elif opcion == "2":
        elemento = SacarDeLaPila(pila)
        if elemento is not None:
            print("Elemento sacado de la pila:", elemento)
            
    elif opcion == "3":
        print("Longitud de la pila:", LongitudPila(pila))
        
    elif opcion == "4":
        EscribirPila(pila)
        
    elif opcion == "5":
        print ("Gracias por usar nuestro programa")
        exit (0)