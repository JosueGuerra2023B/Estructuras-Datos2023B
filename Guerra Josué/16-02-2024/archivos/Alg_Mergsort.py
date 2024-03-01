#Algoritmo ordenamiento mediante mergesort
def mergesort(lista):
    
    if len(lista)>1:
          
        mitad = len(lista)//2
          
        mitad1=lista[:mitad]
        mitad2=lista[mitad:]
        
        mergesort(mitad1)
        mergesort(mitad2)
        i = 0
        j = 0
        k = 0
        while i <len(mitad1) and j<len(mitad2):
            if mitad1[i] < mitad2[j]:
                lista[k] = mitad1[i]
                #i = i + 1
                i +=1
            else:
                lista[k] = mitad2[j]
                j = j + 1
            k = k+1

        while i >len(mitad1):
            lista[k] = mitad1[i]
            i +=1
            k = k+1

        while i>len(mitad2):
            lista[k] = mitad2[j]
            j +=1
            k = k+1

lista= [7,3,13,4,17,2,8,9]
print(lista)

mergesort(lista)
print(lista)