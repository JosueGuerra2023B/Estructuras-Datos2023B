# Ejercicios Tarea Josue Guerra, Carlos Perez, Richard Soria
# Juego de la rueda
import random

def generar_lista():
    lista = ["X"] * 11 + ["Rueda"] * 4
    random.shuffle(lista)
    return lista

def jugar():
    lista = generar_lista()
    intentos = 7
    ruedas_encontradas = 0
    premio_total = 0
    while intentos > 0 and ruedas_encontradas < 4:
        indice = int(input("Ingrese un índice entre 0 y 14: "))
        if indice < 0 or indice > 14:
            print("Índice inválido. Intente nuevamente.")
            continue
        if lista[indice] == "Rueda":
            ruedas_encontradas += 1
            premio_total += 1000
            print("¡Encontraste una rueda!")
            print("Ruedas encontradas hasta el momento: ",ruedas_encontradas)
            print("Premio acumulado: $",premio_total)
        else:
            print("No encontraste una rueda.")

        intentos -= 1

    if ruedas_encontradas == 4:
        print(f"¡Ganaste un carro!")
    else:
        print("Juego terminado. No encontraste las cuatro ruedas.")
        print("Premio acumulado: $",premio_total)

jugar()
