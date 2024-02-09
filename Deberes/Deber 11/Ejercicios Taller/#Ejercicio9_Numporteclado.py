# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
#Contando sin la función
print("\nTupla")
tupla2 = (1, 2, 1, 4, 1, 6, 1, 8, 2, 2, 9, 6, 8, 7, 5)
count = 0
valor = int(input("Ingrese el valor a observar: "))  
for i in tupla2:
    if i == valor:  
        count += 1
print("El elemento" ,valor, " se repite:", count, "veces\n") 
