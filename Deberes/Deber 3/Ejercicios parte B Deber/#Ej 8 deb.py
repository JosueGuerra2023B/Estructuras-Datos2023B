# Ejercicio 8 del deber
# Distancia

print (" Distancia entre dos vehículos ")

v = int (input ("Ingrese la velocidad del primer auto : "))
print(" La velocidad del segundo coche es mayor del primero")
v2 = int (input ("Ingrese la velocidad del segundo auto: "))
dist = float (input ("Ingrese la distancia entre los autos: "))


dif = v2 - v
tiempo = dist / dif 

tiempo = round(tiempo * 60, 2)
print ("El segunco auto alcanzara el primero en ",tiempo, " minutos")

print("Programa echo por Josue Eduard Guerra Lovato")