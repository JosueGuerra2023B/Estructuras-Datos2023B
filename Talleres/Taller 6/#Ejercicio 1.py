#Ejercicio 1
#Ejercicio echo por Josué Guerra

print("Ejercicio 1");
num = int(input("Inserte un número:\n"));

while num <= 0:
    print("Inserte nuevamente el número")
    print("Debe ser diferente de 0");
    num = int(input("Inserte un número:\n"));

suma = 0; 
par = " "; 
for i in range(2, num+1, 2):
            suma += i
            par += str(i) + " + "
par = par.rstrip(" + ")
print(par)
print("La suma de los primeros pares hasta ", num, " es : ",suma)

