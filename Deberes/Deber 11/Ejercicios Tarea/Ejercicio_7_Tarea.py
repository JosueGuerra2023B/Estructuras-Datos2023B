# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
cantidad_compra = 0
factura = 1
base_compras = []


def registrarCompra(base_compras, cantidad_compra):
    global factura
    print("*****NUEVA COMPRA****")
    cantidad_compra += 1
    print ("Ingrese los datos del cliente:")
    for i in range(cantidad_compra):
        detallesCompras = []
        detallesCompras.insert(0,factura)
        factura += 1
        nombre_cliente = str(input("Ingrese el nombre: "))
        detallesCompras.insert(1, nombre_cliente)
        apellido_cliente = str(input("Ingrese el apellido: "))
        detallesCompras.insert(2, apellido_cliente)
        telefono_cliente = int(input("Ingrese el teléfono: "))
        detallesCompras.insert(3, telefono_cliente)
        correo_cliente = str(input("Ingrese el correo: "))
        detallesCompras.insert(4, correo_cliente)
        print ("Ingrese los datos de la persona a quién desea enviar el regalo:")
        nombre_envio = str(input("Ingrese el nombre de envío: "))
        detallesCompras.insert(5, nombre_envio)
        apellido_envio = str(input("Ingrese el apellido de envío: "))
        detallesCompras.insert(6, apellido_envio)
        telefono_envio = int(input("Ingrese el teléfono de envío: "))
        detallesCompras.insert(7, telefono_envio)
        while (True):
            print ("Seleccione el paquete:")
            print ("1) Flores + peluche costo $15.50")
            print ("2) Flores + carta costo $7.50")
            print ("3) Flores + chocolates costo $12.25")
            print ("4) Flores + perfume costo $22.75")
            paquete = int(input("Seleccione una opción: "))

            if (paquete==1):
                paquete = "Flores + peluche"
                detallesCompras.insert(8, paquete)
                precio = 15.50
                detallesCompras.insert(9, precio)
                break            
            elif (paquete==2):
                paquete = "Flores + carta"
                detallesCompras.insert(8, paquete)
                precio = 7.50
                detallesCompras.insert(9, precio)
                break            
            elif (paquete==3):
                paquete = "Flores + chocolates"
                detallesCompras.insert(8, paquete)
                precio = 12.25
                detallesCompras.insert(9, precio)
                break
            elif (paquete==4):
                paquete = "Flores + perfume"
                detallesCompras.insert(8, paquete)
                precio = 22.75
                detallesCompras.insert(9, precio)
                break 
            else:
                print ("Ingrese un paquete de los disponibles")
        print("Compra registrada con éxito.")
        base_compras.append(detallesCompras)
        
def mostrarCompra(base_compras):
    if len(base_compras) > 0:
        print("*****COMPRAS REGISTRADAS****")
        for indice, compra in enumerate(base_compras, start=1):
            print("Compra Registrada 0 0 0", indice)
            print("Número de factura 0 0 0 0 0 0", compra[0])
            print("Datos del cliente:")
            print("Nombre:", compra[1])
            print("Apellido:", compra[2])
            print("Teléfono:", compra[3])
            print("Correo:", compra[4])
            print("Datos de la entrega:")
            print("Nombre:", compra[5])
            print("Apellido:", compra[6])
            print("Teléfono:", compra[7])
            print("Paquete seleccionado:", compra[8])
            print("Precio:", compra[9])
            print("Compra registrada con éxito.")
            print() 
    else:
        print("No se ha registrado ninguna compra todavía, intente realizar una compra.")

def mostrarDetallesCompra(base_compras):
    if len(base_compras) > 0:
        buscarFactura = int(input("Ingrese la factura a buscar, solo debe indicar las cifras significativas: "))
        for compra in base_compras:
            if (compra[0] == buscarFactura):
                print("*****DETALLES DE LA COMPRA****")
                print("Compra Registrada 0 0 0", buscarFactura)
                print("Factura 0 0 0 0 0 0", buscarFactura)
                print("Datos del cliente:")
                print("Nombre:", compra[1])
                print("Apellido:", compra[2])
                print("Teléfono:", compra[3])
                print("Correo:", compra[4])
                print("Datos de la entrega:")
                print("Nombre:", compra[5])
                print("Apellido:", compra[6])
                print("Teléfono:", compra[7])
                print("Paquete seleccionado:", compra[8])
                print("Precio final a pagar:", compra[9])
                print("Compra registrada con éxito.")
                print() 
                break
        else:
            print("Factura no encontrada. Intente de nuevo.")
    else:
        print("No se ha registrado ninguna compra todavía, intente realizar una compra.")


print ("*****RAPID****")
print ("Bienvenido a Rapid") 
print ("¿QuÉ opción desea realizar?")
print ("1. Registrar compra")
print ("2. Mostrar compra")
print ("3. Mostrar el detalle de la compra")
print ("4. Salir")

while (True):
    opcion = int(input("Ingrese la opción a realizar: "))
    match opcion:
        case 1:
            
            registrarCompra(base_compras, cantidad_compra)
        case 2:

            mostrarCompra(base_compras)
        case 3:
            
            mostrarDetallesCompra(base_compras)
        case 4:
            print("Regrese pronto")
            break