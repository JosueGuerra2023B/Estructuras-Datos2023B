#Ejercicio 9
#Ejercicio echo por Josué Guerra
num_empleados = int(input("Ingrese el número de empleados:\n "))
num_profesores = 0
total_horas_trabajadas = 0
totsueldo = 0
total_sueldo_profesores = 0
total_sueldo_no_profesores = 0

for i in range(1, num_empleados + 1):
    print(f"\nEmpleado {i}:")
    horas_trabajadas = int(input("Ingrese el número de horas trabajadas: \n"))
    print(" Es profesor ")
    es_profesor = input("Si (1) | no(2) ): ").upper() == '1'
    sueldo = float(input("Inserte el sueldo del empleado: \n"))
    total_horas_trabajadas += horas_trabajadas
    totsueldo += sueldo
    if es_profesor:
        num_profesores += 1
        total_sueldo_profesores += sueldo
    else:
        total_sueldo_no_profesores += sueldo

print("\nNúmero total de profesores: ",num_profesores)
print("Suma total de horas trabajadas: ", total_horas_trabajadas)
print("Suma total de sueldos: ", totsueldo)
print("Suma total de sueldos de profesores: ", total_sueldo_profesores)
print("Suma total de sueldos de no profesores: ", total_sueldo_no_profesores)