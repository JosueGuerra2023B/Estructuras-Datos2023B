# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
# Ejercicios Tarea

def sumaTiempo (tiempo_1, tiempo_2):
    horas = tiempo_1[0] + tiempo_2[0]
    minutos = tiempo_1[1] + tiempo_2[1]
    segundos = tiempo_1[2] + tiempo_2[2]

    minutos += segundos // 60
    segundos %= 60
    horas += minutos // 60
    minutos %= 60
    return horas, minutos, segundos

tuplaTiempo = (12, 30, 45)
tuplaTiempo_2 = (18, 31, 50)

resultado = sumaTiempo (tuplaTiempo, tuplaTiempo_2)
print ("Tiempo 1: ", tuplaTiempo)
print ("Tiempo2: ", tuplaTiempo_2)
print ("Suma de los timepos: ", resultado)