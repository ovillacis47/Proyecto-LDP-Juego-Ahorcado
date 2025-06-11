import random

def main():
    # Se utiliza un bucle como control de errores si el jugador ingresa una opcion invalida del menu del juego
    while True:
        # Muestra menu del juego
        menuJuego()
        opcionEscogida = input("Selecciona una opcion: \n")
        if opcionEscogida == "1":
            limpiarConsola()
            # Se utiliza un bucle para que se siga ejecutando el juego si el jugador desea
            repetirJuego = True
            while repetirJuego:
                logicaJuego()
                # Se utiliza otro bucle como control de errores si el jugador ingresa una opcion invalida al indicar si desea o no repetir el juego
                opcionValida = True
                while opcionValida:
                    print("¿Deseas continuar? Si: Y / No: N")
                    continuar = input()
                    # Si desea continuar, repite el juego con otra palabra a adivinar
                    if continuar == "Y":
                        opcionValida = False
                        limpiarConsola()
                    # Si no desea continuar, muestra el menu del juego
                    elif continuar == "N": 
                        repetirJuego = False
                        opcionValida = False
                        limpiarConsola()
                    # Si ingresa una opcion invalida, se le indica esto y se le solicita que ingrese una opcion valida
                    else:
                        print("Opcion invalida, intente otra vez")
        elif opcionEscogida == "2":
            # Muestra las instrucciones del juego
            limpiarConsola()
            mostrarInstrucciones()
        elif opcionEscogida == "3":
            # Se termina la ejecucion del programa
            print("\nEJECUCION TERMINADA\n")
            break
        else:
            limpiarConsola()
            print("Opcion invalida, intente otra vez")

# Lista usada como almacenamiento para las palabras del juego    
lista:list = ["MANZANA", "ELEFANTE", "MARIPOSA", "ESTRELLA", "CANGREJO",
             "BIBLIOTECA", "HOSPITAL", "CHOCOLATE", "JARDINES", "TECNOLOGIA",
             "UNIVERSIDAD", "FARMACIA", "SOMBRERO", "PARQUEADERO", "PROGRAMAR",
             "COMPUTADORA", "CUADRADO", "CARRETERA", "TRANSPORTE", "BOSQUE"]

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
    print("===Juego del ahorcado===")
    print("OPCIONES")
    print("1. Iniciar juego")
    print("2. Mostrar instrucciones")
    print("3. Salir")

def mostrarInstrucciones():
    print("===Instrucciones del juego===")
    print("El juego consiste en adivinar una palabra mostrada por el sistema. " +
        "La palabra en un principio se mostrara con ciertas letras que sirvan a modo de pista, " +
        "el resto de espacios seran delimitados por guines bajos. Si ingresas una letra que " +
        "pertenezca a la palabra, esta se añadira a la misma y estaras mas cerca de ganar, " +
        "caso contrario se te contara una falla. Puedes fallar un numero maximo de 6 veces, si lo haces " +
        "perderas automaticamente el juego.\n\n" +
        "- Las letras deben ser ingresadas en mayusculas"
        "- Si deseas terminar el juego antes, puedes escribir 'exit' en la ejecucion del mismo")

def logicaJuego():
    # Establece cuantas veces puede fallar el jugador
    fallas = 6
    # Escoge la palabra a adivinar
    palabra = random.choice(lista)
    letras:list = obtener_Letras(palabra)

    palabraUsada = preparar_Palabra(palabra, letras)

    # Se permite intentos mientras las fallas no lleguen a 6
    while fallas > 0:
        print(palabraUsada)
        # Si la palabra ya no tiene guiones bajos, o sea esta completa, el jugador se le indica que ha ganado y se acaba el bucle
        if "_" not in palabraUsada:
            print("Felicidades, GANASTE!\n")
            break
        # Se obtiene la letra que el jugador cree correcta
        letra_Ingresada = input("Ingresa una letra: \n")
        # Si el jugador ya no quiere seguir, si escribe "exit" se acaba el juego
        if letra_Ingresada == "exit":
            break  
        # Si el jugador cree que ya ha adivinado la palabra, puede ingresarla para ganar automaticamente
        if letra_Ingresada == palabra:
            print("Adivinaste la palabra, felicidades, GANASTE!\n")
            break
        # Si la letra ya estaba entre las letras mostradas, no cuenta como falla ni se ingresa a la palabra porque, pues, ya estaba
        if letra_Ingresada in palabraUsada:
            print("Esta letra ya estaba en la palabra, intente con otra\n")
        # Si la letra pertenece a la palabra, se completan los espacios donde iba y se le indica al jugador que acerto
        elif letra_Ingresada in list(palabra):
            print("Acertaste")
            palabraUsada = comparar_Letras(letra_Ingresada, palabra, palabraUsada)
        # Si el jugador falla, disminuye el numero de fallas que puede cometer
        else:
            fallas -= 1
            # Si el jugador ya alcanzo el numero maximo de fallas, se le indica que perdio y cual era la palabra que debio adivinar
            if fallas <= 0:
                print("Intentos agotados, perdiste")
                print("La palabra era: " + palabra)
            # Si todavia no alcanza el numero maximo de fallas, se le indica que fallo y continua el juego
            else:
                limpiarConsola()
                print("Fallaste, te quedan " + str(fallas) + " intentos \n")

main()
    
        
