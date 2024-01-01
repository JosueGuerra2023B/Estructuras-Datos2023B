# Ejercicio 4
# Ejercicio hecho por Carlos Perez

print("Ejercicio 4");
while True:
    print("--//--// Fe y Alegría \\\--\\\--")
    print(" ")
    nombre = input("Inserte su nombre: \n")
    materia = input("Inserte la materia: \n") 
    suma_calificaciones = 0
    for i in range(4):
        calificacion = float(input("Ingrese su calificación sobre 20: "))
        suma_calificaciones += calificacion
    print("La suma de las calificaciones para", materia, "es: ", suma_calificaciones, "")
    promedio = suma_calificaciones / 4
    print("El promedio de sus calificaciones es: ", promedio, "")
    if promedio >= 14:
        print("Estimado ", nombre, "Usted está Aprobado")
    elif 13 >= promedio >= 9:
        print("Estimado ", nombre, "Usted está en Supletorio")
    elif 8 >= promedio:
        print("Rechazado")
    print("¿Desea ingresar otra materia?")
    op = input("SI-(1) | NO-(2): ")
    if op != '1':
        break

