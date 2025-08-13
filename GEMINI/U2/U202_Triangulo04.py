""" Este ejemplo es igual al anterior, solo que ahora se crea una función
    para dibujar exclusivamente el triángulo.
    Esto nos permite reutilizar el código de la ventana y enfocarnos en el triángulo.
"""

import glfw
from OpenGL.GL import *

def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Primitivas en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana


def dibuja():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.0, 1.0) # Limpiamos a negro para que se note nuestro triángulo

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)      # Color rojo para el siguiente vértice
    glVertex2f(-0.5, -0.5)      # Vértice inferior izquierdo
    glColor3f(0.0, 1.0, 0.0)      # Color verde para el siguiente vértice
    glVertex2f(0.5, -0.5)       # Vértice inferior derecho
    glColor3f(0.0, 0.0, 1.0)      # Color azul para el siguiente vértice
    glVertex2f(0.0, 0.5)        # Vértice superior central
    glEnd()


# El bucle principal
ventana = iniciar_ventana()
while not glfw.window_should_close(ventana):
    dibuja()
    glfw.swap_buffers(ventana)
    glfw.poll_events()
glfw.terminate()
