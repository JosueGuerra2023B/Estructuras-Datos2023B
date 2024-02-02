# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria
# Cupos disponibles
import random

def registrar_aspirante():
    cedula = input("Ingrese la cédula del aspirante: ")
    nombre = input("Ingrese el nombre del aspirante: ")
    condecoracion = int(input("¿Tiene condecoración? (1: Sí, 0: No): "))
    print(" ")
    return {'cedula': cedula, 'nombre': nombre, 'condecoracion': condecoracion}

def sortear_cupos(aspirantes, cupos):
    seleccionados = []
    
    condecorados = [aspirante for aspirante in aspirantes if aspirante['condecoracion'] == 1]
    
    seleccionados.extend(condecorados)

    cupos_restantes = cupos - len(condecorados)

    restantes = [aspirante for aspirante in aspirantes if aspirante['condecoracion'] == 0]
    seleccionados.extend(random.sample(restantes, cupos_restantes))
    
    return seleccionados

def mostrar_seleccionados(seleccionados):
    print("\nLista de estudiantes seleccionados:")
    print("Cédula\t\tNombre\t\tCondecoración")
    for estudiante in seleccionados:
        print(f"{estudiante['cedula']}\t{estudiante['nombre']}\t{estudiante['condecoracion']}")

def main():
    n_cupos = int(input("Ingrese la cantidad total de cupos disponibles: "))
    m_cupos = int(input("Ingrese la cantidad de cupos a sortear: "))
    
    aspirantes = []
    # Registro de aspirantes
    num_aspirantes = int(input("Ingrese la cantidad de aspirantes: "))
    for _ in range(num_aspirantes):
        aspirante = registrar_aspirante()
        aspirantes.append(aspirante)
    
    seleccionados = sortear_cupos(aspirantes, m_cupos)
    
    # Mostrar la lista de seleccionados
    mostrar_seleccionados(seleccionados)
if __name__ == "__main__":
    main()
