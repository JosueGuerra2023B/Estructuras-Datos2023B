#Ejercicio14
#Operadores de nivel de bits
print(" *** Operadores de nivel de bits *** ")
x = 2
y = 7

print(" x = ", x)
print(" y = ", y)

bit_a_bit = x | y
exclusivo_bit_a_bit = x ^ y
and_bit_a_bit = x & y
desplaza_x_n_bits_izquierda = x << 1
desplaza_x_n_bits_derecha = x >> 1
obtiene_bits_invertidos = ~ x
print(" Bit a Bit: (x | y) = ", bit_a_bit)
print(" ///////////////") 
print(" Exclusivo Bit a Bit: (x ^ y) = ", exclusivo_bit_a_bit)
print(" ///////////////") 
print(" And Bit a Bit: (x & y) = ",and_bit_a_bit)
print(" ///////////////") 
print(" Desplaza x,n de bits a la izquierda: (x << y) = ", desplaza_x_n_bits_izquierda)
print(" ///////////////") 
print(" Desplaza x,n de Bits a la derecha: (x >> y) = ",desplaza_x_n_bits_derecha)
print(" ///////////////") 
print(" Obtiene Bits invertidos: (x ~ y) = ",obtiene_bits_invertidos)
print(" ///////////////") 
print("Programa echo por Josue Eduard Guerra Lovato")