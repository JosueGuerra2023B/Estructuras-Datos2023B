# Ejercicio 3
# Ejercicio hecho por Josué Guerra

print("Ejercicio 3");
punto1 = int(input("Ingrese el punto inicial: "))
punto2 = int(input("Ingrese el punto final: "))

while punto1 > punto2:
    print("-----------ERROR-----------")
    print("El punto inicial debe ser menor o igual que el final")
    punto1 = int(input("Ingrese el punto inicial: "))
    punto2 = int(input("Ingrese el punto final: "))

# Realiza la sumatoria y muestra la operación en una sola línea
sumatoria = sum(range(punto1, punto2 + 1))
operacion = ' + '.join(map(str, range(punto1, punto2 + 1)))

print(f'La sumatoria de {operacion} es: {sumatoria}')
