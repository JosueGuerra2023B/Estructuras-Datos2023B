# Ejercicio 7
# Ejercicio echo por Carlos Perez

print("--//--\\\--Etafashion--//--\\\--")
print(" ")
nombre = input("Estimado cliente, inserte su nombre: \n")
num_prendas = int(input("Ingrese el número de prendas: "))

while num_prendas < 0:
    print("Ingrese un número de prendas válido")
    num_prendas = int(input("Ingrese el número de prendas: "))
valor_total = float(input("Ingrese el valor de la compra: "))
if num_prendas > 20:
    valor_final = valor_total - (valor_total * 0.10)
    print("El valor a pagar es de: {:.2f}".format(valor_final))
elif 20 >= num_prendas >= 10:
    valor_final = valor_total - (valor_total * 0.05)
    print("\nUsted ha recibido el 5%" "de descuento")
    print("El valor a pagar es de: {:.2f}".format(valor_final))
elif num_prendas < 9:
    print("No existe descuento: {:.2f}".format(valor_total))
print("\nGracias por confiar en nosotros")
print("--*--* Vuelva pronto *--*--")
