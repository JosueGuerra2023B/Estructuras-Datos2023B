# Ejercicio 8C del deber
# Días de la semana 

dia = int(input("Ingrese un día de la semana del 1 al 7: "))

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

if 1 <= dia <= 7:
    print(f"Es {dias[dia - 1]}")
else:
    print("La semana solo tiene 7 días...")

print("Programa echo por Josue Eduard Guerra Lovato")