# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
# Ejercicios Tarea

def poker (cartas):
    contador = [0] * 14
    for carta in cartas:
        contador[carta] += 1

    for frecuencia in contador:
        if frecuencia == 4:
            return True
    return False

# Programa Principal
Cartas = []

for i in range (5):
    carta = int (input ("Ingresa el numero de tu carta: "))
    Cartas.append (carta)

resultado = poker (Cartas)
if resultado:
    print ("Tienes un poker en tu mano")
else:
    print ("No es un poker")