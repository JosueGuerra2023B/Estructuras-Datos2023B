# Ejercicios Diccionarios Joue Guerra, Carlos Perez, Richard Sorio

# Declarar el diccionario con clave y valor

diccionario = {"Venezuela": "Caracas", "Colombia":"Bogota", "Ecuador":"Quito"}
print(f"El diccionario es: {diccionario}")
print("\n")

#Acceder a un valor

diccionario = {"Venezuela": "Caracas", "Colombia":"Bogota", "Ecuador":"Quito"}
print("La palabra asignada es: ", diccionario["Colombia"])
print("\n")

#Acceder a un valor

valor = diccionario["Ecuador"]
print(f"El valor asignado es: {valor}")
print("\n")

#Agregar un elemento

diccionario["Peru"] = "Limaaaaaaa"
print(f"La asignacion es: {diccionario}")
print("\n")

#Modificar un elemento

diccionario["Peru"] ="Lima"
print(f"La palabra asignada es: {diccionario}")
print("\n")

#Eliminar un elemento con del

del diccionario["Venezuela"]
print(diccionario)
diccionario2 = {"Venezuela": "Caracas", "Colombia":"Bogota", "Ecuador":"Quito", "Peru":"Lima"}
del(diccionario2["Peru"])
print(diccionario2)
print("\n")

#Eliminar un elemento con la funcion pop

diccionario = {"Venezuela": "Caracas", "Colombia":"Bogota", "Ecuador":"Quito", "Peru":"Lima"}
diccionario.pop("Ecuador")
print(diccionario)
print("\n")

# Tuplas

tupla = ["Venezuela", "Colombia", "Ecuador", "Peru", "Brasil"]
dicPaises = {tupla[0]:"Caracas", tupla[1]:"Bogota", tupla[2]:"Quito", tupla[3]:"Peru", tupla[4]:"Brasilia" }
print(dicPaises)
print("\n")

# Acceder un elemento en concreto

print(dicPaises[tupla[2]]) # por el indice de la tupla
print(dicPaises["Peru"]) # por el valor de la tupla
print("\n")

# Crear diccionarios con diferentes tipo de datos

jugadores = {"nombre":"Juan","apellido":"Perez","edad":20,"partidosJugados":5,"partidosGanados":3}
print(jugadores)
print("\n")

# Con valores de tipo tupla

jugador = {"nombre":"Juan","apellido":"Perez","edad":25,"partidosJugados":5,"partidosGanados":3, "detalleAnios":[2020, 2021, 2022, 2023, 2024]}
print("Los partidos se jugaron en los años: ", jugador["detalleAnios"])
print("\n")

# Un diccionario puede contener otro diccionario

jugador = {"nombre":"Juan","apellido":"Perez","edad":25,"partidosJugados":5,"partidosGanados":3, "detalleAnios":{"temporadas":[2020, 2021, 2022, 2023, 2024]}}
print("Los partidos se jugaron en los años: ", jugador["detalleAnios"])
print("\n")

# Consultar las claves del diccionario

print(jugador.keys())
print("\n")

# Consultar los valores del diccionario

print(jugador.values())
print("\n")

# Consultar la longitud del diccionario

print(len(jugador))
print("\n")

# Recorrer el diccionario con for e imprimir claves

diccionario_paises = {"Venezuela": "Caracas", "Colombia":"Bogota", "Ecuador":"Quito", "Peru":"Lima"}
for pais in diccionario_paises:
    print(pais)
print("\n")

# Recorrer el diccionario con for e imprimir clave y valor

diccionario_paises = {"Venezuela": "Caracas", "Colombia":"Bogota", "Ecuador":"Quito", "Peru":"Lima"}
for clave, valor in diccionario_paises.items():
    print (clave, valor)
print("\n")

# Con la funcion items() recorre los elementos del diccionario e imprime tanto la clave como el valor"""