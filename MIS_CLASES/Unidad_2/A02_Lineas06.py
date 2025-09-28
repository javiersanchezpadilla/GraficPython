""" Programa que dibuja una linea en OpenGL version 6
    Esta es la version mas estructurada del programa, donde todo el codigo esta en funciones.
    En este ejemplo se dibuja cuatro lineas de distintos colores que cruzan la ventana y los ejes X y Y en color blanco.
    Lo importante en este ejemplo es que se muestra como crear una función para dibujar lineas, la cual es invocada varias veces.
    desde lo que sería el "main loop" del programa.
"""

import glfw
from OpenGL.GL import *


def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Mi primera ventana como funcion en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


def proyeccion():
    """ Esta función configura la matriz de proyección para definir el espacio de coordenadas
        que vamos a utilizar para dibujar en la ventana.
        No retorna ningún valor, solo configura el estado de OpenGL.
        La función establece un sistema de coordenadas 2D donde el origen (0,0) está en la esquina
        inferior izquierda, el eje X va de 0 a 200 y el eje Y va de 0 a 150.
        Esto significa que cualquier cosa que dibujemos usando estas coordenadas se ajustará a este
        rango dentro de la ventana.
    """
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 200.0, 0.0, 150.0, -1.0, 1.0) 
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def dibuja_linea(x1, y1, x2, y2, rojo, verde, azul):
    """ Dibuja una línea desde el punto (x1, y1) hasta el punto (x2, y2) con el color especificado.
        Parámetros:
        - x1, y1: Coordenadas del primer punto de la línea.
        - x2, y2: Coordenadas del segundo punto de la línea.
        - rojo, verde, azul: Componentes del color de la línea (valores entre 0.0 y 1.0).
    """
    glColor3f(rojo, verde, azul)  # Fija el color para dibujar
    glBegin(GL_LINES)
    glVertex2i(x1, y1)
    glVertex2i(x2, y2)
    glEnd()


def segmento_de_linea():
    dibuja_linea(0, 0, 200, 150, 1.0, 1.0, 0.0)  # Fija color amarillo
    dibuja_linea(200, 0, 0, 150, 0.0, 1.0, 0.0)  # Fija color verde
    dibuja_linea(0, 75, 200, 75, 0.0, 0.0, 1.0)  # Fija color azul
    dibuja_linea(100, 0, 100, 150, 1.0, 0.0, 1.0)  # Fija color magenta
    # Dibuja los ejes X y Y en color blanco
    dibuja_linea(0, 75, 200, 75, 1.0, 1.0, 1.0)  # Eje X
    dibuja_linea(100, 0, 100, 150, 1.0, 1.0, 1.0)  # Eje Y


if __name__ == "__main__":
    ventana = iniciar_ventana()
    proyeccion()
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        segmento_de_linea()
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
