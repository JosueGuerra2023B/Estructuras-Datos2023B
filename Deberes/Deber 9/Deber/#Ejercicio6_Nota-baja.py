# Tarea Carlos Perez, Josue Guerra, Richard Soria

# De las siguientes notas almacenadas en un arreglo: 
#[20, 15, 12, 11, 8, 4, 1] Elimine la nota más baja 
#programáticamente sin usar la función (min) y escriba 
#en pantalla. Luego calcule el promedio de notas descontando la nota eliminada.

notas = [20, 15, 12, 11, 8, 4, 1]
tamanio = len(notas)
menor = notas[0]

for nota in range(0,tamanio):
    if notas[nota]<menor:
        menor = notas[nota] 
notas.remove(menor)
tamanio_nuevo = len(notas)
promedio = (sum(notas)/tamanio_nuevo)

print("La notas menor es:",menor)

print("La notas finales son:", notas)

print("El promedio de las notas es:", round(promedio,2))

