# Tarea Carlos Perez, Josue Guerra, Richard Soria

# Almacenar el abecedario en una lista
print(" Bienvenido al programa ")
abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

print("Abecedario original:")
print(abecedario)

abecedario_filtrado = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]

print("\nLista después de eliminar letras en posiciones múltiplos de 3:")
print(abecedario_filtrado)
