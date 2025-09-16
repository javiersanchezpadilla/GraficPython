

import os
import time
import keyboard

# Definimos los caracteres de nuestro "mundo"
MURO = '#'
PISO = ' '
JUGADOR = '@'
TESORO = 'T'

# El mapa de nuestro juego, representado como una lista de listas
mapa = [
    [MURO, MURO, MURO, MURO, MURO, MURO, MURO, MURO, MURO, MURO],
    [MURO, PISO, PISO, PISO, PISO, PISO, PISO, PISO, PISO, MURO],
    [MURO, PISO, MURO, MURO, MURO, MURO, PISO, MURO, PISO, MURO],
    [MURO, PISO, PISO, PISO, PISO, MURO, PISO, MURO, PISO, MURO],
    [MURO, PISO, MURO, PISO, PISO, PISO, PISO, MURO, PISO, MURO],
    [MURO, PISO, MURO, PISO, PISO, PISO, PISO, MURO, PISO, MURO],
    [MURO, PISO, MURO, PISO, PISO, PISO, PISO, PISO, PISO, MURO],
    [MURO, PISO, PISO, PISO, PISO, PISO, PISO, PISO, TESORO, MURO],
    [MURO, MURO, MURO, MURO, MURO, MURO, MURO, MURO, MURO, MURO],
]

# Posición inicial del jugador
posicion_jugador = [1, 1]

def dibujar_mapa():
    """Limpia la pantalla y dibuja el mapa con el jugador."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Colocamos el jugador en el mapa
    fila_jugador, col_jugador = posicion_jugador
    mapa[fila_jugador][col_jugador] = JUGADOR
    
    # Imprimimos el mapa
    for fila in mapa:
        print("".join(fila))

def mover_jugador(dx, dy):
    """Mueve el jugador si la nueva posición es válida."""
    global posicion_jugador

    # Guardamos la posición actual
    fila_actual, col_actual = posicion_jugador
    
    # Calculamos la nueva posición
    fila_nueva = fila_actual + dx
    col_nueva = col_actual + dy
    
    # Verificamos si la nueva posición es un muro
    if mapa[fila_nueva][col_nueva] == MURO:
        return # No hacemos nada si es un muro

    # Limpiamos la posición anterior del jugador
    mapa[fila_actual][col_actual] = PISO
    
    # Actualizamos la posición del jugador
    posicion_jugador[0] = fila_nueva
    posicion_jugador[1] = col_nueva

def main():
    """El bucle principal del juego."""
    print("¡Bienvenido al juego de ASCII!")
    print("Mueve al @ con las flechas para encontrar la T.")
    print("Presiona ESC para salir.")

    while True:
        dibujar_mapa()
        
        # Obtenemos la tecla que el usuario presiona
        tecla = keyboard.read_key()
        
        # Lógica de movimiento
        if tecla == 'up':
            mover_jugador(-1, 0)
        elif tecla == 'down':
            mover_jugador(1, 0)
        elif tecla == 'left':
            mover_jugador(0, -1)
        elif tecla == 'right':
            mover_jugador(0, 1)
        
        # Comprobamos si el jugador ha encontrado el tesoro
        fila_jugador, col_jugador = posicion_jugador
        if mapa[fila_jugador][col_jugador] == TESORO:
            dibujar_mapa()
            print("\n¡Felicitaciones! ¡Has encontrado el tesoro!")
            break
        
        # Salir del juego
        if tecla == 'esc':
            break

# Ejecutamos el juego
if __name__ == "__main__":
    # Asegúrate de tener la biblioteca instalada
    # pip install keyboard
    main()