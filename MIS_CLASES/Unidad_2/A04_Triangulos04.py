""" En este ejercicio se dibujaran dos triangulos de diferentes colores usando la primitiva 
    GL_TRIANGLES.
    Cada triangulo estara formado por tres vertices y cada uno de ellos tendra un color 
    diferente.
    Los triangulos se dibujaran en el centro de la ventana.
    El fondo de la ventana sera de color gris claro.
    Lo interesante es que dentro de un mismos bloque glBegin(GL_TRIANGLES) y glEnd() podemos 
    definir varios triangulos.
    cada triangulo requiere tres vertices.
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


def dibuja_triangulos():
    """ Dibuja tres triangulos de diferentes colores en el centro de la ventana."""
    
    # Triángulo izquierdo (rojo)
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)  # Rojo
    glVertex2f(-0.8, -0.5)
    glColor3f(0, 1, 0)  # Verde
    glVertex2f(-0.2, -0.5)
    glColor3f(0, 0, 1)  # Azul
    glVertex2f(-0.5,  0.2)
    glEnd()

    # Triángulo derecho (azul)
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)  # Amarillo
    glVertex2f(0.2, -0.5)
    glColor3f(0, 1, 1)  # Cyan
    glVertex2f(0.8, -0.5)
    glColor3f(1, 0, 1)  # Magenta
    glVertex2f(0.5,  0.2)
    glEnd()


if __name__ == "__main__":
    ventana = iniciar_ventana()
    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.9, 0.9, 0.9, 1)  # Fondo gris claro
        dibuja_triangulos()
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
