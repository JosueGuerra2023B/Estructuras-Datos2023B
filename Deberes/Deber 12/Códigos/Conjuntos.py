# Ejercicios Diccionarios Joue Guerra, Carlos Perez, Richard Sorio
# Conjuntos

# Crear un conjunto
conjunto = {1, 2, 3, 4, 5}

# Mostrar el conjunto
print("Conjunto:", conjunto)

# Agregar un elemento al conjunto
conjunto.add(6)
print("Conjunto después de agregar 6:", conjunto)

# Eliminar un elemento del conjunto
conjunto.remove(3)
print("Conjunto después de eliminar 3:", conjunto)

# Verificar si un elemento está en el conjunto
print("¿El número 2 está en el conjunto?", 2 in conjunto)

# Obtener la longitud del conjunto
print("Longitud del conjunto:", len(conjunto))

# Iterar sobre los elementos del conjunto
print("Elementos del conjunto:")
for elemento in conjunto:
    print(elemento)

# Crear un conjunto a partir de una lista
lista = [4, 5, 6, 7, 8]
conjunto_desde_lista = set(lista)
print("Conjunto creado a partir de una lista:", conjunto_desde_lista)

# Operaciones de conjuntos
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# Unión de conjuntos
union = conjunto_a.union(conjunto_b)
print("Unión de conjuntos:", union)

# Intersección de conjuntos
interseccion = conjunto_a.intersection(conjunto_b)
print("Intersección de conjuntos:", interseccion)

# Diferencia entre conjuntos
diferencia = conjunto_a.difference(conjunto_b)
print("Diferencia entre conjuntos A y B:", diferencia)