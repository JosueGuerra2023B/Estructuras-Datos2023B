# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Crear una lista e inicialízala con 5 cadenas de caracteres. 
#Copia los elementos de la lista en otra lista pero en orden 
#inverso, y muestra sus elementos por la pantalla.
# Imprimir la lista invversa

cadena_ingresada = []
cantidad = 5

for caracteres in range (cantidad):
    caracteres = input ("Ingrese una palabra: " )
    cadena_ingresada.append (caracteres)


print ("La lista original es: ",cadena_ingresada)
print ("La lista inversa es: ", cadena_ingresada [::-1])

    