# Guerra Josue
# Tuplas

#tuple: función con parentesis
#lo que determina una tupla son las comas, parentesis opcionales 

tupla = ('a', 'b', 'd')
print(tupla[2])

bebidas = ('agua','café','batido','sorbete')
print(bebidas[-1])

vocales = ('a', 'e', 'i', 'o', 'u')
print(vocales[2:3])
print(len(vocales))

pares = (2, 4, 6, 8, 10, 12, 14)
print(pares[::2])
print(pares[1:5:2])#desde el uno hasta el 5 de 2 en dos

bebidas1 = 'agua', 'cafe', 'batido'
a, b, c = bebidas1
print("\n",a,"\n",b,"\n",c)

colores = 'azul', 'blanco', 'negro'
for color in colores:
    print(color)
if 'azul' in colores:
    print('si')
if 'verde' not in colores:
    print("no")

tup = (1, ['a', 'b'], 'hola', 8.2)
tup[1].append('c')
print(tup)

