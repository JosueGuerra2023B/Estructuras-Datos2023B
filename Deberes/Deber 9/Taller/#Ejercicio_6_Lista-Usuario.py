# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Agregar un elemento pidiendo al usuario a una lista usando append()
# Que el usuario ingrese los elementos

arreglo_usuario = []

for notas in range (5):
    notas = int (input ("Ingrese la nota: " ))
    arreglo_usuario.append (notas)
    
print ("La lista de notas es: ",arreglo_usuario)
print ("El numero de notas ingresadas es: ", len(arreglo_usuario))

    
