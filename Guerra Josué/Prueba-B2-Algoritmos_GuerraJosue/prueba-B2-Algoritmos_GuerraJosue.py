#Prueba Guerra Josue
import random

def generar_codigo():
    return random.randint(1000, 9999)

def ingresar_datos_cliente():
    print("\nIngresar los datos del cliente")
    nombre = input("Nombre:   ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    return nombre, apellido, telefono

def ingresar_datos_policrush():
    print("\nIngresar los datos del PoliCrush")
    nombreCrush = input("Nombre:   ")
    facultadCrush = input("Facultad de tu Crush: ")
    telefonoCrush = input("Teléfono: ")
    return nombreCrush, facultadCrush, telefonoCrush

def registrar_pedido(pedidos):
    nombre, apellido, telefono = ingresar_datos_cliente()
    nombreCrush, facultadCrush, telefonoCrush = ingresar_datos_policrush()

    print("\nSelección del regalo")
    print("1. Poliflor + Polipeluche = $2.50")
    print("2. Poliflor + Policarta   = $1.50")
    print("3. Poliflor + Polillavero = $2.00")
    print("4. Poliflor + Polivaso    = $2.75")
    detalle = int(input("Selecciona el detalle: "))
    if detalle < 1 or detalle > 4:
#Guerra Josue
        print("Opción inválida.")
        return
    
    costo = {1: 2.5, 2: 1.5, 3: 2.0, 4: 2.75}[detalle]
    costo_total = costo * 1.10
    codigo_pedido = generar_codigo()
    pedidos[codigo_pedido] = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Teléfono": telefono,
        "NombreCrush": nombreCrush,
        "FacultadCrush": facultadCrush,
        "TeléfonoCrush": telefonoCrush,
        "Detalle": detalle,
        "Costo Total": costo_total
    }
    print("\nCódigo de pedido:", codigo_pedido)
    print("----------Pedido registrado con éxito----------\n")

def visualizar_pedidos(pedidos):
    if not pedidos:
        print("\n-------------------------------")
        print("No existen pedidos registrados.")
        print("-------------------------------\n")
        return
    print("\n//--//--//Lista de pedidos//--//--//")
    detalle_pedidos = 1
    for codigo, pedido in pedidos.items():
#Guerra Josue
        print("\nDetalle del pedido", detalle_pedidos, ":")
        print("\nDatos del Cliente")
        print("                    | Nombre:", pedido['Nombre'])
        print("                    | Apellido:", pedido['Apellido'])
        print("                    | Teléfono:", pedido['Teléfono'])
        print("\nDatos de la entrega")
        print("                    | Nombre del Crush:", pedido['NombreCrush'])
        print("                    | Facultad del Crush:", pedido['FacultadCrush'])
        print("                    | Teléfono del Crush:", pedido['TeléfonoCrush'])
        print("\nDatos del pago:")
        print("                    | Código del pedido:", codigo)
        print("                    | Detalle:", pedido["Detalle"])
        print("                    | Costo Total:", round(pedido["Costo Total"], 3))
        print("---------------------------------------")
        print("---------------------------------------------")
        print(" ")
        detalle_pedidos += 1

def visualizar_detalle_pedido(pedidos):
    print("\nDetalle del pedido:")
    codigo = int(input("Ingrese el código del pedido: "))
    if codigo not in pedidos:
        print("\n-------------------------------")
        print("Pedido no encontrado.")
        print("-------------------------------\n")
        return
    pedido = pedidos[codigo]
    print("Pedido encontrado.")
    print("\nDatos del pago:")
#Guerra Josue
    print("Código del pedido:", codigo)
    print("Detalle:", pedido["Detalle"])
    print("Costo Total:", pedido["Costo Total"])
    print("\nDatos del Cliente")
    print("                    | Nombre:", pedido['Nombre'])
    print("                    | Apellido:", pedido['Apellido'])
    print("                    | Teléfono:", pedido['Teléfono'])
    print("\nDatos de la entrega")
    print("                    | Nombre del Crush:", pedido['NombreCrush'])
    print("                    | Facultad del Crush:", pedido['FacultadCrush'])
    print("                    | Teléfono del Crush:", pedido['TeléfonoCrush'])
    print("---------------------------------------")
    print("---------------------------------------------")
    print(" ")


# Función principal del sistema
def sistema_pedido():
    pedidos = {}
    while True:
        print("\n---------Mi POLICRUSH----------\n")
        print("                    ***Bienvenido(a)")
        print("\n¿Qué acción desea realizar?:")
        print("1) Registrar nuevo pedido")
        print("2) Visualizar todos los pedidos")
        print("3) Visualizar detalle de un pedido")
        print("4) Salir del sistema")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            registrar_pedido(pedidos)
        elif opcion == 2:
            visualizar_pedidos(pedidos)
        elif opcion == 3:
            visualizar_detalle_pedido(pedidos)
        elif opcion == 4:
            print("Gracias por usar nuestro sistema\nTu pedido sera enviado")
            print("\nSaliendo del sistema...")
            break
        else:
#Guerra Josue
            print("\nOpción inválida. Por favor, seleccione una opción válida.")

sistema_pedido()
