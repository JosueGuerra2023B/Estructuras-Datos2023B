# Ejercicio 6
#Eejercicio echo por Carlos Perez

print ("---Bienvenido a Banco Pichincha---")
cliente = input ("Porfavor ingrese su nombre: \n")

tipo_tarjeta = int (input ("Ingrese su tipo de tarjeta: 1.) o 2.) o 3.) o 4.): \n"))

while tipo_tarjeta != 1 and tipo_tarjeta != 2 and tipo_tarjeta != 3 and tipo_tarjeta != 4:
    print ("Tipo de tarjeta invalido...")
    tipo_tarjeta = int (input ("Ingrese su tipo de tarjeta: 1.) o 2.) o 3.) o 4.)"))

credito_anterior = float (input ("Ingrese su credito actual: "))

if tipo_tarjeta == 1:
    credito_nuevo = (credito_anterior + (credito_anterior * 0.25))
elif tipo_tarjeta == 2: 
    credito_nuevo = (credito_anterior + (credito_anterior * 0.35))
elif tipo_tarjeta == 3:
    credito_nuevo = (credito_anterior + (credito_anterior * 0.40))
elif tipo_tarjeta == 4: 
    credito_nuevo = (credito_anterior + (credito_anterior * 0.50))

print (cliente)
print ("Su tipo de tarjeta es: ",tipo_tarjeta)
print ("Su credito anterior es: ",credito_anterior)
print ("Su nuevo credito es: ",credito_nuevo)