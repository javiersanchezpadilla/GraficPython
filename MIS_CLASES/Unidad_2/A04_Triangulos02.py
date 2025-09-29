""" En este ejercicio dibujaremos un triangulo en el centro de la pantalla.
    Usa coordenadas normalizadas.
    Aplica colores distintos para cada vertice del triangulo, lo que nos permitira ver un degradado de colores.
    Usar funciones para organizar el codigo.

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
    ventana = glfw.create_window(800, 600, "Primitiva Triangulo", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


def dibuja_triangulo():
    """ Funcion que dibuja un triangulo en el centro de la pantalla. """     
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)  # Color rojo
    glVertex2f(0, 0.5)  # Vertice superior
    glColor3f(0, 1, 0)  # Color verde
    glVertex2f(-0.5, -0.5)  # Vertice inferior izquierdo
    glColor3f(0, 0, 1)  # Color azul
    glVertex2f(0.5, -0.5)  # Vertice inferior derecho
    glEnd()


if __name__ == "__main__":
    ventana = iniciar_ventana()
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        dibuja_triangulo()         
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
