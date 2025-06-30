# Proyecto-LDP-Juego-Ahorcado

Versión de Python: 3.13.3. El programa se ha realizado en el lenguaje de programación Python mediante el editorde código Visual Studio Code en la plataforma Windows 10.
Fecha: 29/06/2025
Estudiante: Owen Villacis
Nombre del proyecto: Desarrollo de software basado en el juego del ahorcado.

Objetivo:
Demostrar los conocimientos adquiridos a lo largo de la asignatura mediante el diseño e implementación de un software basado en el juego del ahorcado, aplicando técnicas de programación como el uso de bucles iterativos, estructuras de control, estructuras condicionales y programación modular, con el fin de evidenciar el dominio práctico de los conceptos fundamentales de la programación.

Funcionalidades:
El software en ejecución cuenta con un menú principal con las siguientes opciones:

- Inicio del juego
- Instrucciones del juego
- Terminar ejecución

La primera opción nos mostraría otro menú en el que las opciones serían los modos de juego, el mostrar las estadísticas de los jugadores y el volver al menú anterior.
Al seleccionar un modo de juego se solicitará el nombre de el o los jugadores, y se ssiendo los modos de juego los siguientes:

Un jugador: El sistema establecerá como número de fallas máxima la cantidad de 6 y escogerá y mostrará una palabra de la lista de 20 
palabras para adivinar, siendo que mostrará dicha palabra con un tercio de sus letras como caracteres únicos y el resto de caracteres serán reemplazados por guiones bajos, luego le solicitará al jugador que ingrese una letra que el considere que sea de la palabra. Si el jugador acierta la letra, el sistema completa en la palabra los espacios en donde iría la letra; si el jugador falla, se resta el número de fallas en 1. Si el jugador completa la palabra, se le indica que ha ganado, por el contrario si el jugador alcanza las 6 fallas se le indica que ha perdido.

Jugador contra computadora: En este modo quien deberá adivinar la palabra será la computadora. Al inicio se solicitará por teclado al usuario que ingrese una palabra, se validará el que los caracteres correspondan únicamente a letras, tras esto la computadora mostrará al jugador únicamente guiones bajos separados por espacio en base al número de letras de la palabra que ingresó, luego le mostrará una letra seleccionada aleatoriamente y, en caso de no ser el primer intento, que no haya sido ingresada antes por la computadora, y le preguntará si dicha letra pertenece a la palabra que el jugador ingreso.
Se le solicitará al jugador su respuesta con un “S” para “si” o “N” para “no”; en caso de ingresar “S” la computadora completará los guiones/espacios en donde iría la letra que se adivinó y el resto de espacios seguirían siendo guiones bajos. En caso de ingresar “N” se contaría como un fallo y se restaría un intento. La computadora puede fallar un máximo de 15 veces.
Si la computadora llega al máximo de fallos, se indica al jugador que ganó y se actualizan sus estadísticas. Si por el contrario la computadora completa todos los espacios de la palabra, se le indica al jugador que perdió y asimismo se actualizan sus estadísticas.

Multijugador: Este modo es muy similar al anterior, siendo que ahora otro usuario tomaría el rol de la computadora. Al igual que en el modo anterior, al inicio se le solicitar al jugador 1 que ingrese la palabra a adivinar, tras esto se le muestra al jugador 2 la palabra con guiones bajos únicamente y se le solicita que ingrese una letra que el considere pertenece a la palabra. Cabe aclarar que se valida cada ingreso para asegurar que el juego se ejecute correctamente.
Tras este ingreso sería la misma validación que en el modo contra la computadora, pero al ser una persona y no una computadora que seleccione aleatoriamente letras, el jugador 2 solo tendrá un máximo de 6 fallos como en el modo un jugador. Si el jugador 2 se queda sin intentos, se muestra la palabra que debía adivinar y se le indica al jugador 1 que ganó y al jugador 2 que perdió y se actualizan sus estadísticas. Caso contrario si el jugador 2 adivina todas las letras de la palabra, se le indica al jugador 1 que perdió y al jugador 2 que ganó y se actualizan sus estadísticas.

Al finalizar cada ejecución, se mostrará nuevamente el menú con los modos de juego.

La opción para mostrar estadísticas funciona en base a listas de diccionarios, contando de 3 valores: nombre del jugador, numero de victorias y numero de derrotas. Se cuenta con una función especifica para mostrar en el formato deseado las estadísticas de todos los jugadores. Las estadísticas se actualizan con otro método que busca en la lista un diccionario en que el nombre coincida con el del jugador a actualizar y actualiza los datos, de no existir uno con ese nombre lo crea y lo añade a la lista.

El código incluye métodos que permiten mostrar la palabra con palabras de pista para el primer modo, para definir las letras a mostrar y para reestructurar la palabra a medida que se vayan adivinando letras, además se ha gestionado el control de errores para evitar fallos o caídas en la ejecución.

La segunda opción del menú principal nos mostrará las reglas e instrucciones para la correcta ejecución del juego y la tercera opción terminará la ejecución del programa. 

Conclusiones:
A lo largo del desarrollo de este proyecto, pude aplicar de manera práctica los conocimientos adquiridos en la asignatura de programación. Diseñar e implementar un juego del ahorcado me permitió comprender mejor cómo funcionan las estructuras de control, los bucles, las condiciones y la organización modular del código.
El proceso me ayudó a reforzar la lógica de programación, a manejar distintos tipos de entradas por parte del usuario y a controlar posibles errores durante la ejecución. Además, implementar diferentes modos de juego y un sistema de estadísticas me permitió ir más allá de lo básico, agregando funcionalidades que aportan valor a la experiencia del jugador.
