# Ejercicios Carlos Perez, JOsue Guerra, Richard Soria
# Ejercicios Tarea

def diaSiguiente (dia, mes, año):
    bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bisiesto:
        dias_por_mes[2] = 29
    if 1 <= mes <= 12 and 1 <= dia <= dias_por_mes[mes]:
        dia_siguiente = dia + 1
        if dia_siguiente > dias_por_mes[mes]:
            dia_siguiente = 1
            mes += 1
            if mes > 12:
                mes = 1
                año += 1
        return dia_siguiente, mes, año
    else:
        return None 
fecha_actual = (7, 2, 2024) 
siguiente_fecha = diaSiguiente (*fecha_actual)
if siguiente_fecha:
    print("Fecha actual:", fecha_actual)
    print("Día siguiente:", siguiente_fecha)
else:
    print("Fecha no válida.")