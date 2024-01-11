#Ejercicio echo por Josué Guerra
#Suma de dos números
def suma(a, b):
    resultado = a + b
    return resultado

print("-- Bienvenido al programa --")
print(" Suma de dos números ")
a = float(input("Inserte el primer número: "))
b = float(input("Inserte el primer número: "))
resultado_suma = suma(a, b)
print("El resultado de la suma es: ", resultado_suma) 
