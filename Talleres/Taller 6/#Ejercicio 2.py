# Ejercicio 2
# Ejercicio hecho por Josué Guerra

print("Ejercicio 2");
while True:
    print("--CHEVROLET--\n")
    print("-*-*-*-//Bienvenido al sistema//-*-*-*-")
    print("-/--- Sensor de fugas ---\-\n")
    correo = input("Inserte su correo: \n")
    print(" ")
    print(" Menu de opciones")
    print(" 1. Verificar los talleres")
    print(" 2. Salir")
    op = float(input("Seleccione la opción a realizar: \n"))

    while op != 1 and op != 2:
        print("Seleccione la opción correcta")
        op = float(input("Seleccione la opción a realizar: \n"))

    if op == 1:
        fugas = 0
        cantidad_talleres = int(input("Inserte la cantidad de talleres: \n"))

        while cantidad_talleres <= 1:
            print("La cantidad de talleres debe ser mayor que 1. Intente nuevamente.")
            cantidad_talleres = int(input("Inserte la cantidad de talleres: \n"))

        talleres = 1
        while talleres <= cantidad_talleres:
            print("¿Hay alguna fuga dentro del taller", talleres, ": ")
            op2 = input("si (S) | no (N): \n")

            if op2.upper() == 'S':
                fugas += 1

            talleres += 1

        if fugas >= 1:
            print(" ")
            print("Se enviará un correo con el informe a \n", correo)
            print("Gracias por usar nuestro sistema")
            print(" ")

    else:
        if op == 2:
            print("Gracias por usar nuestro sistema")
            break

    print("¿Desea ingresar de nuevo?")
    op3 = input("SI-(1) | NO-(2): ")

    if op3 != '1':
        break
