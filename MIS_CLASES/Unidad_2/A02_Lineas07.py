""" Programa que dibuja una linea en OpenGL version 7
    Esta es la version mas estructurada del programa, donde todo el codigo esta en funciones.
    En este ejemplo se dibuja las lineas mediante el uso de ciclos, creando una cuadrícula de lineas grises cada 10 unidades
    y los ejes X y Y en color blanco.
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
    """ Dibuja varias líneas en la ventana utilizando OpenGL.
        No retorna ningún valor, solo ejecuta comandos de dibujo.
        La función utiliza la función `dibuja_linea` para dibujar múltiples líneas:
        1. Una cuadrícula de líneas grises cada 10 unidades en ambos ejes X e Y.
        2. Los ejes X e Y en color blanco.
    """
    for x in range(0, 201, 10):
        dibuja_linea(x, 0, x, 150, 0.3, 0.3, 0.3)   # Dibuja lineas verticales

    for y in range(0, 151, 10):
        dibuja_linea(0, y, 200, y, 0.3, 0.3, 0.3)   # Dibuja lineas horizontales

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
