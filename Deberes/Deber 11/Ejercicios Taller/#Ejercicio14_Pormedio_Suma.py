#miscelanea-listas
#crear una lista vacia, (5) que pida sus valores 
# y devuelva la suma y el promedio 
lista = []
suma = 0
promedio = 0
numero = 0
for i in range(5):
    numero = int(input("Ingrese un valor: "))
    lista.append(numero)
    suma = suma + numero

promedio = suma / len(lista)
for i in lista:
    print(i, end=" ")
print("\nLa suma de los valores es:", suma)
print("El promedio de los valores es:", promedio)

lista=[5, 7, 3, 6, 2, 8, 9, 11, 4]
for i in range(1, len(lista)):
    aux= lista[i]
    indice = i
    while indice >0 and lista[indice-1]> aux:
        lista[indice] = lista[indice-1]
        indice = -1
        lista[indice]=aux
print(lista)
