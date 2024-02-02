#Contando sin la función
print("\nSegunda tupla")
tupla2 = (1, 2, 1, 4, 1, 6, 1, 8, 2, 2, 9, 6, 8, 7, 5)
count = 0
valor = int(input("Ingrese el valor a observar: "))  
for i in tupla2:
    if i == valor:  
        count += 1
print("El elemento" ,valor, " se repite:", count, "veces\n") 

#Usando la función index con un paramaetro
tup1= (7, 7, 7, 3, 5)
print(tup1.index(5))

#Usando la función index con dos parametros
tup1= (7, 7, 7, 3, 5)
print(tup1.index(7,2),"\n")
persona =("Josue","Guerra.")
nombre, apellido = persona
print(apellido)
print(nombre)

#Metodo enumerate
atletas = ("Josue", "Eduard", "Lovato")
#posicion = enumerate(atletas)
for index, atleta in enumerate(atletas):
    print("Posición: ",index+1, "atleta: ",atleta)
