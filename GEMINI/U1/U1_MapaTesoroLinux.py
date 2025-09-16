import curses
import os
import time

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

def dibujar_mapa(stdscr):
    """Dibuja el mapa con el jugador en la pantalla de curses."""
    stdscr.clear()
    
    # Colocamos el jugador en el mapa
    fila_jugador, col_jugador = posicion_jugador
    mapa[fila_jugador][col_jugador] = JUGADOR
    
    # Imprimimos el mapa en la pantalla de curses
    for i, fila in enumerate(mapa):
        stdscr.addstr(i, 0, "".join(fila))

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
        return

    # Limpiamos la posición anterior del jugador
    mapa[fila_actual][col_actual] = PISO
    
    # Actualizamos la posición del jugador
    posicion_jugador[0] = fila_nueva
    posicion_jugador[1] = col_nueva

def game_loop(stdscr):
    """El bucle principal del juego, adaptado para curses."""
    curses.curs_set(0)  # Ocultamos el cursor
    stdscr.nodelay(True)  # No esperamos por una tecla
    
    dibujar_mapa(stdscr)
    stdscr.refresh()
    
    while True:
        try:
            tecla = stdscr.getch()
        except:
            tecla = -1  # No se ha presionado ninguna tecla
            
        # Lógica de movimiento
        if tecla == curses.KEY_UP:
            mover_jugador(-1, 0)
        elif tecla == curses.KEY_DOWN:
            mover_jugador(1, 0)
        elif tecla == curses.KEY_LEFT:
            mover_jugador(0, -1)
        elif tecla == curses.KEY_RIGHT:
            mover_jugador(0, 1)
        elif tecla == 27:  # Código ASCII para la tecla ESC
            break
        
        dibujar_mapa(stdscr)
        
        # Comprobamos si el jugador ha encontrado el tesoro
        fila_jugador, col_jugador = posicion_jugador
        if mapa[fila_jugador][col_jugador] == TESORO:
            dibujar_mapa(stdscr)
            stdscr.addstr(len(mapa) + 1, 0, "\n¡Felicitaciones! ¡Has encontrado el tesoro!")
            stdscr.refresh()
            time.sleep(3)  # Damos tiempo al usuario para ver el mensaje
            break
        
        stdscr.refresh()
        time.sleep(0.1)  # Pequeña pausa para controlar la velocidad del juego

# Ejecutamos el juego
if __name__ == "__main__":
    curses.wrapper(game_loop)