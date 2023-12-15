#JOSUÉ GUERRA
#Ejercicoio pares impares 3

par = 0
impar = 0
cont = 0
num = int(input(" ingrese la cantidad de números "))

while   (cont < num):
    num2 = int(input(" Ingrese el número "))
    if (num2 %2 == 0):
            par = par + 1
    else:
         impar = impar + 1  
    cont = cont + 1
print(" Los pares ingresados son ", par )
print(" Los impares ingresados son: ", impar)


          