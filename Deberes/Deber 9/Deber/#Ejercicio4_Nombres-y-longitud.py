# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Crea dos arrays unidimensionales que 
#tengan el mismo tamaño (lo pedirá por teclado), 
# en uno de ellos almacena nombres de personas 
#como cadenas, en el otro array se almacena la longitud de los nombres.

tamaño = int (input ("Ingrese el tamaño que desea para el arreglo: "))

nombres = []
logintud_nombres = []

for nombre in range (tamaño):
    nombre = input ("Ingresa un nombre: ")
    nombres.append (nombre)
    logintud_nombres.append (len(nombre))

print ("Los nombres son: ",nombres)
print ("La logintud de los nombres es: ",logintud_nombres)