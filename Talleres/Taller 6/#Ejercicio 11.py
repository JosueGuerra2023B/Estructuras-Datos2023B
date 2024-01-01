#Ejercicio 11
#Ejercicio echo por Josué Guerra
print("-------------PRODUBANCO---------------")
print("Bienvenido al sistema")
print("Inserte sus credenciales")
usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")
# RECUERDE INSERTAR EL USUARIO Y CONTRASEÑA EN LA EJECUCIÓN
while usuario != "Juan" or contraseña != "123":
    print("Incorrecto")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
# Procedimiento
opcion = 0
total = 0
ahorro_anual = 0
while opcion != 4:
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion: "))
    while opcion not in [1, 2, 3, 4]:
        opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        mes = input("Inserte el mes: ")
        cantidad = float(input(f"Ingrese la cantidad a depositar en {mes}: "))
        while cantidad <= 0:
            print("Valor ingresado inválido")
            cantidad = float(input(f"Ingrese la cantidad a depositar en {mes}: "))
        total += cantidad
        ahorro_anual += cantidad
    elif opcion == 2:
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        while cantidad <= 0 or cantidad > total:
            print("Valor ingresado inválido")
            cantidad = float(input("Ingrese la cantidad a retirar: "))
        total -= cantidad
    elif opcion == 3:
        print("Su saldo actual es: ", total)
# Al salir del bucle, mostrar el ahorro anual
print("El ahorro total al final del año es:", ahorro_anual)