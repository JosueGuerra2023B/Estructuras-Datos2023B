# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
# Ejercicios Tarea
def diaSiguienteT (dia, mes, año):

    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_por_mes[2] = 29  

    if mes < 1 or mes > 12 or dia < 1 or dia > dias_por_mes[mes]:
        return "FECHA INCORRECTA"
    
    
    tuplaMeses = ("Enero", "Febrero", "Marzo","Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre","Diciembre")
    dia_siguiente = dia + 1
    if dia_siguiente > dias_por_mes[mes]:
        dia_siguiente = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1

    fecha_siguiente = (dia_siguiente, tuplaMeses[mes], año)
    return fecha_siguiente
fecha_actual = (7, 2, 2024)  
fecha_siguiente = diaSiguienteT (*fecha_actual)
print(f"Fecha actual: {fecha_siguiente}")