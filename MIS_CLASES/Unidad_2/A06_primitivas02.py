""" En este ejercicio dibujaremos una casa sencilla usando las primitivas GL_QUADS y GL_TRIANGLES.
    La casa estara formada por una pared principal, un techo, una puerta y dos ventanas.
    Cada parte de la casa tendra un color diferente.
    El fondo de la ventana sera de color celeste (cielo).
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


def dibuja():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.8, 0.9, 1.0, 1)  # Fondo celeste (cielo)

    # ---- Pared principal ----
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0.5)  # Color amarillo
    glVertex2f(-0.4, -0.5)
    glVertex2f(0.4, -0.5)
    glVertex2f(0.4, 0.0)
    glVertex2f(-0.4, 0.0)
    glEnd()

    # ---- Techo ----
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.2, 0.0)  # Color rojo oscuro
    glVertex2f(-0.45, 0.0)
    glVertex2f(0.45, 0.0)
    glVertex2f(0.0, 0.4)
    glEnd()

    # ---- Puerta ----
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.3, 0.1)  # Marrón oscuro
    glVertex2f(-0.1, -0.5)
    glVertex2f(0.1, -0.5)
    glVertex2f(0.1, -0.2)
    glVertex2f(-0.1, -0.2)
    glEnd()

    # ---- Marco de la Puerta ----
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.0, 0.0)  # Marrón oscuro
    glVertex2f(-0.2, -0.5)
    glVertex2f(0.2, -0.5)
    glVertex2f(0.2, -0.2)
    glVertex2f(-0.2, -0.2)
    glEnd()

    # ---- Ventana izquierda ----
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.8, 1.0)  # Azul claro (vidrio)
    glVertex2f(-0.35, -0.1)
    glVertex2f(-0.15, -0.1)
    glVertex2f(-0.15, 0.1)
    glVertex2f(-0.35, 0.1)
    glEnd()

    # ---- Ventana derecha ----
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.8, 1.0)
    glVertex2f(0.15, -0.1)
    glVertex2f(0.35, -0.1)
    glVertex2f(0.35, 0.1)
    glVertex2f(0.15, 0.1)
    glEnd()


if __name__ == "__main__":
    ventana = iniciar_ventana()
    glClearColor(0.3, 0.3, 0.3, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    while not glfw.window_should_close(ventana):
        dibuja()         
        glfw.swap_buffers(ventana)  # intercala los buffers
        glfw.poll_events()          # procesa eventos

    glfw.terminate()
