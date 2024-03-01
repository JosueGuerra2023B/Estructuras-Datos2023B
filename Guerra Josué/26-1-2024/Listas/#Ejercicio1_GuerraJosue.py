#Ejercicio 1
#Guerra Josue
print("Ejercico 8: ")
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
for i in range(len(abecedario), 1,-1):
    if i %3==0:
        abecedario.pop(i-1)
print(abecedario)

print("\n")
print("Ejercico 9: ")
palabra =input("Ingrese la palabra: ")
vocales=["a","e","i","o","u"]
#palabra=[]
contar = 0
for vocal in vocales:
     for letra in palabra:
         if letra == vocal:
          contar= contar +1
print("\n",vocal, contar)
