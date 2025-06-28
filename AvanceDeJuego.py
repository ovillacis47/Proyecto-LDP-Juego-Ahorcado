import random

def main():
    while True:
        # Muestra menu del juego
        opcionEscogida = menuJuego()
        if opcionEscogida == "1":
            limpiarConsola()
            # Muestra menu de los modos de juego
            modoEscogido = menu_modos_juego()
            # Ejecucion para el modo un jugador
            if modoEscogido == "1":
                limpiarConsola()
                contador = 0
                # Solicita las rondas a jugar, el nombre del jugador y se ejecuta un bucle en base a esas rondas
                rondas = cantidad_rondas()
                jugador_1 = pedir_nombre("1")
                while contador < rondas:
                    print("RONDA " + str(contador + 1) + "\n\n")
                    terminar = logica_un_jugador(jugador_1)
                    print("\n\n")
                    # Si se obtiene un valorde retorno, se termina la partida (todas las rondas)
                    if terminar != 1:
                        contador += 1
                    else:
                        contador = rondas
            # Ejecucion para el modo vs computadora
            elif modoEscogido == "2":
                limpiarConsola()
                contador = 0
                # Solicita las rondas a jugar, el nombre del jugador y se ejecuta un bucle en base a esas rondas
                rondas = cantidad_rondas()
                jugador_1 = pedir_nombre("1")
                while contador < rondas:
                    print("RONDA " + str(contador + 1) + "\n\n")
                    terminar = logica_vs_computadora(jugador_1)
                    print("\n\n")
                    # Si se obtiene un valorde retorno, se termina la partida (todas las rondas)
                    if terminar != 1:
                        contador += 1
                    else:
                        contador = rondas
            # Ejecucion para el modo multijugador
            elif modoEscogido == "3":
                limpiarConsola()
                contador = 0
                # Solicita las rondas a jugar, el nombre de los jugadores y se ejecuta un bucle en base a esas rondas
                rondas = cantidad_rondas()
                jugador_1 = pedir_nombre("1")
                jugador_2 = pedir_nombre("2")
                while contador < rondas:
                    print("RONDA " + str(contador + 1) + "\n\n")
                    terminar = logica_multijugador(jugador_1, jugador_2)
                    print("\n\n")
                    # Si se obtiene un valorde retorno, se termina la partida (todas las rondas)
                    if terminar != 1:
                        contador += 1
                    else:
                        contador = rondas
            # Ejecucion para mostrar estadisticas
            elif modoEscogido == "4":
                limpiarConsola()
                imprimir_estadisticas()
                print("\n")
            # Sale del menu modos de juego
            elif modoEscogido == "5":
                continue
                
        elif opcionEscogida == "2":
            # Muestra las instrucciones del juego
            limpiarConsola()
            mostrarInstrucciones()
        elif opcionEscogida == "3":
            # Se termina la ejecucion del programa
            print("\nEJECUCION TERMINADA\n")
            break

# Lista usada como almacenamiento para las palabras del juego    
lista:list = ["MANZANA", "ELEFANTE", "MARIPOSA", "ESTRELLA", "CANGREJO",
             "BIBLIOTECA", "HOSPITAL", "CHOCOLATE", "JARDINES", "TECNOLOGIA",
             "UNIVERSIDAD", "FARMACIA", "SOMBRERO", "PARQUEADERO", "PROGRAMAR",
             "COMPUTADORA", "CUADRADO", "CARRETERA", "TRANSPORTE", "BOSQUE"]
# Lista usada como almacenamiento para los jugadores
lista_jugadores = []

def obtener_Letras(palabra):
    tamano = len(palabra)
    # Las letras que se mostraran seran un tercio de las letras de la palabra a adivinar
    numero_letras_mostradas = int(tamano/3) 

    # Se transforma la palabra en un conjunto para eliminar los caracteres repetidos y luego transformarlo a lista
    letras_unicas = list(set(palabra))

    # Si el número a mostrar es mayor que las letras unicas, ajustamos
    numero_letras_mostradas = min(numero_letras_mostradas, len(letras_unicas))

    # Escoge letras sin repetir aleatoriamente de la palabra en base al numero de letras a mostrar
    letras_mostradas = random.sample(letras_unicas, numero_letras_mostradas)

    return letras_mostradas
    
def preparar_Palabra(palabra, letrasMostradas:list):
    palabraMostrada = ""

    # Muestra la palabra con las letras seleccionadas y el resto de espacios delimitados por guiones bajos
    for letra in palabra:
        if letra in letrasMostradas:
            palabraMostrada += letra
        else:
            palabraMostrada += "_"

    return palabraMostrada

