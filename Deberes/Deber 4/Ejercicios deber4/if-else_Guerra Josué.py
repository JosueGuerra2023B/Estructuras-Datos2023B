#Ejercicio 2 if-else
#Elaborado por Josué Guerra

#Nota: En la división y el módulo deberá controlar  que el usuario ingrese números diferenetes de cero

while True:
    print("-*-*-*- Bienvenido al sistema de cálculo de operaciones -*-*-*- ")
    print("---/--- Porfavor seleccione la operación que desea realizar ---/--- ")
    print(" 1). Suma ")
    print(" 2). Resta ")
    print(" 3). Multiplicación ")
    print(" 4). División ")
    print(" 5). Potencia ")
    print(" 6). Modulo ")
    op = int (input(" Escoja la opción solo en números: "))
    if op == 1:
         print(" Usted escogio la operación suma ")
         num1 = float (input("Inserte el primer número: "))
         num2 = float (input("Inserte el segundo número: "))
         suma = num1 +num2
         print(" El resultado de la operación es:")
         print(suma)
    elif op == 2:
        print(" Usted escogio la operación resta ")
        num1 = float (input("Inserte el primer número: "))
        num2 = float (input("Inserte el segundo número: "))
        resta = num1 - num2
        print(" El resultado de la operación es:")
        print(resta)
    elif op == 3:
        print(" Usted escogio la operación muutliplicación ")
        num1 = float (input("Inserte el primer número: "))
        num2 = float (input("Inserte el segundo número: "))
        multi = num1 * num2
        print(" El resultado de la operación es:")
        print(multi)
    elif op == 4:
        print(" Usted escogio la operación división ") 
        num1 = float (input("Inserte el primer número: "))
        num2 = float (input("Inserte el segundo número: "))
        if (num2 == 0):
            print("No se puede dividir para 0, inserte un número diferente ")
            num2 = float (input ("Inserte el nuevo número: "))
            divi = num1 / num2
            print(" El resultado de la operación es:")
            print(divi)
        else:
            divi = num1 / num2
            print(" El resultado de la operación es:")
            print(divi)
    elif op == 5:
        print(" Usted escogio la operación potencia ")
        num1 = float (input("Inserte el número: "))
        pot = int (input("Inserte el valor a elevar: "))
        potencia = num1 ** pot
        print(" El resultado de la operación es:")
        print(potencia)
    elif op == 6:
        print(" Usted escogio la operación módulo ")
        num1 = float (input("Inserte el primer número: "))
        num2 = float (input("Inserte el segundo número: "))
        
        if num2 == 0:
            print("No se puede dividir para 0, inserte un número diferente ")
            num2 = float (input ("Inserte el nuevo número: "))
            mod = num1 % num2
            print(" El resultado de la operación es:")
            print(mod)
    else:
        print(" Opción incorrecta")   
    repetir = input("¿Desea escoger nuevamente la operación? ( Yes (y) || No (N) ): ")
    if repetir.lower() != 'y':
        break
print("/-//-/ Gracias por usar nuestro sistema /-//-/")
print("-/--/- Creado por Josué Eduard Guerra Lovato -/--/-")