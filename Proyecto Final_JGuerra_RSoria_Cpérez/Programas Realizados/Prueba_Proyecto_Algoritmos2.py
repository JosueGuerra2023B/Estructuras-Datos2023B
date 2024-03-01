import os
import tkinter as tk
from tkinter import messagebox

def obtener_ruta_escritorio():
    return os.path.join(os.path.expanduser('~'), 'Desktop')

def inicioSesion():
    def validar_ingreso():
        usuario_ingresado = entry_usuario.get()
        contraseña_ingresada = entry_contraseña.get()

        if usuario_ingresado == usuario and contraseña_ingresada == contraseña:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
            ventana_inicio.destroy()
            mostrar_menu_principal()
        else:
            intentos_restantes.set(intentos_restantes.get() - 1)
            if intentos_restantes.get() == 0:
                messagebox.showerror("Inicio de Sesión", "Cuenta bloqueada.")
                ventana_inicio.destroy()
            else:
                messagebox.showwarning("Inicio de Sesión", f"Correo o contraseña incorrectos. Tiene {intentos_restantes.get()} intentos restantes.")

    ventana_inicio = tk.Tk()
    ventana_inicio.title("Inicio de Sesión")
    ventana_inicio.geometry("300x150")

    intentos_restantes = tk.IntVar(value=3)
    usuario = "docente@esfot.edu.ec"
    contraseña = "Docente2023*"

    label_usuario = tk.Label(ventana_inicio, text="Correo electrónico:")
    label_usuario.grid(row=0, column=0, padx=10, pady=5)
    entry_usuario = tk.Entry(ventana_inicio)
    entry_usuario.grid(row=0, column=1, padx=10, pady=5)

    label_contraseña = tk.Label(ventana_inicio, text="Contraseña:")
    label_contraseña.grid(row=1, column=0, padx=10, pady=5)
    entry_contraseña = tk.Entry(ventana_inicio, show="*")
    entry_contraseña.grid(row=1, column=1, padx=10, pady=5)

    boton_ingresar = tk.Button(ventana_inicio, text="Ingresar", command=validar_ingreso)
    boton_ingresar.grid(row=2, column=0, columnspan=2, pady=10)

    ventana_inicio.mainloop()

def mostrar_menu_principal():
    def opcion_registrar_datos():
        ventana_menu.destroy()
        registrarDatos()

    def opcion_ordenar_calificaciones():
        ventana_menu.destroy()
        ordenarCalificaciones()

    def opcion_buscar_calificacion():
        ventana_menu.destroy()
        buscarCalificacion()

    ventana_menu = tk.Tk()
    ventana_menu.title("Menú Principal")

    label_titulo = tk.Label(ventana_menu, text="Menú Principal", font=("Helvetica", 16))
    label_titulo.pack(pady=10)

    boton_registrar_datos = tk.Button(ventana_menu, text="Registrar datos", command=opcion_registrar_datos)
    boton_registrar_datos.pack(pady=5)

    boton_ordenar_calificaciones = tk.Button(ventana_menu, text="Ordenar Calificaciones", command=opcion_ordenar_calificaciones)
    boton_ordenar_calificaciones.pack(pady=5)

    boton_buscar_calificacion = tk.Button(ventana_menu, text="Buscar Calificación", command=opcion_buscar_calificacion)
    boton_buscar_calificacion.pack(pady=5)

    boton_salir = tk.Button(ventana_menu, text="Salir", command=ventana_menu.destroy)
    boton_salir.pack(pady=5)

    ventana_menu.mainloop()

