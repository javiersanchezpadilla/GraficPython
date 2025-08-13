""" Manejo de puntos en OpenGL
    En este ejemplo creamos una función que permita definir el color y la posición de un punto.
    """


import glfw
from OpenGL.GL import *
import numpy as np      # Para manejar coordenadas de puntos con valores entre 0 y 1 (flotantes)

def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Primitivas en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana

def dibuja_punto():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0, 0, 0, 1)    # Fondo negro

    for i in np.arange(-1.0, 1.0, 0.001):
        glColor3f(1.0, 1.0, 0.0)    # Color del punto
        glBegin(GL_POINTS)
        glVertex2f(i, i)            # Coordenada de dibujo
        glEnd()


# Aquí pondremos el código para dibujar primitivas
ventana = iniciar_ventana()
while not glfw.window_should_close(ventana):
    dibuja_punto() 
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
