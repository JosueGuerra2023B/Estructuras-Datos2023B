# Ejercicio 1
# Pedir al usuario una cantidad para ahorrar
# Ejercicio echo por Carlos Perez

print ("---Bienvenido---")
ahorro =  float (input ("Ingrese la cantidad de dinero que desea ahorrar: "))
suma_ahorro = 0

while ahorro < 0:
  if ahorro < 0:
      print ("No puede ahorrar cantidades negativas")
      ahorro =  float (input ("Ingrese la cantidad de dinero que desea ahorrar: "))
while suma_ahorro < ahorro:
    dinero = float (input ("Ingrese el valor de su deposito: "))
    if dinero < 0:
        print ("No puede ingresar cantidades negativas")
    else:
        suma_ahorro = suma_ahorro + dinero
        print(suma_ahorro, " + ", dinero, " = ", suma_ahorro)
print ("Felicidades usted cumplio su meta :D")