def registrarDatos():
    def guardar_datos():
        nombre_docente = entry_nombre_docente.get()
        num_materias = int(entry_num_materias.get())

        with open(os.path.join(ruta_escritorio, "calificaciones.txt"), "a") as file:
            file.write(f"Profesor: {nombre_docente}\n")
            file.write("Materias:\n")
            for i in range(num_materias):
                materia = entry_materias[i].get()
                file.write(f"- {materia}\n")
                num_estudiantes = int(entry_num_estudiantes[i].get())
                for j in range(num_estudiantes):
                    estudiante = entry_estudiantes[i][j].get()
                    calificacion = entry_calificaciones[i][j].get()
                    file.write(f"- {estudiante}: {calificacion}\n")
            file.write("\n")
        
        messagebox.showinfo("Registro de Datos", "Datos registrados exitosamente.")
        ventana_registrar.destroy()

    ventana_registrar = tk.Tk()
    ventana_registrar.title("Registro de Datos")

    label_nombre_docente = tk.Label(ventana_registrar, text="Nombre del profesor:")
    label_nombre_docente.grid(row=0, column=0, padx=10, pady=5)
    entry_nombre_docente = tk.Entry(ventana_registrar)
    entry_nombre_docente.grid(row=0, column=1, padx=10, pady=5)

    label_num_materias = tk.Label(ventana_registrar, text="Número de materias:")
    label_num_materias.grid(row=1, column=0, padx=10, pady=5)
    entry_num_materias = tk.Entry(ventana_registrar)
    entry_num_materias.grid(row=1, column=1, padx=10, pady=5)

    def agregar_campos_estudiantes():
        num_materias = int(entry_num_materias.get())

        for widget in ventana_registrar.winfo_children():
            widget.destroy()

        label_nombre_docente.grid(row=0, column=0, padx=10, pady=5)
        entry_nombre_docente.grid(row=0, column=1, padx=10, pady=5)
        label_num_materias.grid(row=1, column=0, padx=10, pady=5)
        entry_num_materias.grid(row=1, column=1, padx=10, pady=5)

        label_materias = []
        entry_materias = []
        label_num_estudiantes = []
        entry_num_estudiantes = []
        entry_estudiantes = []
        entry_calificaciones = []

        for i in range(num_materias):
            label_materias.append(tk.Label(ventana_registrar, text=f"Materia {i+1}:"))
            label_materias[i].grid(row=i+2, column=0, padx=10, pady=5)
            entry_materias.append(tk.Entry(ventana_registrar))
            entry_materias[i].grid(row=i+2, column=1, padx=10, pady=5)

            label_num_estudiantes.append(tk.Label(ventana_registrar, text="Número de estudiantes:"))
            label_num_estudiantes[i].grid(row=i+2, column=2, padx=10, pady=5)
            entry_num_estudiantes.append(tk.Entry(ventana_registrar))
            entry_num_estudiantes[i].grid(row=i+2, column=3, padx=10, pady=5)

            entry_estudiantes.append([])
            entry_calificaciones.append([])
            for j in range(3, 3 + 2*int(entry_num_estudiantes[i].get()), 2):
                entry_estudiantes[i].append(tk.Entry(ventana_registrar))
                entry_estudiantes[i][-1].grid(row=i+2, column=j, padx=10, pady=5)
                entry_calificaciones[i].append(tk.Entry(ventana_registrar))
                entry_calificaciones[i][-1].grid(row=i+2, column=j+1, padx=10, pady=5)

        boton_guardar = tk.Button(ventana_registrar, text="Guardar", command=guardar_datos)
        boton_guardar.grid(row=num_materias+3, column=0, columnspan=4, pady=10)

    boton_agregar_campos = tk.Button(ventana_registrar, text="Agregar Campos", command=agregar_campos_estudiantes)
    boton_agregar_campos.grid(row=2, column=2, columnspan=2, padx=10, pady=5)

    ventana_registrar.mainloop()

