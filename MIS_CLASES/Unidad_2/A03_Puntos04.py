""" GL_POINTS   Primitiva PUNTO. 
    glPointSize(tamaño)     Permite definir el tamaño del punto (en pixeles).

    Este ejemplo es igual al anterior, solamente que ahora los puntos se dibujaran
    usando distintos colores y ademas usaremos arange de la libreria NumPy.
    Con este ejemplo se podrá entender que la ejecución de un programa en OpenGL
    es un ciclo infinito, donde se dibuja, se actualiza la ventana y se procesan los eventos.
       
    Las coordenadas están normalizadas: X e Y van de -1 a 1.
    """

import glfw
import numpy as np
import random as rnd
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


def dibuja_punto(x, y, size):
    """ Dibuja un punto en las coordenadas (x, y) con el tamaño especificado.
        :param x: Coordenada X del punto (de -1 a 1)
        :param y: Coordenada Y del punto (de -1 a 1)
        :param size: Tamaño del punto en píxeles
    """
    glColor3f(rnd.random(), rnd.random(), rnd.random())
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def dibuja_varios_puntos():
    """ Dibuja varios puntos de diferentes tamaños y colores a lo largo del eje X. """
    glColor3f(1, 0, 0)                  # Color rojo
    tamanio_punto = 1
    for pos_x in np.arange(-0.9, 1.0, 0.1):
        dibuja_punto(pos_x, 0.0, tamanio_punto)
        tamanio_punto += 1


if __name__ == "__main__":
    ventana = iniciar_ventana()
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        dibuja_varios_puntos()         
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
