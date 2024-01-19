# Desarrollar un programa que permita al usuario obtener un identificador 
#de la “La Unión”. Para eso ingresará el nombre completo y número de DNI de cada 
#socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.

def get_socio_id():
    nombre1 = input("Ingrese el nombre del socio (deje en blanco para finalizar): ")
    while nombre1 != "":
        if len(nombre1.split()) < 2:
            print("Formato de nombre inválido. Por favor, ingrese el nombre en el formato: nombre1 nombre2 apellido.")
            nombre1 = input("Ingrese el nombre del socio (deje en blanco para finalizar): ")
            continue
        dni = input("Ingrese el DNI del socio (10 dígitos): ")
        while len(dni) != 10:
            print("Formato de DNI inválido. Por favor, ingrese un DNI válido (10 dígitos).")
            dni = input("Ingrese el DNI del socio (10 dígitos): ")
        nombre2 = nombre1.split()[0]
        apellido = nombre1.split()[-1]
        apellido_len = len(apellido)
        socio_id = nombre2 + str(apellido_len) + dni[:3]
        print("ID de socio:", socio_id)
        nombre1 = input("Ingrese el nombre del socio (deje en blanco para finalizar): ")

get_socio_id()

# Richard Soria, Josué Guerra, Carlos Pérez