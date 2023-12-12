#Ejercicio de la prueba con switch case
#Echo por Josué Guerra

print("/-/-/- Bienvenido al Carbonero -/-/-/")

print(" Ingrese los datos de la factura ")
nom = input(" Inserte su nombre: ")
ced = input(" Ingrese su N° de cédula: ")
cor = input(" Inserte su correo electrónico: ")

while True:
    print(" Nuestro Menu se compone de ")
    print(" 3 tipos de hamburguesas que son: ")
    print(" 1). Sencilla  -- $1,50 --")
    print(" 2). Doble     -- $2,50 --")
    print(" 3). Triple    -- $3,50 --")
    op = (input(" Por favor seleccione la opción que desea consumir "))
    
    # Calcular el costo total sin cargo adicional
    if 0 < int(op) <= 3:
        cant = int(input("Inserte la cantidad de Hamburguesas: "))
        
        cost = 0
        match op:
            case '1':
                cost = cant * 1.50
            case '2':
                cost = cant * 2.50
            case '3':
                cost = cant * 3.50
            case _:
                print("Tipo de hamburguesa no válida")
                continue

        while True:
            print(" Inserte el metodo de pago ")
            print("1). Tarjeta ")
            print("2). Efectivo ")
            pag = int(input(" Seleccione cualquiera de las dos opciones: "))
            
            match pag:
                case 1:
                    cost += cost * 0.05
                    print(" Usted debe pagar un recargo del 5%")
                case 2:
                    pass
                case _:
                    print("Opción incorrecta, Ingrese nuevamente el metodo de pago")
                    continue

            print("/---/ Gracias por su compra /---/ ")
            print("Estimado/a", nom)
            print("el total de su compra es de:", cost)
            print(" Su factura se le enviará al correo que registró ")
            print("/--/ Esperamos tenerlo de vuelta /--/ ")
            break
        break
    else:
        print(" Opción seleccionada incorrecta, vuelva a seleccionar el tipo de hamburguesa ")
 
print("/-//-/ Gracias por usar nuestro sistema /-//-/")
print("-/--/- Creado por Josué Eduard Guerra Lovato -/--/-")