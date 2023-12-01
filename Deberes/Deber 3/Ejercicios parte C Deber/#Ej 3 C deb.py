#Ejercicio 3c del deber
#Numeros en orden 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

numeros_ordenados = sorted([num1, num2, num3], reverse=True)

mayor, medio, menor = numeros_ordenados

print(f"Números ordenados de mayor a menor: {mayor}, {medio}, {menor}")

print("Programa echo por Josue Eduard Guerra Lovato")