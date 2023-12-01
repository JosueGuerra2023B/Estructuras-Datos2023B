# Ejercicio 7C del deber
# Paquetes de compañia

l =input(" Inserte su nombre: ")
print("---Bienvenido", l, "a nuestras aerolineas--- ")
print("---Seleccione su paquete de vuelo---")
print("1. América del Norte")
print("2. América Central")
print("3. América del Sur")
print("4. Europa")
print("5. Asia")

opcion = int(input("Ingrese su selección: "))
peso = int(input("Ingrese el peso del paquete en gramos: "))

if peso >= 5000:
    print("Lo sentimos, el paquete es muy pesado...")
elif 1 <= opcion <= 5:
    costos_por_kilo = [0, 24, 20, 21, 10, 18]
    valor = peso * costos_por_kilo[opcion]
    print(f"El costo es de {valor}")
else:
    print("Opción inválida...")

print("Programa echo por Josue Eduard Guerra Lovato")