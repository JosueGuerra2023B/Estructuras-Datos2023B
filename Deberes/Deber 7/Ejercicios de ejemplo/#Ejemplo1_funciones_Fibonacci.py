#Ejercicio echo por Josué Guerra
#Serie de fibonacci
def fibonacci(n, opcion):
    if n <= 0:
        return []
    secuencia = [0, 1]
    if opcion == 1:
        while secuencia[-1] + secuencia[-2] <= n:
            termino = secuencia[-1] + secuencia[-2]
            secuencia.append(termino)
    else:
        while len(secuencia) < n:
            termino = secuencia[-1] + secuencia[-2]
            secuencia.append(termino)

    return secuencia
print("-- Bienvenido al programa --")
print(" serie de Fibonacci")
numero = int(input(" Ingrese un número para la secuencia: "))
while True:
    print(" Menú:")
    print(" 1. Continuar desde el número proporcionado.")
    print(" 2. Generar los primeros n términos.")
    print(" 3. Salir del programa ")
    opcion = int(input("Seleccione una opción : "))

    if opcion == 3:
        print("Gracias por usar el sistema")
        break;
    
    resultado = fibonacci(numero, opcion)
    print("Secuencia Fibonacci:", resultado)
