#Ejercio Josué Guerra
#Programa que pide al usuario los números 
#para sumarlos hasta que ingrese 0

sum = 0 
num = 1
cont = 0
cont1 = 0

print("Ingrese los números para sumar ")
print(" Si ingresa el número 0 el programa realizara los cálculos ")

while num != 0:
    num = float(input("Ingrese el número: "))
    sum = sum + num 
    cont += 1
    print("La suma del número es: ", sum)
tot = sum/(cont-1)
print ("El promedio es de: ", round(tot,2))

