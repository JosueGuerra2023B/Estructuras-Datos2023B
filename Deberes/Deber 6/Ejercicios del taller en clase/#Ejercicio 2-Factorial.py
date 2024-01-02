# Ejercicio 2: cálculo de factorial
# Pedir al usuario un número
# Realizar el cálculo factorial
# Ejercicio realizado por Carlos Pérez

num = int(input("Ejercicio 4: Cálculo de factorial\nIngrese un número para calcular su factorial: "))

if num < 0:
    print("El factorial no puede ser negativo.")
else:
    factorial = 1
    print(f"Fórmula del factorial: {num}! = ", end="")
    for i in range(1, num + 1):
        print(i, end="")
        if i < num:
            print(" * ", end="")
    print()
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, " es: ",factorial)
