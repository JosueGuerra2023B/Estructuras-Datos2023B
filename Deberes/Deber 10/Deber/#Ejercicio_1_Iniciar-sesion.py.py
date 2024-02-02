# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria
# Crear una función llamada “iniciarSesion”, que recibe 
# un nombre de usuario y una contraseña  si el nombre de usuario 
# es “usuario1” y la contraseña es “asdasd”. Además recibe el 
# número de intentos que se ha intentado iniciar sesión

def iniciarSesion (usuario, contraseña, intentos):
    if usuario == "usuario1" and contraseña == "asdasd":
        return True
    else:
        intentos += 1
        return False
intentos = 0

while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if iniciarSesion(usuario, contraseña, intentos):
        print("Inicio de sesión exitoso")
        break
    else:
        intentos += 1
        print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")

if intentos == 3:
    print("Se han agotado los tres intentos. Intente más tarde.")