# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Programa que almacena las asignaturas de un curso 
#en una lista y la muestre por pantalla pide al usuario las notas
print("          --Bienvenido al programa-- ")
asignaturas = []
calificaciones = []

cantidad_asignaturas = int (input ("Ingrese la cantidad de asignaturas que desea ingresar: "))

for materia in range (cantidad_asignaturas):
    materia = input ("Ingrese la asignatura: ")
    nota = (float (input ("Ingrese su calificacion: ")))

    asignaturas.append (materia)
    calificaciones.append (nota)

asignaturas_notas = asignaturas + calificaciones
print ("Las asignaturas con sus notas correspondientes son: ",asignaturas_notas)