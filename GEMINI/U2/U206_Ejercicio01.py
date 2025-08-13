""" Ejercicio práctico
    Dibuja dos triángulos de diferentes colores y colócalos lado a lado.
👉 Pista: usa glBegin(GL_TRIANGLES) dos veces o dentro del mismo bloque."""


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

# Aquí pondremos el código para dibujar primitivas
ventana = iniciar_ventana()

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.9, 0.9, 0.9, 1)  # Fondo gris claro

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)  # Rojo
    glVertex2f(-1.0, 0.0)
    glVertex2f(-0.5, 1.0)
    glVertex2f(0.0, 0.0)

    glColor3f(0, 1, 0)  # Verde
    glVertex2f(0.0, 0.0)
    glVertex2f(0.5, 1.0)
    glVertex2f(1.0, 0.0)

    glColor3f(0, 0, 1)  # Azul
    glVertex2f(0.0, 0.0)
    glVertex2f(-0.5, -0.9)
    glVertex2f(0.5, -0.9)

    glEnd()

    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
