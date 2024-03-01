#clase de archivos 
#open(<archivo>, <modo>) crear o abrir el archivo 
#open("nombres.txt")
#open("datos/nombre.txt")-<var_objetos>.<atributo>
#crear archivo en rsuta específica
"""archivo = open('archivos/prueba1.txt','w')

archivo.close()"""

#sobre escribir el archivo  creado 
"""archivo = open('archivos/prueba1.txt','w')
archivo.write('Hola que hace\n')
archivo.write('compraste leche xd ')


archivo.close()"""

#Abrir el archivo 
"""archivo = open('archivos/codigos.txt',"r")
print(archivo.read())

archivo.close()"""

#Abrir un archivvo y leer linea por linea
"""archivo = open('archivos/prueba1.txt','r')
linea_txt = archivo.readline()
while linea_txt != "":
    print(linea_txt)
    linea_txt = archivo.readline()
    
archivo.close()"""

archivo = open('archivos/prueba1.txt','r')
for linea in archivo.readlines():
    print(linea)
archivo.close()
