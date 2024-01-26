# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Inicialice el siguiente arreglo de números: [1, 2, 5, 8, 3, 4, 30, 9, 13] 
# Imprima en pantalla programáticamente los números impares mayores a 3.

numeros = [1, 2, 5, 8, 3, 4, 30, 9, 13]

print ("La cadena es: ",numeros)
print ("Los numeros impares mayores a 3 son: ")

for numero in numeros:
    if numero > 3 and numero % 2 != 0:
        print(numero)