def ordenarCalificaciones():
    def guardar_ordenamiento():
        opcion = combo_opciones.get()
        calificaciones_ordenadas = []

        if opcion == "Burbuja":
            calificaciones_ordenadas = sorted(calificaciones, key=lambda x: x[1])  # Burbuja
        elif opcion == "Inserción":
            calificaciones_ordenadas = sorted(calificaciones, key=lambda x: x[1])  # Inserción
        elif opcion == "Selección":
            calificaciones_ordenadas = sorted(calificaciones, key=lambda x: x[1])  # Selección
        elif opcion == "MergeSort":
            calificaciones_ordenadas = sorted(calificaciones, key=lambda x: x[1])  # MergeSort
        elif opcion == "QuickSort":
            calificaciones_ordenadas = sorted(calificaciones, key=lambda x: x[1])  # QuickSort

        ruta_escritorio = obtener_ruta_escritorio()
        with open(os.path.join(ruta_escritorio, f"ordenamiento_{opcion}.txt"), "w") as file:
            file.write(f"Calificaciones ordenadas por opción {opcion}:\n")
            for estudiante, calificacion in calificaciones_ordenadas:
                file.write(f"{estudiante}: {calificacion}\n")

        messagebox.showinfo("Ordenamiento de Calificaciones", f"Calificaciones ordenadas por {opcion} y guardadas en {ruta_escritorio}.")

        ventana_ordenar.destroy()

    ventana_ordenar = tk.Tk()
    ventana_ordenar.title("Ordenar Calificaciones")

    combo_opciones = tk.StringVar()
    opciones = ["Burbuja", "Inserción", "Selección", "MergeSort", "QuickSort"]
    combo_opciones.set(opciones[0])

    label_titulo = tk.Label(ventana_ordenar, text="Seleccione un algoritmo de ordenamiento:")
    label_titulo.grid(row=0, column=0, padx=10, pady=5)

    combo_opciones = tk.OptionMenu(ventana_ordenar, combo_opciones, *opciones)
    combo_opciones.grid(row=0, column=1, padx=10, pady=5)

    boton_ordenar = tk.Button(ventana_ordenar, text="Ordenar y Guardar", command=guardar_ordenamiento)
    boton_ordenar.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    ventana_ordenar.mainloop()

def buscarCalificacion():
    def realizar_busqueda():
        calificacion_buscar = float(entry_calificacion.get())
        algoritmo_busqueda = combo_algoritmo.get()

        ruta_escritorio = obtener_ruta_escritorio()
        with open(os.path.join(ruta_escritorio, "calificaciones.txt"), "r") as file:
            lineas = file.readlines()
            encontrada = False
            for linea in lineas:
                if str(calificacion_buscar) in linea:
                    resultados_text.insert(tk.END, linea.strip() + "\n")  # Elimina espacios en blanco alrededor de la línea
                    encontrada = True
            if not encontrada:
                resultados_text.insert(tk.END, "La calificación no se encontró.\n")

    ventana_buscar = tk.Tk()
    ventana_buscar.title("Buscar Calificación")

    label_calificacion = tk.Label(ventana_buscar, text="Calificación a buscar:")
    label_calificacion.grid(row=0, column=0, padx=10, pady=5)
    entry_calificacion = tk.Entry(ventana_buscar)
    entry_calificacion.grid(row=0, column=1, padx=10, pady=5)

    label_algoritmo = tk.Label(ventana_buscar, text="Algoritmo de búsqueda:")
    label_algoritmo.grid(row=1, column=0, padx=10, pady=5)
    combo_algoritmo = tk.StringVar()
    combo_algoritmo.set("Búsqueda Lineal")
    opciones_algoritmos = ["Búsqueda Lineal", "Búsqueda Binaria", "Búsqueda Interpolación"]
    combo_algoritmo = tk.OptionMenu(ventana_buscar, combo_algoritmo, *opciones_algoritmos)
    combo_algoritmo.grid(row=1, column=1, padx=10, pady=5)

    boton_buscar = tk.Button(ventana_buscar, text="Buscar", command=realizar_busqueda)
    boton_buscar.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    resultados_text = tk.Text(ventana_buscar, height=10, width=50)
    resultados_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    ventana_buscar.mainloop()

inicioSesion()
