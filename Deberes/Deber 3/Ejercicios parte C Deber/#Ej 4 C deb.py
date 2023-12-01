# Ejercicio 4C del deber
# PTriangulos

A, B, C = sorted(map(float, input("Ingrese las longitudes de los lados separadas por espacios: ").split()))

if A == B == C:
    print("Triángulo equilátero")
elif A == B or B == C or A == C:
    print("Triángulo isósceles")
elif A**2 + B**2 == C**2:
    print("Triángulo rectángulo")
else:
    print("Triángulo escaleno")


print("Programa echo por Josue Eduard Guerra Lovato")