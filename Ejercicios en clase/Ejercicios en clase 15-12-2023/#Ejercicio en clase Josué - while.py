#Ejercicio en clase
#Pedir al usuario que inserte un número 


tab = int(input(" Ingrese un número que desea ver la tabla de multiplicar "))
i = 1;
while i<=12:
    multi = tab *i
    print ( tab, " * ", i," = ", multi)
    i +=1 

#Imprimir los números pares hasta el 50
par = 0
while par <= 50:
    print(par)
    par = par + 2           