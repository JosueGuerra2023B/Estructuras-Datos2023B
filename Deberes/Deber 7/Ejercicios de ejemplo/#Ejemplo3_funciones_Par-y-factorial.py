#Ejercicio echo por Josué Guerra
#Par y factorial
def factorial(n):
    if n == 0 or n == 1:
        return "1"
    else:
        op = str(n) + " * " + factorial(n - 1)
        return op
    
def par_impar(numero):
    if numero % 2 == 0:
        fact = factorial(numero)
        resultado = str(numero) + "! = " + str(eval(fact))
        return " Tu número es Par\nEl factorial del número es: " + resultado + " = " + fact 
    else:
        return " Tu número es Impar"

print("-- Bienvenido al programa --")
print(" Número par o impar\n y el Factorial del número par ")
print(" Si su número es par en pantalla se mostrara dos características" ) 
n = int(input(" Inserte un número: "))
verificacion = par_impar(n)
print(verificacion)  
