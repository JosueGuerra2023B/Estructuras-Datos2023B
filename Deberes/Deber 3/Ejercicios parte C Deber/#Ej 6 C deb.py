# Ejercicio 6C del deber
# Costo matrícula

alumnos = int(input("Ingrese el número de alumnos: "))

if alumnos >= 100:
    costo_por_alumno = 65
elif alumnos >= 50:
    costo_por_alumno = 70
elif alumnos >= 30:
    costo_por_alumno = 95
else:
    costo_por_alumno = 4000 / max(alumnos, 1)

costo_total = costo_por_alumno * alumnos
pago_por_alumno = costo_total / alumnos

print(f"El pago a la compañía es de: {costo_total}")
print(f"Los alumnos deben pagar un valor de: {pago_por_alumno}")


print("Programa echo por Josue Eduard Guerra Lovato")