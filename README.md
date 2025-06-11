# Proyecto-LDP-Juego-Ahorcado

El programa se ha realizado en el lenguaje de programación Python mediante el editorde código Visual Studio Code en la plataforma Windows 10.

El programa ejecuta el "Juego del ahorcado" utilizando como medio de interacción la consola de comandos; al inicio de la ejecución se mostrará un menú con 3 opciones 
que permitirán iniciar el juego, mostrar las instrucciones o finalizar la ejecución. En caso de ingresar una opción no numérica o que no sea válida entre las opciones, 
se indicará al usuario que ha ingresado un caracter inválido y le solicitará que escoja una opción posible.

Al escoger la opción para iniciar el juego, el sistema establecerá como número de fallas máxima la cantidad de 6 y escogerá y mostrará una palabra de la lista de 20 
palabras para adivinar, siendo que mostrará dicha palabra con un tercio de sus letras como caracteres únicos y el resto de caracteres serán reemplazados por guiones 
bajos, luego le solicitará al jugador que ingrese una letra que el considere que sea de la palabra. 

Si el jugador acierta la letra, el sistema completa en la palabra los espacios en donde iría la letra; si el jugador falla, se resta el número de fallas en 1. Si el
jugador completa la palabra, se le indica que ha ganado, por el contrario si el jugador alcanza las 6 fallas se le indica que ha perdido. Tras decidirse el resultado,
se le consulta al jugador si desea continuar con el juego con otra palabra o si desea terminar el juego; si escoge terminar el juego se le mostrará nuevamente el
menú del juego.