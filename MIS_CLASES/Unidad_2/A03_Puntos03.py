""" GL_POINTS   Primitiva PUNTO. 
    glPointSize(tamaño)     Permite definir el tamaño del punto (en pixeles).

    En este ejemplo dibujamos varios puntos rojos de diferentes tamaños en la ventana.
    Para generar una secuencia de números decimales, no podemos usar la funcion range()
    podemos usar la función arange() de la biblioteca NumPy o escribir un bucle while 
    que maneje el incremento decimal, para este programa usaremos el ciclo while.
        
    Las coordenadas están normalizadas: X e Y van de -1 a 1.
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


def dibuja_punto(x, y, size):
    """ Dibuja un punto en las coordenadas (x, y) con el tamaño especificado.
        :param x: Coordenada X del punto (de -1 a 1)
        :param y: Coordenada Y del punto (de -1 a 1)
        :param size: Tamaño del punto en píxeles
    """
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def dibuja_varios_puntos():
    """ Dibuja varios puntos de diferentes tamaños y colores a lo largo del eje X. """
    glColor3f(1, 0, 0)                  # Color rojo
    tamanio_punto = 1
    pos_x = -0.9
    while pos_x <= 0.9:
        dibuja_punto(pos_x, 0.0, tamanio_punto)
        pos_x += 0.1
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