def comparar_Letras(letra, palabra, palabraMostrada):
    listaAuxiliar = list(palabraMostrada)
    # Obtiene los espacios en los que va la letra que el jugador adivino
    posiciones:list = [i for i, caracter in enumerate(palabra) if caracter == letra]
    # Sustituye los guiones bajos de las posiciones obtenidas por la letra que el jugador adivino
    for contador in posiciones:
        listaAuxiliar[contador] = letra
    # Retorna la palabra con la nueva letra
    palabraMostrada = "".join(listaAuxiliar)
    return palabraMostrada

def limpiarConsola():
    print("\n \n \n \n \n \n \n \n \n \n")

def menuJuego():
    opcion = ""
    while True:
        print("===Juego del ahorcado===")
        print("OPCIONES")
        print("1. Iniciar juego")
        print("2. Mostrar instrucciones")
        print("3. Salir")
        opcion = input("Selecciona una opcion: \n")
        if opcion == "1" or opcion == "2" or opcion == "3":
            break 
        else:
            limpiarConsola()
            print("Opcion invalida, intente nuevamente")
    return opcion

def menu_modos_juego():
    opcion = ""
    while True:
        print("===Modos de Juego===")
        print("OPCIONES")
        print("1. Un jugador")
        print("2. VS Computadora")
        print("3. Multijugador")
        print("4. Estadisticas")
        print("5. Salir")
        opcion = input("Selecciona una opcion: \n")
        if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5":
            break
        else:
            limpiarConsola()
            print("Opcion invalida, intente nuevamente")
    return opcion

# Obtiene el numero de rondas
def cantidad_rondas():
    while True:
        try:
            numero_rondas = input("¿Cuantas rondas desea jugar?\n")
            numero_rondas = int(numero_rondas)
            break
        except Exception as e:
            limpiarConsola()
            print("Ingrese un caracter numerico entero")
    return numero_rondas

# Pide nombre del jugador
def pedir_nombre(numero):
    return input("Ingrese nombre del jugador " + numero + "\n")

# Actualiza las estadisticas usando listas de diccionarios, tiene como parametro el nombre y resultado del jugador
def actualizar_estadisticas(jugador, resultado):
    # Obtiene posicion en la lista del jugador con el nombre de existir en la lista
    posicion = [iteracion for iteracion, diccionario in enumerate(lista_jugadores) if diccionario['Nombre'] == jugador]
    # Si es nuevo, le añade un elemento con el nombre y resultado del jugador
    if posicion == []:
        if resultado == 'Victorias':
            lista_jugadores.append({'Nombre': jugador, 'Victorias': 1, 'Derrotas': 0})
        else:
            lista_jugadores.append({'Nombre': jugador, 'Victorias': 0, 'Derrotas': 1})
    # Si no es nuevo, se suma en uno a la estadistica del resultado obtenido
    else:
        lista_jugadores[posicion[0]][resultado] += 1

# Metodo para imprimir la listade jugadores en un formato especifico
def imprimir_estadisticas():
    print("ESTADISTICAS DE LOS JUGADORES\n")
    if not lista_jugadores == []:
        for jugador in lista_jugadores:
            print("Nombre: " + jugador['Nombre'])
            print("Victorias: " + str(jugador['Victorias']))
            print("Derrotas: " + str(jugador['Derrotas']) + "\n")
    else:
        print("Aun no se han registrado partidas")

def mostrarInstrucciones():
    print("===Instrucciones del juego===")
    print("El juego consiste en adivinar una palabra mostrada por el sistema. " 
        "\nMODO UN JUGADOR\n" 
        "La palabra en un principio se mostrara con ciertas letras que sirvan a modo de pista, " 
        "el resto de espacios seran delimitados por guines bajos. Si ingresas una letra que " 
        "pertenezca a la palabra, esta se añadira a la misma y estaras mas cerca de ganar, " 
        "caso contrario se te contara una falla. Puedes fallar un numero maximo de 6 veces, si lo haces " 
        "perderas automaticamente el juego.\n" 
        "\nVS COMPUTADORA\n" 
        "El jugador ingresara una palabra la cual debera adivinar la computadora, la computadora"
        " escogera una letra al azar del abecedario y se debera ingresar por teclado nuestra decision "
        "respecto a si la letra mostrada pertenece o no a la palabra\n"
        "Para esta modalidad la computadora tiene 15 intentos al ser una maquina y escoger numeros al azar "
        "independientemente de las letras que vaya adivinando o fallando"
        "\nMODO MULTIJUGADOR\n" \
        "La base de funcionamiento es el mismo respecto a vs computadora, solo que ahora quien adivinara" \
        "las letras no sera la computadora sino otro jugador. En este modo el jugador 2 solo podra falla un numero " \
        "maximo de 6 veces\n"
        "- Las letras deben ser ingresadas en mayusculas\n"
        "- Si deseas terminar el juego antes, puedes escribir 'exit' en la ejecucion del mismo")

