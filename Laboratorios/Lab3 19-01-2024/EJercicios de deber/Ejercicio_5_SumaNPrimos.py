# Solicitar al usuario el ingreso de números primos. 
# La lectura finalizará cuando ingrese un número que no sea primo. 
# Por cada número, mostrar la suma de sus dígitos. 
# También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
# Al finalizar el programa, mostrar el factorial del mayor número ingresado.?   
# import math

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True    

def digit_frequency(num, digit):
    count = 0
    for i in str(num):
        if i == digit:
            count += 1
    return count

def digit_sum(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Lectura de números primos
nums = []
while True:
    num = int(input("Ingrese un número primo (ingrese un número no primo para finalizar): "))
    if is_prime(num):
        nums.append(num)
    else:
        break

# Lectura de dígito y frecuencia
digit = input("Ingrese un dígito para ver su frecuencia en los números ingresados: ")
max_num = max(nums)

# Mostrar resultados
for num in nums:
    print("Número:", num, "suma de dígitos:", digit_sum(num))
    print("Frecuencia del dígito", digit, "en el número", num, ":", digit_frequency(num, digit))

print("Factorial del mayor número ingresado (", max_num, "):", factorial(max_num))                                                                  
# Richard Soria, Josué Guerra, Carlos Pérez
