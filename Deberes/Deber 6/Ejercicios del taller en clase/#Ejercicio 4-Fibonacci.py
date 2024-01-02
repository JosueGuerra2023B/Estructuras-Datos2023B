# Ejercicio 7: Serie de Fibonacci /Josué Guerra
# Pedir al usuario n números
# Se mostrará hasta ese número o el anterior si es el caso
print("Ejercicio 7: Serie de Fibonacci\n")
n = 1597; a, b = 0, 1
serie = [a]
while a <= n:
    a, b = b, a + b
    serie.append(a)
print("Serie de Fibonacci hasta", n, ":", *serie, sep=", ")



