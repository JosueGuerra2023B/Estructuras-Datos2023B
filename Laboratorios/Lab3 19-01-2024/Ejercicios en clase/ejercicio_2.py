# Determinar la suma de las coordenadas de salida, dado que un usuario ingresa las mismas por teclado
def calcularCoordenadas(x,y):
    x += 12
    y += 15
    suma = x+y
    return suma

x = int(input("Ingrese el valor de la coordenada x: "))
y = int(input("Ingrese el valor de la coordenada y: "))

print("La suma de las coordenas", x, y, "es:", calcularCoordenadas(x,y))

# Richard Soria, Josué Guerra, Carlos Pérez