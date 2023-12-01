# Ejercicio 10C del deber
# Notas

alumno = input("Ingrese su nombre: ")
nota = float(input("Ingrese su nota de Inglés: "))

if 9 <= nota <= 10:
    mensaje = "Felicitaciones, su nota es excelente"
elif 7 <= nota <= 8:
    mensaje = "Siga adelante, su nota es muy buena"
elif 5 <= nota <= 6:
    mensaje = "Debe esforzarse más, su nota es buena"
elif 0 <= nota <= 4:
    mensaje = "Usted puede reprobar, su nota es regular"
else:
    mensaje = "Nota fuera de rango"

print(mensaje)

print("Programa echo por Josue Eduard Guerra Lovato")