#Metodo Max y min  
print("\nPrimer tupla")
tupla3 = (2, 5, 100, 7, 2, 6, 8, 35, 28)
print("El número mayor es:", max(tupla3))
print("El número menor es:", min(tupla3))


#Crear tupla con números e indicar el número mayor y el menor
print("\nSegunda tupla")
tupla2 = (2, 5, 100, 7, 2, 6, 8, 35, 28)
mayor = tupla2[0]
menor = tupla2[0]
for num in tupla2:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
print("El mayor es:", mayor)
print("El menor es:", menor)

#FUNCIÓN TUPLA -Convertir una lista en tupla 
valores = [6, 7, 8, 9, 10]
print(valores)
tupla_lista = tuple(valores)
print(tupla_lista)

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



