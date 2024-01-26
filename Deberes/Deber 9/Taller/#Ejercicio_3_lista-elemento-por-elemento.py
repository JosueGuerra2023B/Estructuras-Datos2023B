# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Imprimir una lista de 5 materias 
# Obtener el tamño de la lista
# Imprimir asignatura por asignatura

nombre = input ("Ingrese su nombre: ")
materias = ["Matematica", "Programacion", "Fisica", "Algoritmos", "Redes"]
print (nombre)
print ("Las materias que usted toma son: \n" ,materias)
print ("La cantidad de materias son: ",(len(materias)))

for materia in materias:
    print (materia)