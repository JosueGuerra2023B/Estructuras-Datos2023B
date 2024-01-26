# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Escribir un programa que almacene las asignaturas 
#de un curso (por ejemplo: Base de Datos, Programación, 
#Matemáticas, Algoritmos, Análisis y Lengua) en una lista, 
#pregunte al usuario la nota que ha sacado en cada asignatura 
#y elimine de la lista las asignaturas aprobadas. Al final el 
#programa debe mostrar por pantalla las asignaturas que el 
#usuario tiene que repetir.

asignaturas = ["Base de Datos", "Programación", "Matemáticas", "Algoritmos", "Análisis", "Lengua"]
tamanio_asignaturas = len(asignaturas)
notas = []
nota = 0
materias_reprobadas =  []
for asignatura in asignaturas:
    while(True):
        nota = float(input("Ingrese la nota de la asignatura de "+asignatura+" : "))
        if (nota<=20 and nota>=1):
            notas.append(nota)
            break
        else:
            print("Ingrese una nota válida.")
tamanio_notas = len(notas)
for i in range(0,tamanio_notas):
    if (notas[i]<14):
        materias_reprobadas.append(asignaturas[i])
        
print("Las asignaturas a repetir por parte del estudiante son:", materias_reprobadas)