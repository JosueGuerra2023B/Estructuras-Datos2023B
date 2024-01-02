# Ejercicio 3
# Pedir al usuario un NÚMERO DEL MENU
# Ejercicio echo por Carlos Perez

print("Ejercicio 3: Menu")
aux = 0
while aux != 3:
    print ("---Bienvenido---")
    print ("1. Comenzar programa")
    print ("2. Imprimir Listado")
    print ("3. Finalizar programa")
    aux = int (input ("Ingresa tu seleccion: "))
    if aux != 1 and aux != 2 and aux != 3:
        print ("Seleccion invalida")
    elif aux == 1:
        print ("El programa se esta iniciando...")
    elif aux == 2:
        print ("1, 2, 3 , 4 , 5, 6, 7, 8, 9, 10")