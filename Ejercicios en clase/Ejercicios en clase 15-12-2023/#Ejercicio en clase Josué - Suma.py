#Ejercio Josué Guerra
#Programa que pide al usuario los números 
#para sumarlos hasta que ingrese 0

sum = 0 
num = 1

print("Ingrese los números para sumar ")
print(" Si ingresa el número 0 el programa realizara los cálculos ")

while num != 0:
    num = int(input("Ingrese el número: "))
    sum = sum + num 
    print("La suma del número es: ", sum)
print ("La suma de los cálculos es: ",sum)

     
   

