# Calcular la serie de Fibonacci (Función recursiva

def fibonacci(numero):
    if numero <= 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

numero = int (input ("Ingrese el numero maximo de repeticiones: "))
for i in range(numero):
    resultado = fibonacci(i)
    print(resultado, end=" ")
    # Richard Soria, Josué Guerra, Carlos Pérez
