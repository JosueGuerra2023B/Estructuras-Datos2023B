import os

def obtener_ruta_escritorio():
    return os.path.join(os.path.expanduser('~'), 'Desktop')

def inicioSesion():
    intentos = 3
    usuario = "docente@esfot.edu.ec"
    contraseña = "Docente2023*"

    print("----------------Inicio de Sesion")
    while intentos > 0:
        usuarioIngresado = input("Ingrese su correo electrónico: ")
        contraseñaIngresada = input("Ingrese su contraseña: ")

        if usuarioIngresado == usuario and contraseñaIngresada == contraseña:
            print("Inicio de sesión exitoso.")
            return True 

        print("Correo o contraseña incorrectos")
        intentos -= 1
        print(f"Tiene {intentos} intentos restantes")

    print("Cuenta Bloqueada")
    return False


def registrarDatos():
    print("--- Registro de Datos ---")
    docente = []
    materias = []
    estudiantes = []
    calificaciones = []

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
    ruta_escritorio = obtener_ruta_escritorio()
    with open(os.path.join(ruta_escritorio, "calificaciones.txt"), "a") as file:
        file.write(f"Profesor: {nombre_docente}\n")
        file.write("Materias:\n")
        for materia in materias:
            file.write(f"- {materia}\n")
        file.write("Estudiantes y Calificaciones:\n")
        for estudiante, calificacion in zip (estudiantes, calificaciones ):
            file.write(f"- {estudiante}: {calificacion}\n")
        file.write("\n")

# Funciones de los algoritmos de ordenamiento

def burbuja(calificaciones):
    n = len(calificaciones)
    for i in range(n):
        for j in range(0, n-i-1):
            if calificaciones[j][1] > calificaciones[j+1][1]:
                calificaciones[j], calificaciones[j+1] = calificaciones[j+1], calificaciones[j]
    return calificaciones

def insercion(calificaciones):
    for i in range(1, len(calificaciones)):
        elemento_actual = calificaciones[i]
        j = i-1
        while j >=0 and elemento_actual[1] < calificaciones[j][1] :
                calificaciones[j+1] = calificaciones[j]
                j -= 1
        calificaciones[j+1] = elemento_actual
    return calificaciones

def seleccion(calificaciones):
    for i in range(len(calificaciones)):
        minimo = i
        for j in range(i+1, len(calificaciones)):
            if calificaciones[minimo][1] > calificaciones[j][1]:
                minimo = j
        calificaciones[i], calificaciones[minimo] = calificaciones[minimo], calificaciones[i]
    return calificaciones

def mergeSort(calificaciones):
    if len(calificaciones) >1:
        mitad = len(calificaciones)//2
        mitad_1 = calificaciones[:mitad]
        mitad_2 = calificaciones[mitad:]
        mergeSort(mitad_1)
        mergeSort(mitad_2)
        i = j = k = 0
        while i < len(mitad_1) and j < len(mitad_2):
            if mitad_1[i][1] < mitad_2[j][1]:
                calificaciones[k] = mitad_1[i]
                i+=1
            else:
                calificaciones[k] = mitad_2[j]
                j+=1
            k+=1
        while i < len(mitad_1):
            calificaciones[k] = mitad_1[i]
            i+=1
            k+=1
        while j < len(mitad_2):
            calificaciones[k] = mitad_2[j]
            j+=1
            k+=1
    return calificaciones

def particion(calificaciones, inferior, superior):
    i = (inferior-1)
    pivote = calificaciones[superior][1]
    for j in range(inferior, superior):
        if calificaciones[j][1] <= pivote:
            i = i+1
            calificaciones[i], calificaciones[j] = calificaciones[j], calificaciones[i]
    calificaciones[i+1], calificaciones[superior] = calificaciones[inferior], calificaciones[i+1]
    return (i+1)

