# Dada una temperatura f en grados Fahrenheit, devuelva la temperatura en grados 
# centígrados c, es decir, c = 5(� − 32)/9. Implementa una función.

def gradosC(grados_F):
    grados_celcius = round((5/9)*(grados_F-32),2)
    return grados_celcius

def continuar(opcion):
    while(True):
        if(opcion=="si"):
            return True
        elif(opcion=="no"):
            return exit(0)
        
print("Conversión de grados Fahrenheit a grados Centígrados ")
while(True):
    grados_F = int(input("Ingrese la cantidad de grados Farhenheit a convertir a Centígrados: "))
    print(grados_F, "°F equivalen a", gradosC(grados_F),"°C")
    opcion = str(input("¿Desea continuar (Escriba salir para finalizar)?\n"))
    continuar(opcion)

# Richard Soria, Josué Guerra, Carlos Pérez