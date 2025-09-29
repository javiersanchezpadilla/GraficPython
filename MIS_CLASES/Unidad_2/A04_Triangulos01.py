""" En este ejercicio dibujaremos un triangulo en el centro de la pantalla.
    Usa coordenadas normalizadas.
    Aplica fondo rojo y el triangulo de color blanco
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


if __name__ == "__main__":
    ventana = iniciar_ventana()
    while not glfw.window_should_close(ventana):
        glClearColor(1.0, 0.0, 0.0, 1.0)    # Establece el color de limpieza a rojo
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
        glVertex2f(0.5, -0.5)   # Vértice inferior derecho
        glVertex2f(0.0, 0.5)    # Vértice superior central
        glEnd()
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