def quickSort(calificaciones):
    if len(calificaciones) <= 1:
        return calificaciones
    pivot = calificaciones[len(calificaciones) // 2]
    izquierda = [i for i in calificaciones if i < pivot]
    medio = [i for i in calificaciones if i == pivot]
    derecha = [i for i in calificaciones if i > pivot]
    return quickSort(izquierda) + medio + quickSort(derecha)


def ordenarCalificaciones(calificaciones):
    print("--- Ordenar Calificaciones ---")
    print("Seleccione un algoritmo de ordenamiento:")
    print("1. Burbuja")
    print("2. Inserción")
    print("3. Selección")
    print("4. MergeSort")
    print("5. QuickSort")
    opcion = int(input("Ingrese el tipo de ordenamiento que desea: "))

    if opcion == 1:
        opcion = "Burbuja"
        calificaciones_ordenadas = burbuja(calificaciones)
    elif opcion == 2:
        opcion = "Inserción"
        calificaciones_ordenadas = insercion(calificaciones)
    elif opcion == 3:
        opcion = "Selección"
        calificaciones_ordenadas = seleccion(calificaciones)
    elif opcion == 4:
        opcion = "MergeSort"
        calificaciones_ordenadas = mergeSort(calificaciones)
    elif opcion == 5:
        opcion = "QuickSort"
        calificaciones_ordenadas = quickSort(calificaciones)
    else:
        print("Opción no válida.")
        return

    # Almacenar resultados en un archivo
    ruta_escritorio = obtener_ruta_escritorio()
    with open(os.path.join(ruta_escritorio, f"ordenamiento_opcion{opcion}.txt"), "w") as file:
        file.write(f"Calificaciones ordenadas por opción {opcion}:\n")
        for estudiante, calificacion in calificaciones_ordenadas:
            file.write(f"{estudiante}: {calificacion}\n")

    # Mostrar información en la consola
    print(f"Calificaciones ordenadas por opción {opcion}:")
    for estudiante, calificacion in calificaciones_ordenadas:
        print(f"{estudiante}: {calificacion}")

def buscarCalificacion():
    print("--- Buscar Calificación ---")
    calificacion_buscar = float(input("Ingrese la calificación a buscar: "))

    print("Seleccione un algoritmo de búsqueda:")
    print("1. Búsqueda Lineal")
    print("2. Búsqueda Binaria")
    print("3. Búsqueda Interpolación")
    opcion = int(input("Ingrese el tipo de algoritmo de búsqueda que desea: "))

    ruta_escritorio = obtener_ruta_escritorio()
    calificaciones = []  # Lista para almacenar las calificaciones
    with open(os.path.join(ruta_escritorio, "calificaciones.txt"), "r") as file:
        lineas = file.readlines()
        for i, linea in enumerate(lineas):
            if "Estudiantes y Calificaciones:" in linea:
                # Recorremos las líneas siguientes para obtener las calificaciones
                for j in range(i + 1, len(lineas)):
                    estudiante_calificacion = lineas[j].strip().split(": ")
                    if len(estudiante_calificacion) == 2:
                        estudiante = estudiante_calificacion[0].strip()
                        calificacion = float(estudiante_calificacion[1].strip())
                        calificaciones.append((estudiante, calificacion))
                    else:
                        break  # Se alcanzó el final de las calificaciones

    # Selección del algoritmo de búsqueda
    if opcion == 1:
        opcion = "Búsqueda Lineal"
        encontrado = busqueda_lineal(calificaciones, calificacion_buscar)
    elif opcion == 2:
        opcion = "Búsqueda Binaria"
        encontrado = busqueda_binaria(calificaciones, calificacion_buscar)
    elif opcion == 3:
        opcion = "Búsqueda Interpolación"
        encontrado = busqueda_interpolacion(calificaciones, calificacion_buscar)
    else:
        print("Opción no válida.")
        return

    # Mostrar el resultado de la búsqueda
    if encontrado:
        print("La calificación se encontró.")
    else:
        print("La calificación no se encontró.")

# Almacenar resultados en un archivo
    with open(os.path.join(ruta_escritorio, "busqueda.txt"), "a") as file:
        file.write(f"Resultado de la búsqueda de la calificación {calificacion_buscar} con el algoritmo {opcion}:\n")
        if encontrado:
            for estudiante, calificacion in calificaciones:
                if calificacion == calificacion_buscar:
                    file.write(f"Estudiante: {estudiante}, Calificación: {calificacion}\n")
                    break
            file.write("Calificación encontrada.\n")
        else:
            file.write("La calificación no se encontró.\n")




# Algoritmo de búsqueda lineal
def busqueda_lineal(calificaciones, calificacion_buscar):
    for estudiante, calificacion in calificaciones:
        if calificacion == calificacion_buscar:
            print(f"Estudiante: {estudiante}, Calificación: {calificacion}")
            return True
    return False

# Algoritmo de búsqueda binaria
def busqueda_binaria(calificaciones, calificacion_buscar):
    calificaciones.sort(key=lambda x: x[1])  # Ordenar la lista de calificaciones por calificación
    inicio = 0
    fin = len(calificaciones) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if calificaciones[medio][1] == calificacion_buscar:
            print(f"Estudiante: {calificaciones[medio][0]}, Calificación: {calificacion_buscar}")
            return True
        elif calificaciones[medio][1] < calificacion_buscar:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False

# Algoritmo de búsqueda por interpolación
def busqueda_interpolacion(calificaciones, calificacion_buscar):
    calificaciones.sort(key=lambda x: x[1])  # Ordenar la lista de calificaciones por calificación
    n = len(calificaciones)
    inicio = 0
    fin = n - 1

    while inicio <= fin and calificaciones[inicio][1] <= calificacion_buscar <= calificaciones[fin][1]:
        # Interpolación para encontrar la posición más probable
        pos = inicio + int((calificacion_buscar - calificaciones[inicio][1]) * (fin - inicio) / (calificaciones[fin][1] - calificaciones[inicio][1]))

        if calificaciones[pos][1] == calificacion_buscar:
            print(f"Estudiante: {calificaciones[pos][0]}, Calificación: {calificacion_buscar}")
            return True
        elif calificaciones[pos][1] < calificacion_buscar:
            inicio = pos + 1
        else:
            fin = pos - 1
    return False


# Nueva función para generar el reporte y guardarlo en un archivo
def generarReporte(calificaciones):
    print("--- Generar Reporte ---")
    print("Estudiante    Calificación    Estado")
    ruta_escritorio = obtener_ruta_escritorio()
    with open(os.path.join(ruta_escritorio, "reporte.txt"), "w") as file:
        file.write("--- Reporte de Calificaciones ---\n")
        file.write("Estudiante    Calificación    Estado\n")
        for estudiante, calificacion in calificaciones:
            estado = ""
            if calificacion >= 14:
                estado = "Aprobado"
            elif calificacion >= 10:
                estado = "Supletorio"
            else:
                estado = "Reprobado"
            file.write(f"{estudiante:<14} {calificacion:<15} {estado}\n")
            print(f"{estudiante:<14} {calificacion:<15} {estado}")

def menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar datos")
    print("2. Ordenar Calificaciones")
    print("3. Buscar Calificación")
    print("4. Generar Reporte")
    print("5. Salir")

if inicioSesion():
    while True:
        menu()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            registrarDatos()
        elif opcion == 2:
            with open(os.path.join(obtener_ruta_escritorio(), "calificaciones.txt"), "r") as file:
                lineas = iter(file.readlines())
                calificaciones = []
                for linea in lineas:
                    if "Estudiantes y Calificaciones:" in linea:
                        while True:
                            try:
                                estudiante_info = next(lineas).strip()
                                if estudiante_info == '':
                                    break
                                estudiante, calificacion = estudiante_info.split(":")
                                calificaciones.append((estudiante.strip(), float(calificacion.strip())))
                            except StopIteration:
                                break
            ordenarCalificaciones(calificaciones.copy())
        elif opcion == 3:
            buscarCalificacion()
        elif opcion == 4:
            generarReporte(calificaciones.copy())  # Generar reporte con las calificaciones actuales
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")