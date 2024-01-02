# Ejercicio 5
# Compra por el día de la madre
# Ejercicio hecho por Josué Guerra

print("Ejercicio 5: Compra día de la madre")

print("--/--/--/-/ Centro comercial el CORAL /-/--/--/--")
print("Bienvenido")
print("Este es el sistema del centro comercial el CORAL")
print(" 1. Entrar categorías de compra")
print(" 2. Mostrar factura")
print(" 3. Salir ")
categorias = {
    1: {"Perfumería": {"Tentación": 30, "Primavera": 28, "Otoño": 15, "Seducción": 35}},
    2: {"Joyería": {"Aretes": 7, "Collar": 5, "Cadena": 20, "Pulsera": 15}},
    3: {"Maquillaje": {"Sombras": 8, "Maquillaje": 5, "Labiales": 4, "Rimel": 6}},
    4: {"Ropa": {"Blusa": 25, "Chaqueta": 60, "Pantalón": 18, "Abrigo": 90}}
}
subtotal_total = 0
articulos_comprados = {categoria: 0 for categoria in categorias}

while True:
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        print("\nCategorías disponibles:")
        for num_categoria, categoria in categorias.items():
            print(num_categoria, "-", list(categoria.keys())[0])
        num_categoria_elegida = int(input("Ingrese el número de la categoría de compra: "))
        if num_categoria_elegida in categorias:
            categoria_elegida = list(categorias[num_categoria_elegida].keys())[0]
            while True:
                print("\nArtículos disponibles en", categoria_elegida + ":")
                for num_articulo, (articulo, precio) in enumerate(categorias[num_categoria_elegida][categoria_elegida].items(), 1):
                    print(num_articulo, "-", articulo, "$", precio)
                num_articulo_elegido = int(input("Ingrese el número del artículo que desea comprar: "))
                if 1 <= num_articulo_elegido <= len(categorias[num_categoria_elegida][categoria_elegida]):
                    articulo_elegido = list(categorias[num_categoria_elegida][categoria_elegida].keys())[num_articulo_elegido - 1]
                    cantidad = int(input("Ingrese la cantidad de unidades: "))
                    subtotal_total += categorias[num_categoria_elegida][categoria_elegida][articulo_elegido] * cantidad

                    if categoria_elegida in articulos_comprados:
                        articulos_comprados[categoria_elegida] += cantidad
                    else:
                        articulos_comprados[categoria_elegida] = cantidad
                    comprar_otro = input("¿Desea comprar otro artículo de esta categoría? (S/N): ")
                    if comprar_otro.upper() != "S":
                        break
                else:
                    print("Artículo no válido. Inténtelo de nuevo.")
        else:
            print("Categoría no válida. Inténtelo de nuevo.")

    elif opcion == 2:
        print("\nMostrar factura:")
        for categoria, cantidad in articulos_comprados.items():
            if cantidad > 0:
                subtotal_categoria = sum([categorias[num_categoria][categoria_articulo][articulo] * cantidad for categoria_articulo in categorias[num_categoria] for articulo, _ in categorias[num_categoria][categoria_articulo].items()])
                print(categoria + ":", cantidad, "unidades - Subtotal: $", subtotal_categoria)
        print("\nTotal de la compra:", subtotal_total)
    elif opcion == 3:
        print("Saliendo del sistema. ¡Gracias por su compra!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")


