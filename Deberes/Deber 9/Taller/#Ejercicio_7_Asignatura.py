# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Insertar las asignaturas en la lista e imprimirlas.

asignaturas = []

cantidad_asignaturas = int (input ("Ingrese la cantidad de asignaturas a añadir: "))

for materias in range (cantidad_asignaturas):
    materias = (input ("Ingrese la asignatura: "))
    asignaturas.append (materias)

print ("La lista de asignaturas es: ",asignaturas)
for materia in asignaturas:
    print (materia)

