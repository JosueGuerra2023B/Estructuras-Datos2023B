# Ejercicio 8
# Ejercicio echo por Carlos Perez
print("--//--\\\--Panadería--//--\\\--")
print("--//--\\\--La unión--//--\\\--")
print(" ")
nombre = input("Estimado cliente inserte su nombre: \n")
numero_guaguas = int (input ("Ingrese el numero de guaguas de pan que desea: \n"))
contador_guaguas = 1
guaguas_mora = 0
suma_guaguas = 0

while contador_guaguas <= numero_guaguas:
    precio = float (input ("Ingrese el precio de la guagua: "))
    suma_guaguas = suma_guaguas + precio
    sabor = int (input ("Seleccion el sabor de la guagua de pan: \n 1. Mora \n 2.Manjar \n"))
    while sabor != 1 and sabor != 2:
        print ("Ingrese un sabor valido")
        sabor = int (input ("Seleccion el sabor de la guagua de pan: \n 1. Mora \n 2.Manjar \n"))    
    if sabor == 1:
        guaguas_mora = guaguas_mora + 1
    contador_guaguas = contador_guaguas + 1

print ("\n-///---///-- Factura --\\\\\---\\\\\-\n")
print ()
print ("Estimado ",nombre )
print ("El precio a pagar es de: ",suma_guaguas)
print ("El total de guaguas de pan de mora es de: ",guaguas_mora)
print ("--**-- Vuelva pronto --**--")