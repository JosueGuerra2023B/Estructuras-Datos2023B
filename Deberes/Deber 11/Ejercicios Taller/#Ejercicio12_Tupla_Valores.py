# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
# Crear la tupla con valores del 1 al 10
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
indice = int(input("Ingrese un índice entre 0 y 9: "))

if 0 <= indice < len(tupla):
    print("El valor en el índice", indice, "es:", tupla[indice])
else:
    print("Índice fuera de rango.")
