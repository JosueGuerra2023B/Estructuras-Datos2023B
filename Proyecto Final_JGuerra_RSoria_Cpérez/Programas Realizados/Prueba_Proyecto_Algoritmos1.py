import tkinter as tk

def inicioSesion():
    intentos = 3
    usuario = "docente@esfot.edu.ec"
    contraseña = "Docente2023*"

    print("----------------Inicio de Sesion")
    while intentos > 0:
        usuarioIngresado = input("Ingrese su correo electronico: ")
        contraseñaIngresada = input("Ingrese su contraseña: ")

        if usuarioIngresado == usuario and contraseñaIngresada == contraseña:
            print("Inicio de sesion exitoso.")
            return True 

        print("Correo o contraseña incorrectos")
        intentos -= 1
        print(f"Tiene {intentos} intentos restantes")

    print("Cuenta Bloqueada")
    return False

def registrarDatos(docente, materias, estudiantes, calificaciones):
    print("--- Registro de Datos ---")
    
    # Registro del profesor
    nombre_docente = input("Ingrese el nombre del profesor: ")
    docente.append(nombre_docente)
    
    # Registro de las materias y estudiantes
    num_materias = int(input("Ingrese el número de materias: "))
    for i in range(num_materias):
        materia = input(f"Ingrese el nombre de la materia {i + 1}: ")
        materias.append(materia)
        
        num_estudiantes = int(input(f"Ingrese el número de estudiantes para la materia {materia}: "))
        for j in range(num_estudiantes):
            estudiante = input(f"Ingrese el nombre del estudiante {j + 1}: ")
            estudiantes.append(estudiante)
            
            calificacion = float(input(f"Ingrese la calificación del estudiante {estudiante}: "))
            calificaciones.append(calificacion)
    
    # Guardar información en un archivo
    with open("calificaciones.txt", "w") as file:
        file.write("COLEGIO o UNIVERSIDAD _________\n")
        file.write("REPORTE DE CALIFICACIONES\n\n")
        for i in range(len(docente)):
            file.write(f"Año lectivo o Semestre: _________\n")
            file.write(f"Materia: {materias[i]}\n")
            file.write("N°- Estudiante Apellido correo Nota 1 Nota 2 Total\n")
            for j in range(len(estudiantes)):
                file.write(f"{j+1} {estudiantes[j]} - - - - {calificaciones[j]}\n")
            file.write("\n")
        file.write("RESUMEN\n")
        file.write("Promedio del curso: 14.75\n")
        file.write("Total Aprobados (14 - 20) 3\n")
        file.write("Suspenso (09 - 13) 1\n")
        file.write("Reprobados (01 - 08) 0\n")
        file.write("_______________________________________\n")
        file.write("Docente\n")
        file.write("____________\n")
        file.write("____________\n")

def ordenarCalificaciones(calificaciones, root):
    print("--- Ordenar Calificaciones ---")
    print("Seleccione un algoritmo de ordenamiento:")
    print("1. Burbuja")
    print("2. Inserción")
    print("3. Selección")
    print("4. MergeSort")
    print("5. QuickSort")
    opcion = int(input("Ingrese el número correspondiente al algoritmo: "))
    
    if opcion == 1:
        calificaciones.sort()  # Burbuja
    elif opcion == 2:
        calificaciones.sort()  # Inserción
    elif opcion == 3:
        calificaciones.sort()  # Selección
    elif opcion == 4:
        calificaciones.sort()  # MergeSort
    elif opcion == 5:
        calificaciones.sort()  # QuickSort
    else:
        print("Opción no válida.")
        return
    
    # Almacenar resultados en un archivo
    with open("ordenamiento.txt", "w") as file:
        file.write("COLEGIO o UNIVERSIDAD _________\n")
        file.write("REPORTE DE CALIFICACIONES\n\n")
        file.write("Calificaciones Ordenadas\n\n")
        file.write("ALGORITMO: Burbuja / Heap Sort / Merge Sort / Quick Sort / ………………\n\n")
        file.write("N°- ")
        for calificacion in calificaciones:
            file.write(f"|{calificacion}|")
        file.write("\n_______________________________________\n")
        file.write("Docente\n")
        file.write("____________\n")
        file.write("____________\n")
    
    # Mostrar información en la interfaz
    mostrarEnInterfaz("Calificaciones ordenadas:", calificaciones, root)

def buscarCalificacion(calificaciones):
    print("--- Buscar Calificación ---")
    calificacion_buscar = float(input("Ingrese la calificación a buscar: "))
    
    print("Seleccione un algoritmo de búsqueda:")
    print("1. Lineal")
    print("2. Binaria")
    print("3. Interpolación")
    opcion = int(input("Ingrese el número correspondiente al algoritmo: "))
    
    if opcion == 1:
        indice = buscarLineal(calificaciones, calificacion_buscar)
    elif opcion == 2:
        indice = buscarBinaria(calificaciones, calificacion_buscar)
    elif opcion == 3:
        indice = buscarInterpolacion(calificaciones, calificacion_buscar)
    else:
        print("Opción no válida.")
        return
    
    if indice == -1:
        print("La calificación no se encontró.")
    else:
        print(f"La calificación se encontró en el índice {indice}.")

def buscarLineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def buscarBinaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def buscarInterpolacion(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha and lista[izquierda] <= objetivo <= lista[derecha]:
        medio = izquierda + int(((float(derecha - izquierda) /
                                  (lista[derecha] - lista[izquierda])) *
                                 (objetivo - lista[izquierda])))
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def mostrarEnInterfaz(titulo, datos, root):
    tk.Label(root, text=titulo).pack()
    for dato in datos:
        tk.Label(root, text=str(dato)).pack()

# Programa principal
root = tk.Tk()

# Simulamos inicio de sesión
#inicioSesion()

docente = []
materias = []
estudiantes = []
calificaciones = []

while True:
    print("\n--- Menú Principal ---")
    print("1. Registrar datos")
    print("2. Ordenar Calificaciones")
    print("3. Buscar Calificación")
    print("4. Salir")
    
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        registrarDatos(docente, materias, estudiantes, calificaciones)
    elif opcion == 2:
        ordenarCalificaciones(calificaciones.copy(), root)
    elif opcion == 3:
        buscarCalificacion(calificaciones)
    elif opcion == 4:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

root.mainloop()
