# Ejercicio 3
# Pedir al usuario un número
# Ejercicio realizado por Josué Guerra

print("Ejercicio 1: Cantidad de pares o impares")

while True:
    print("El programa se está iniciando...")
    contador_pares = 0
    contador_impares = 0
    while True:
        try:
            numero = int(input("Ingrese un número (1-100): "))
            if 0 <= numero <= 100:
                if numero == 0:
                    break
                contador_pares += numero % 2 == 0
                contador_impares += numero % 2 != 0
            else:
                print("Número fuera del rango permitido (1-100). Inténtelo de nuevo.")                   
        except ValueError:
            print("Por favor, ingrese un número válido.")
    print("\nResumen:")
    print("Cantidad de números pares:", contador_pares)
    print("Cantidad de números impares:", contador_impares)
    if numero == 0:
        print("Finalizando programa")
        break
