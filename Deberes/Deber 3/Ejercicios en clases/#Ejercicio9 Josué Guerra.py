#Ejercicio 9
#Ingreso de notas

num1 = float(input(" Ingrese la nota de Ingles: "))
num2 = float(input(" Ingrese la nota de Programación: "))
num3 = float(input(" Ingrese la nota de Algoritmos: "))

promedio = (num1 + num2 + num3) / 3
print("Su promedio es de", round(promedio,2))
if(promedio >= 9 and promedio <= 10):
        print(" Felicidades usted aprobo el curso ")
        print(" Usted se ha ganado una beca en Masachusets ")
elif(promedio >= 7 and promedio <= 8):
        print(" Felicitaciones usted aprobo el curso ")
elif(promedio > 10):
    print(" //Usted se ha salido del rango de nota// ")
    print(" //Porfavor ingrese las notas dentro del rango de 10// ")
else:
    promedio <= 7 
    print("Lo sentimos usted reporobo el curso con una nota de: ", (promedio,2))