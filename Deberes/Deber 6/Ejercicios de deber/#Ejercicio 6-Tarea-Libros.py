# Ejercicio 6
# Pedir al usuario los títulos de libros
# Ejercicio echo por Josué Guerra

print("Ejercicio 6: Conteo de dígitos numéricos en títulos de libros")

lineas_completas = 0
digitos_totales = 0
print(" Use * para acabar y muestre las lineas completas")
print(" Use / para ver los dígitos númericos de un título")
while True:
    titulo = input("Libro: ")

    if titulo == "*":
        break
    elif titulo == "/":
        print("Línea completa. Aparecen", digitos_totales, "dígitos numéricos.")
        lineas_completas += 1
        digitos_totales = 0
    else:
        digitos_totales += sum(1 for caracter in titulo if caracter.isdigit())
print("Fin. Se leyeron", lineas_completas, "líneas completas.")
