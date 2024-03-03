# Ejercicios Diccionarios Joue Guerra, Carlos Perez, Richard Sorio
# Crud con Diccionarios

notas = {}

def agregarNota(notas, titulo, contenido):
    notas[titulo] = contenido

def verNotas(notas):
    if not notas:
        print("No existe ninguna nota ")
    else:
        for titulo, contenido in notas.items():
            print(f" {titulo} ")
            print(contenido)

def editarNota(notas, titulo, nuevoContenido):
    if titulo in notas:
        notas[titulo] = nuevoContenido
        print("La nota se actualizo exitosamente")
    else:
        print("La nota consulatda no se encuentra en el registro")

def eliminarNota(notas, titulo):
    if titulo in notas:
        del notas[titulo]
        print("La nota se elimino exitosamente")
    else:
        print("La nota que desea eliminar no se encuentra en el registro")

# Programa principal

while True:

    print("--------- BIENVENIDOS AL REGISTRO DE NOTAS ---------")
    print("1. Agregar nota")
    print("2. Ver nota")
    print("3. Editar nota")
    print("4. Eliminar nota")
    print("5. Salir \n")

    opcion = int(input("Ingrese la opcion a realizar: "))
    if opcion == 1:

        titulo = input("Ingrese el titulo de la nota: ")
        contenido = input("Ingrese el contenido de la nota: ")
        agregarNota(notas, titulo, contenido)
        print("La nota se agrego exitosamente")

    elif opcion == 2:
        verNotas(notas)

    elif opcion == 3:

        titulo = input("Ingrese el titulo de la nota que desea editar: ")
        nuevoContenido = input("Ingrese el nuevo contenido de la nota: ")
        editarNota(notas, titulo, nuevoContenido)

    elif opcion == 4:

        titulo = input("Ingrese el titulo de la nota que desea editar: ")
        eliminarNota(notas, titulo)

    elif opcion == 5:
        break
    else:
        print("La opcion ingresada no es valida")