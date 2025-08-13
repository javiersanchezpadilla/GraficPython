""" Esta función inicializa una ventana OpenGL usando GLFW.
    La estemos utilizando para dibujar primitivas en OpenGL."""

import glfw
from OpenGL.GL import *

def iniciar_ventana():
    """
    The function `iniciar_ventana` initializes a GLFW window with specified dimensions and title in
    Python.
    :return: The function `iniciar_ventana` is returning the GLFW window object `ventana`.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Primitivas en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana


# Aquí pondremos el código para dibujar primitivas

ventana = iniciar_ventana()
while not glfw.window_should_close(ventana):

    glClear(GL_COLOR_BUFFER_BIT)

    # Aqui ponemos todo loque se desee

    glfw.swap_buffers(ventana)
    glfw.poll_events()

# Terminamos el programa y cerramos todo
glfw.terminate()
