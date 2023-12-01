# Ejercicio 5 del deber
# notas

print("--Bienvenido al sistema de cálculo de notas--")

non = input(print(" Ingrese su nombre"))

a = float(input("Inserta la calificación del Primer parcial:  "))
b = float(input("Inserta la calificación del Segundo parcial: "))
c = float(input("Inserta la calificación del primer parcial:  "))
d = float(input("Inserta la calificación del examen final: "))
e = float(input("Inserta la calificación de un trabajo final: "))

prom = (a + b+ c) / 3
prom_t = prom * 0.55
ex = d * 0.30
trab = e * 0.15

tot = prom_t + ex + trab

print(".", non, " Su nota final es de: ", tot)
print("Programa echo por Josue Eduard Guerra Lovato")