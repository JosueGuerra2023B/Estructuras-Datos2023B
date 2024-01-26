# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Crear un lista con 5 string, que el usuario 
# ingrese los caracteres y los imprima de forma invertida.

lista = []

for i in range(5):
    string = input("Ingresa un string: ")
    lista.append(string)

print ("La lista ingresada es: ",lista)
print ("La lista inversa es: ", lista [::-1])