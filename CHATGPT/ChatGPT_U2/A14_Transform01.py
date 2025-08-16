""" Transformaciones: un cuadro que rota, escala y se mueve suavemente
    Lo que pasa en este ejemplo

    glPushMatrix() guarda la matriz de transformación actual.
    Aplicamos traslación, rotación y escalado al cuadrado.
    Lo dibujamos ya transformado.
    glPopMatrix() restaura la matriz para que otros objetos no hereden 
    estas transformaciones.
"""

import glfw
from OpenGL.GL import *
import math


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Primitivas en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana


def dibujar_cuadrado():
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2f(-0.2, -0.2)
    glColor3f(0, 1, 0)
    glVertex2f(0.2, -0.2)
    glColor3f(0, 0, 1)
    glVertex2f(0.2, 0.2)
    glColor3f(1, 1, 0)
    glVertex2f(-0.2, 0.2)
    glEnd()



# Aquí pondremos el código para dibujar primitivas
ventana = iniciar_ventana()

while not glfw.window_should_close(ventana):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    tiempo = glfw.get_time()

    # Guardamos el estado inicial de la matriz
    glPushMatrix()

    # Transformaciones
    glTranslatef(math.sin(tiempo) * 0.5, math.cos(tiempo) * 0.5, 0)  # movimiento circular
    glRotatef(tiempo * 50, 0, 0, 1)  # rotación constante
    glScalef(abs(math.sin(tiempo)) + 0.5, abs(math.sin(tiempo)) + 0.5, 1)  # escala pulsante

    # Dibujar cuadrado transformado
    dibujar_cuadrado()

    # Restauramos la matriz original
    glPopMatrix()

    glfw.swap_buffers(ventana)

glfw.terminate()


