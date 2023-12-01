#Ejercicio 5

nombre = input("Ingrese el nombre del estudiante: ")
nota = int(input("Ingrese la nota: "))
if(nota >=7):
    print("Felicitaciones ", nombre, "Usted ha aprobado el curso con una nota de: ", nota)
else:
    print("Lo sentimos ", nombre, "usted ha reprobado el curso curso con una nota de: ", nota)
