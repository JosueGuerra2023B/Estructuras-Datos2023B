# Ejercicio 5 
# Ejercicio echo por Carlos Perez

print("Ejercicio 5");
numero = int (input("Ingrese un numero: "))

while numero < 0 or numero == 0:
    print ("Recuerde ingresar un numero positivo")
    numero = int (input("Ingrese un numero: "))

if 10 <= numero <= 100:
     print ("El numero si pertence")
else:
    print ("El numero no pertence")