#Imprimir elemento de la posición 5
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupla[5],"\n")

#Iterar la tupla conn for
for i in tupla:
    print(i)

#Anidar tupla
tup = 1, 2, ('a', 'b'),3
print(tup)
print(tup[2][0],"\n")

#Asignar valor de tupla con 3 elementos a 3 variables
tupla = ('JUEGO', 'VIDEO', 'COMPUTADOR', 'xd')
a, b, c, d = tupla
print(a, " ", b, " ", c, " ", d, "\n")

#Metodo count
tuplas = (1, 2, 1, 4, 1, 6, 1, 8, 2, 2, 9, 6, 8, 7, 5)
print("El elemento se repite: ", tuplas.count(1), "veces\n")

#Que el ususario digite el elemento
tu = (1, 2, 1, 4, 1, 6, 1, 8, 2, 2, 9, 6, 8, 7, 5)
n = int (input ("Ingresa el elemento a contar: "))
print (tu.count(n))
# print("El elemento se repite: ", count, "veces\n")