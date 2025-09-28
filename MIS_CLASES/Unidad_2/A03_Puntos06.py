""" En este ejercicio dibujaremos muchos puntos de forma aleatoria. 
    Comunmente se han colocado las siguientes instrucciones dentro del ciclo principal.

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    Pero en este caso no quiero que se borre la pantalla en cada iteracion,
    por lo que las he colocado antes del ciclo while.
"""

import glfw
from OpenGL.GL import *
import random


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


def dibuja_puntos():
    """ Dibuja muchos puntos en posiciones aleatorias con colores aleatorios. """     
    for i in range(1000):
        glColor3f(random.random(), random.random(), random.random())  # Color aleatorio del punto
        valor_x = random.random() * 2 - 1   # Genera un valor entre -1 y 1
        valor_y = random.random() * 2 - 1   # Genera un valor entre -1 y 1
        glBegin(GL_POINTS)
        glVertex2f(valor_x, valor_y)  # Coordenada de dibujo
        glEnd()


if __name__ == "__main__":
    ventana = iniciar_ventana()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    while not glfw.window_should_close(ventana):
        dibuja_puntos()         
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
