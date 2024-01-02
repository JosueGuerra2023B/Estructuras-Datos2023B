# Ejercicio 4
# Pedir al usuario la cantidad de compra y sumar al final
# Ejercicio echo por Carlos Perez

print("Ejercicio 4 : Compra")
suma = 0
numero = 1
contador = 0

while numero != 0:
   numero = float (input ("Ingrese el valor de su compra: "))
   print ("Si desea finalizar ingrese 0.")
   suma = suma + numero
   contador += 1
   print (suma)
   
if suma >= 1000:
    respuesta = suma - (suma *0.1)
    print ("El total a pagar es de: ",respuesta)
else:
    print ("El total a pagar es de: ",suma)
