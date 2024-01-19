# Solicitar al usuario que ingrese su dirección email.
# Imprimir un mensaje indicando si la dirección es válida o no, 
# valiéndose de una función para decidirlo.
# Nota: El correo se considerará válido si tiene el símbolo "@".
def validarCorreo(correo):
    if "@" in correo:
        print("Dirreción válida")
        return exit(0)
    else:
        print("Ingrese una dirrección de correo válida") 

while(True):
    correo = str(input("Ingrese su correo electrónico: "))
    validarCorreo(correo)  

# Richard Soria, Josué Guerra, Carlos Pérez