def logica_un_jugador(nombre_jugador):
    # Establece cuantas veces puede fallar el jugador
    fallas = 6
    # Escoge la palabra a adivinar
    palabra = random.choice(lista)
    letras:list = obtener_Letras(palabra)

    palabraUsada = preparar_Palabra(palabra, letras)

    # Se permite intentos mientras las fallas no lleguen a 6 
    while fallas > 0:
        print(" ".join(palabraUsada))
        # Si la palabra ya no tiene guiones bajos, o sea esta completa, el jugador se le indica que ha ganado y se acaba el bucle
        if "_" not in palabraUsada:
            print("Felicidades, GANASTE " + nombre_jugador + "!\n")
            actualizar_estadisticas(nombre_jugador, 'Victorias')
            break
        # Se obtiene la letra que el jugador cree correcta
        letra_Ingresada = input("Ingresa una letra: \n")
        letra_Ingresada = letra_Ingresada.upper()
        # Si el jugador ya no quiere seguir, si escribe "exit" se acaba el juego
        if letra_Ingresada == "EXIT":
            limpiarConsola()
            print("-Partida terminada-")
            return 1
        # Si el jugador cree que ya ha adivinado la palabra, puede ingresarla para ganar automaticamente
        if letra_Ingresada == palabra:
            print("Adivinaste la palabra, felicidades, GANASTE!\n")
            break
        # Si la letra ya estaba entre las letras mostradas, no cuenta como falla ni se ingresa a la palabra porque, pues, ya estaba
        if letra_Ingresada in palabraUsada:
            print("Esta letra ya estaba en la palabra, intente con otra\n")
        # Si la letra pertenece a la palabra, se completan los espacios donde iba y se le indica al jugador que acerto
        elif letra_Ingresada in list(palabra):
            limpiarConsola()
            print("Acertaste")
            palabraUsada = comparar_Letras(letra_Ingresada, palabra, palabraUsada)
        # Si el jugador falla, disminuye el numero de fallas que puede cometer
        else:
            limpiarConsola()
            fallas -= 1
            # Si el jugador ya alcanzo el numero maximo de fallas, se le indica que perdio y cual era la palabra que debio adivinar
            if fallas <= 0:
                print("Intentos agotados, perdiste " + nombre_jugador)
                print("La palabra era: " + palabra)
                actualizar_estadisticas(nombre_jugador, 'Derrotas')
            # Si todavia no alcanza el numero maximo de fallas, se le indica que fallo y continua el juego
            else:
                print("Fallaste, te quedan " + str(fallas) + " intentos \n")

def logica_vs_computadora(nombre_jugador):
    # Establece cuantas veces puede fallar el jugador
    fallas = 15
    # Ingresa la palabra a adivinar y verifica que los caracteres solo sean letras
    while True:
        palabra = input("¿Cuál será la palabra a adivinar?:\n")
        if palabra.isalpha() and palabra.isascii:
            palabra = palabra.upper()
            break
        else:
            print("Palabra contiene caracteres no validos, por favor intente con otra")
    palabra_mostrada = ""
    for letra in palabra:
        palabra_mostrada += "_"
    letras_adivinadas = []
    letras_erradas = []
    # Se permite intentos mientras las fallas no lleguen a 15
    while fallas > 0:
        print(" ".join(palabra_mostrada))
        #Cuando la palabra ya este completa, se termina el juego
        if palabra == palabra_mostrada:
            print("Gano la computadora, perdiste " + nombre_jugador)
            actualizar_estadisticas(nombre_jugador, 'Derrotas')
            break
        #Muestra una letra que no haya sido mostrada antes
        while True:
            letra = chr(random.randint(ord('A'), ord('Z')))
            if (not letra in letras_adivinadas) and (not letra in letras_erradas):
                break
            else:
                continue
        #Inicia un bucle para evitar caidas por ingreso de opcion invalida
        while True:
            #Pregunta si la letra mostrada esta en la palabra a adivinar
            respuesta = input("¿La letra esta en la palabra?: " + letra + " (S/N)\n")
            respuesa = respuesta.upper()
            #Si el jugador lo desea, puede terminar esta ronda abruptamente
            if respuesta == "EXIT":
                limpiarConsola()
                print("-Partida terminada-")
                return 1
            #Si lo esta, completa esa letra en la palabra
            elif respuesta == "S":
                limpiarConsola()
                letras_adivinadas.append(letra)
                palabra_mostrada = comparar_Letras(letra, palabra, palabra_mostrada)
                break
            #Si no, resta un intento
            elif respuesta == "N":
                fallas -= 1
                limpiarConsola()
                # Si la computadora ya alcanzo el numero maximo de fallas, se le indica al jugador que gano y la palabra que se debia adivinar
                if fallas <= 0:
                    print("Intentos agotados para la computadora, ganaste " + nombre_jugador)
                    print("La palabra era: " + palabra)
                    actualizar_estadisticas(nombre_jugador, 'Victorias')
                # Si todavia no alcanza el numero maximo de fallas, se le indica que fallo y continua el juego
                else:
                    print("Fallo la computadora, le quedan " + str(fallas) + " intentos \n")
                    letras_erradas.append(letra)
                break
            else:
                limpiarConsola()
                print("Opcion invalida, intente otra vez")

