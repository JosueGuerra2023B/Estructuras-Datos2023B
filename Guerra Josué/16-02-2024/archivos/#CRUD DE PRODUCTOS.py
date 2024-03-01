print("-----MENU-----")

codigos = []
nombres = []
categorias = []
precios = []

# Abrir archivos
codigosLeer = open("archivos/Codigo-Productos.txt", "r")
nombresLeer = open("archivos/Nombres-Productos.txt", "r")
categoriasLeer = open("archivos/Categorias-Productos.txt", "r")
preciosLeer = open("archivos/Precios-Productos.txt", "r")

# Leer datos de los archivos y almacenarlos en las listas correspondientes
for c in codigosLeer.readline().split(' , '):
    if c != '':
        codigos.append(c)

for nombre in nombresLeer.readline().split(' , '):
    if nombre != '':
        nombres.append(nombre)

for categoria in categoriasLeer.readline().split(' , '):
    if categoria != '':
        categorias.append(categoria)

for precio in preciosLeer.readline().split(' , '):
    if precio != '':
        precios.append(precio)

# Cerrar archivos
codigosLeer.close()
nombresLeer.close()
categoriasLeer.close()
preciosLeer.close()

opcion=1
while opcion !=0:
    print("Menu Productos \n")
    print("1. Leer Productos\n2. Insertar Productos\n3. Eliminar Productos\n4. Modificar Productos\n0. Salir\n")
    opcion = int(input("Escoja la opción que desea realizar: "))

    if opcion == 1:
        print("Leer Productos/---/---\n")
        print("|Codigos  |  Nombres  |  Categorias  |  Precios")
        for i in range(len(codigos)):
            print(codigos[i], "     ", nombres[i], "  ", categorias[i], "     ", precios[i])

    elif opcion == 2:
        print("\n---/---/Insertar Productos/---/---")
        codigos.append(input("Ingrese el código del producto: "))
        nombres.append(input("Ingrese el Nombre del producto: "))
        categorias.append(input("Ingrese La Categoría del producto: "))
        precios.append(input("Ingrese el Precio del producto: "))

    elif opcion == 3:
        print("\n---/---/Eliminar productos/---/---")
        codigo = input("Ingrese el código del producto a eliminar: ")
        for i in range(len(codigos) - 1, -1, -1):
            if codigos[i] == codigo:
                codigos.pop(i)
                nombres.pop(i)
                categorias.pop(i)
                precios.pop(i)
                print("El producto se ha eliminado correctamente")
                break
        else:
            print("El código no se ha encontrado")

    elif opcion == 4:
        print("---/---/Modificar productos/---/---\n")
        codigo = input("Ingrese el código del producto que desea modificar: ")
        for i in range(len(codigos)):
            if codigos[i] == codigo:
                nombres[i] = input("Ingrese el nuevo Nombre del producto: ")
                categorias[i] = input("Ingrese la nueva Categoría del producto: ")
                precios[i] = input("Ingrese el nuevo Precio del producto: ")
                break
        else:
            print("El código no se ha encontrado")

    elif opcion == 0:
        print("Gracias por usar el sistema\n")
        break

# Abrir los archivos para escritura
archivoCodigos = open("archivos/Codigo-Productos.txt", "w")
for i in range(len(codigos)):
    archivoCodigos.write(codigos[i])
archivoNombres = open("archivos/Nombres-Productos.txt", "w")
for i in range(len(codigos)):
    archivoNombres.write(nombres[i])
archivoCategorias = open("archivos/Categorias-Productos.txt", "w")
for i in range(len(codigos)):
    archivoCategorias.write(categorias[i])
archivoPrecios = open("archivos/Precios-Productos.txt", "w")
for i in range(len(codigos)):
    archivoPrecios.write(precios[i])


# Cerrar los archivos
archivoCodigos.close()
archivoNombres.close()
archivoCategorias.close()
archivoPrecios.close()
