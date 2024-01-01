#Ejercicio 10
#Ejercicio echo por Josué Guerra
while True:
    print("\Menú de Televisión/")
    print("Opciones para ver en el televisor")
    print("1. Noticias ")
    print("2. Deportes ")
    print("3. Spotify ")
    print("4. Amazon Prime ")
    print("5. Netflix ")
    print("6. carton network ")
    print("7. Youtube")
    print("8. HDMI ")
    print("0. Volver al menu central")
    print("9. APAGAR TELEVISOR")
    opcion = input("Selecciona una opción a su conveniencia: \n")
    if opcion == '1':
        print(" 1. Nacionales ")
        print(" 2. Internacionales\n")
        print(" 0. para regresar al menu central \n 9. para apagar el televisor: \n")
        noti = input("Que tipo de noticias desea ver: ")
        if noti == '1':
            print("Usted está viendo noticias Nacionales\n")
            note = input(" 0. para regresar al menu central \n9. para apagar el televisor:\n ")
            if note == '0':
                continue
            elif note == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
        elif noti == '2':
            print("Usted está viendo noticias Internacionales")
            note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
            if note == '0':
                continue
            elif note == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
        elif noti == '0':
            continue
        elif noti == '9':
            print("Apagando la televisión. ¡Hasta luego!")
            break
        else:
            print("Escoja una de las opciones indicadas")
            noti = input("Que tipo de noticias desea ver: ")
    elif opcion == '2':
        print(" 1. Basquet ")
        print(" 2. Futbol ")
        print(" 3. Formula 1 ")
        print(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
        noti2 = input("Que tipo de deporte desea ver: ")
        if noti2 == '1':
            print("Sintonizando en  un canal de Basquet")
            print("\n canal encontrado")
            print("Partido de lakers vs Warriors")
            note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
            if note == '0':
                continue
            elif note == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
        elif noti2 == '2':
            print("Sintonizando en canal de Futbol")
            print("\n canal encontrado")
            print("Partidos de la copa Champions")
            note = input(" 0. para regresar al menu central \n 9. para apagar el televisor: \n")
            if note == '0':
                continue
            elif note == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
        elif noti2 == '3':
            print("Sintonizando en la formula 1")
            print("\n canal encontrado")
            print("Giro de italia")
            note = input(" 0. para regresar al menu central \n 9. para apagar el televisor: \n")
            if note == '0':
                continue
            elif note == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
        elif noti2 == '0':
            continue
        elif noti2 == '9':
            print("Apagando la televisión. ¡Hasta luego!")
            break
        else:
            print("Escoja una de las opciones indicadas")
            noti2 = input("Que tipo de deporte desea ver: ")
    elif opcion == '3':
        print("entrando a spotify\n")
        print("Sintonizando en canciones más escuchadas")
        opi = input(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
        if  opi == '0':
            continue
        elif opi == '9':
            print("Apagando la televisión. ¡Hasta luego!")
            break
    elif opcion == '4':
        print("Cambiando a Amazon prime")
        print("Opciones que ofrece Amazon")
        print(" ")
        print(" 1. Peliculas ")
        print(" 2. Documentales ")
        print(" 3. Series")
        print(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
        noti3 = input("Que desea ver: ")
        if noti3 == '1':
            print("Sintonizando en peliculas")
            print(" 1. Terror ")
            print(" 2. Comedia romantica ")
            print(" 3. Ciencia ficción ")
            print(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
            peli = input("Que tipo de película desea ver: ")
            if peli == '1':
                print("Usted está viendo el canal de películas")
                print("\n genero ")
                print("-* Terror *-")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif peli == '2':
                print("Usted está viendo el canal de películas")
                print("\n genero ")
                print("-*- Comedia romantica -*-")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif peli == '3':
                print("Usted está viendo el canal de películas")
                print("\n genero ")
                print("/-*\\ Ciencia ficción /-*-\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif peli == '0':
                continue
            elif peli == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break    
            else:
                print("Escoja una de las opciones indicadas")
            peli = input("Que tipo de película desea ver: ")
        elif noti3 == '2':
            print("Sintonizando en Documentales")
            print("1. Naturaleza")
            print("2. Vida animal")
            print("Presione 0 para regresar al menu central \nPresione 9 para apagar el televisor: ")
            docu = input("Que tipo de documental desea ver: ")
            if docu == '1':
                print("Usted esta viendo el canal de documentales")
                print("\n Genero:")
                print("// Naturaleza\\\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif docu == '2':
                print("Usted esta viendo el canal de documentales")
                print("\n Genero:")
                print("// Vida animal\\\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif docu == '0':
                continue
            elif docu == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
            else:
                print("Escoja una de las opciones indicadas")
                docu = input("Que tipo de documental desea ver: ")
        elif noti3 == '3':
            print("Sintonizando en Series")
            print(" 1. koreanas ")
            print(" 2. Americanas ")
            print(" 3. Mexicanas ")
            print(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
            seri = input("Que tipo de serie desea ver: ")
            if seri == '1':
                print("Usted esta viendo series")
                print("\n Genero:")
                print("// Koreano\\\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif seri == '2':
                print("Usted esta viendo series")
                print("\n Genero:")
                print("// Americano \\\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif seri == '2':
                print("Usted esta viendo series")
                print("\n Genero:")
                print("// mexicano \\\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif seri == '0':
                continue
            elif seri == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break    
            else:
                print("Escoja una de las opciones indicadas")
                seri = input("Que tipo de serie desea ver: ")
        elif docu == '0':
                continue
        elif docu == '9':
            print("Apagando la televisión. ¡Hasta luego!")
            break
        else:
            print("Escoja una de las opciones indicadas")
            noti3 = input("Que desea ver: ")   
    elif opcion == '5':
        print("Cambiando a Netflix")
        print("Opciones que ofrece Netflix")
        print(" ")
        print(" 1. Peliculas ")
        print(" 2. Documentales ")
        print(" 3. Series")
        print(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
        noti4 = input("Que desea ver: ")
        if noti4 == '1':
            print("Sintonizando en peliculas")
            print("1. Terror ")
            print("2. Comedia romantica ")
            print("1. Ciencia ficción ")
            peli2 = input("Que tipo de película desea ver: ")
            if peli2 == '1':
                print("Usted está viendo el canal de películas")
                print("\n genero ")
                print("-* Terror *-")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif peli2 == '2':
                print("Usted está viendo el canal de películas")
                print("\n genero ")
                print("-*- Comedia romantica -*-")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif peli2 == '3':
                print("Usted está viendo el canal de películas")
                print("\n genero ")
                print("/-*\\ Ciencia ficción /-*-\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif peli2 == '0':
                continue
            elif peli2 == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
            else:
                print("Escoja una de las opciones indicadas")
                peli2 = input("Que tipo de película desea ver: ")
        elif noti4 == '2':
            print("Sintonizando en Documentales")
            print(" 1. Naturaleza")
            print(" 2. Vida animal")
            print(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
            docu2 = input("Que tipo de documental desea ver: ")
            if docu2 == '1':
                print("Usted esta viendo el canal de documentales")
                print("\n Genero:")
                print("// Naturaleza\\\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break 
            elif docu2 == '2':
                print("Usted esta viendo el canal de documentales")
                print("\n Genero:")
                print("// Vida animal\\\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif docu2 == '0':
                continue
            elif docu == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
            else:
                print("Escoja una de las opciones indicadas")
                docu2 = input("Que tipo de documental desea ver: ")
        elif noti4 == '3':
            print("Sintonizando en Series")
            print(" 1. koreanas ")
            print(" 2. Americanas ")
            print(" 3. Mexicanas ")
            print(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
            seri2 = input("Que tipo de serie desea ver: ")
            if seri2 == '1':
                print("Usted esta viendo series")
                print("\n Genero:")
                print("// Koreano\\\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif seri2 == '2':
                print("Usted esta viendo series")
                print("\n Genero:")
                print("// Americano \\\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif seri2 == '2':
                print("Usted esta viendo series")
                print("\n Genero:")
                print("// mexicano \\\\")
                note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
                if note == '0':
                    continue
                elif note == '9':
                    print("Apagando la televisión. ¡Hasta luego!")
                    break
            elif seri2 == '0':
                continue
            elif seri2 == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
            else:
                print("Escoja una de las opciones indicadas")
                seri2 = input("Que tipo de serie desea ver: ")
        elif noti4 == '0':
                continue
        elif noti4 == '9':
            print("Apagando la televisión. ¡Hasta luego!")
            break
        else:
            print("Escoja una de las opciones indicadas")
            noti4 = input("Que desea ver: ")  
    elif opcion == '6':
        print("Sintonizando Cartoon Network")
        print("Usted está viendo el canal de carton network")
        print("Programa en emisión actual: ")
        print("---/ El increible Mundo de Gumball \---")
        opi2 = input(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
        if opi2 == '0':
            continue
        elif opi2 == '9':
            print("Apagando la televisión. ¡Hasta luego!")
            break
    elif opcion == '7':
        print("Cambiando a youtube")
        print(" 1. Música ")
        print(" 2. Streamers ")
        print(" 3. Tutoriales")
        print(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
        noti5 = input("Que desea ver en Youtube: ")
        if noti5 == '1':
            print("Reproduciendo múisca del monento")
            print("Canción en curso - Mecha/Chano ")
            note = input(" 0. para regresar al menu central \n9. para apagar el televisor: \n")
            if note == '0':
                continue
            elif note == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
        elif noti5 == '2':
            print(" 1. Misasinfonia")
            print(" 2. Farfadox ")
            print(" 3. Amilcar")
            str = input("A que Youtuber desea ver: ")
            print("******---******\n")
            print(" 0. para regresar al menu central \n 9. para apagar el televisor: ")
            if str != '1' and str != '2' and str != '3':
                print(" Ingrese solo las opciones mencionadas ")
                str = input("A que Youtuber desea ver: ")
            if str == '0':
                continue
            elif str == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
            else:
                print("Reproduciendo contenido de ", str)
        elif noti5 == '2':
            print(" 1. Cocina")
            print(" 2. Arreglos ")
            print(" 3. Manualidades")
            tuto = input("Que tutorial desea ver: ")
            print("******---******\n")
            print(" 0. para regresar el menu central \n 9. para apagar el televisor: ")
            if tuto != '1' and tuto != '2' and tuto != '3':
                print(" Ingrese solo las opciones mencionadas ")
                tuto = input("Que tutorial desea ver: ")
            print("Presione 0 para regresar al menu central \nPresione 9 para apagar el televisor: ")
            if tuto != '1' and tuto != '2' and tuto != '3':
                print(" Ingrese solo las opciones mencionadas ")
                tuto = input("Que tutorial desea ver: ")
            if tuto == '0':
                continue
            elif tuto == '9':
                print("Apagando la televisión. ¡Hasta luego!")
                break
            else:
                print("Reproduciendo tutorial de ", tuto)
        else:
            print("Escoja una de las opciones indicadas")
            noti5 = input("Que desea ver en Youtube: ")

    elif opcion == '8':
        print("Señala HDMI detectada\n")
        print(" 1. HDMI-1/Playstation" )
        print(" 2. HDMI-2/Segunda pantalla-pc")
        print("0. para regresar al menu central \n 9. para apagar el televisor: ")
        hd = input("A cual de las conexiones HDMI desea conectarse: ")
        if hd != '1' and hd != '2':
            print(" Ingrese solo las opciones mencionadas ")
            hd = input("A cual de las conexiones HDMI desea conectarse: ")
        elif hd == '0':
                continue
        elif hd == '9':
            print("Apagando la televisión. ¡Hasta luego!")
            break
        else:
            print("Conectando a ", hd)
    elif opcion == '9':
        print("Apagando la televisión. ¡Hasta luego!")
        break
    else:
        print( "Opción no válida.")
        print( "Escoja una de las opciones presentadas")