def logica_multijugador(jugador_1, jugador_2):
    # Establece cuantas veces puede fallar el jugador
    fallas = 6
    # Jugaodor 1 ingresa la palabra a adivinar
    while True:
        palabra = input("¿Cuál será la palabra a adivinar, " + jugador_1 + "?:\n")
        if palabra.isalpha() and palabra.isascii:
            palabra = palabra.upper()
            limpiarConsola()
            break
        else:
            print("Palabra contiene caracteres no validos, por favor intente con otra")
    palabra_mostrada = ""
    for letra in palabra:
        palabra_mostrada += "_"
    # Se permite intentos mientras las fallas no lleguen a 6 
    while fallas > 0:
        print(" ".join(palabra_mostrada))
        #Cuando la palabra ya este completa, se termina el juego
        if palabra == palabra_mostrada:
            print(jugador_2 + " adivinaste la palabra \nPerdiste " + jugador_1)
            actualizar_estadisticas(jugador_1, 'Derrotas')
            actualizar_estadisticas(jugador_2, 'Victorias')
            break
        #Solicita al jugador 2 una letra y verifica que sea una letra
        while True:
            letra = input(jugador_2 + " ingrese una letra:\n")
            if letra.isalpha() and letra.isascii:
                letra = letra.upper()
                limpiarConsola()
                break
            else:
                print("Caracteres no validos, por favor intente otra vez")
        
        #Si el jugador 2 lo desea, puede terminar esta ronda abruptamente
        if letra == "EXIT":
            limpiarConsola()
            print("-Partida terminada-")
            return 1
        
        #Inicia un bucle para evitar caidas por ingreso de opcion invalida
        while True:
        #Pregunta si la letra mostrada esta en la palabra a adivinar
            respuesta = input("" + jugador_1 + ", ¿la letra esta en la palabra?: (S/N)\n")
            respuesta = respuesta.upper()
            
            #Si el jugador 1 lo desea, puede terminar esta ronda abruptamente
            if respuesta == "EXIT":
                limpiarConsola()
                print("-Partida terminada-")
                return 1
            #Si lo esta, completa esa letra en la palabra
            elif respuesta == "S":
                limpiarConsola()
                print("Acertaste " + jugador_2)
                palabra_mostrada = comparar_Letras(letra, palabra, palabra_mostrada)
                break
            #Si no, resta un intento
            elif respuesta == "N":
                limpiarConsola()
                fallas -= 1
                # Si la computadora ya alcanzo el numero maximo de fallas, se le indica al jugador que gano y la palabra que se debia adivinar
                if fallas <= 0:
                    print("Intentos agotados \nPerdiste " + jugador_2 + "\nGanaste " + jugador_1)
                    print("La palabra era: " + palabra)
                    actualizar_estadisticas(jugador_1, 'Victorias')
                    actualizar_estadisticas(jugador_2, 'Derrotas')
                # Si todavia no alcanza el numero maximo de fallas, se le indica que fallo y continua el juego
                else:
                    print("Fallaste " + jugador_2 + ", te quedan " + str(fallas) + " intentos \n")
                break
            else:
                limpiarConsola()
                print("Opcion invalida, intente otra vez")

main()
    
        
