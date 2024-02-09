# Crear un archivo y escribir en él
def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f'Se ha escrito el contenido en el archivo {nombre_archivo}')

# Leer un archivo
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(f'Contenido del archivo {nombre_archivo}:')
            print(contenido)
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no se encontró')

# Agregar contenido a un archivo existente
def agregar_contenido(nombre_archivo, contenido):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(contenido)
    print(f'Se ha agregado contenido al archivo {nombre_archivo}')

nombre_archivo = 'ejemplo.txt'
escribir_archivo(nombre_archivo, 'Hola, este es un archivo de ejemplo.\n')
leer_archivo(nombre_archivo)
agregar_contenido(nombre_archivo, 'Esto es contenido adicional.\n')
leer_archivo(nombre_archivo)
