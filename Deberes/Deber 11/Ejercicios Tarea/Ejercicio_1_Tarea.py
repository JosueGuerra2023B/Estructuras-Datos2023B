# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
# Ejercicios tarea 
# Crea una tupla con los meses del año, pide números 
#al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, 
# muestra el contenido de esa posición sino muestra un mensaje de error.
# El programa termina cuando el usuario introduce un cero.

tuplaMeses = ("Enero", "Febrero", "Marzo","Abril", "Mayo", "Junio", "Julio", "Agosto", 
              "Septiembre", "Octubre", "Noviembre","Diciembre")

numeroMes = 1

while numeroMes != 0:
    numeroMes = int (input ("Ingresa un numero del 1 al 12: "))
    if numeroMes == 0:
        print ("Adios")
        exit (1)
    elif 1 <= numeroMes <= len(tuplaMeses):
        print ("El mes correspondiente a ", numeroMes, " es " , tuplaMeses [numeroMes - 1])
    else:
        print ("Recuerda que es un numero entre 1 y 12")