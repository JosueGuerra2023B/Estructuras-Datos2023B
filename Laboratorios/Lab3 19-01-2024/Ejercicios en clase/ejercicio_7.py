#Escribir una función que, dado un número de DNI, retorne True si el número es 
#válido y False si no lo es. Para que un número de DNI sea válido debe tener 10 dígitos.

def validarDNI(dni):
    cantidad = 0
    while(dni != 0):  
        dni //= 10
        cantidad += 1
    return cantidad==10
    
dni = int(input("Ingrese su dni: "))
print(validarDNI(dni))

# Richard Soria, Josué Guerra, Carlos Pérez