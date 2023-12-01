# Ejercicio 9C del deber
# Programa de calculos

opcion = int(input("Ingrese el tipo de motor (1, 2, 3, 4): "))

if 1 <= opcion <= 4:
    tipos_bomba = ["agua", "gasolina", "hormigón", "pasta alimenticia"]
    print(f"La bomba es una bomba de {tipos_bomba[opcion - 1]}.")
else:
    print("No hay un valor válido para el tipo de bomba.")

print("Programa echo por Josue Eduard Guerra Lovato")