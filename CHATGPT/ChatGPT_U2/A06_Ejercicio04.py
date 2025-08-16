""" Ejercicio extra
    Cambia los colores para hacer un degradado dentro de cada triángulo:
    Basta con cambiar glColor3f() antes de cada vértice."""

""" Continuamos con un ejemplo de OpenGL en Python.
    dibujar dos triángulos de diferentes colores y colocarlos lado a lado usando 
    primitivas de OpenGL."""

import glfw
from OpenGL.GL import *

# Función para iniciar la ventana
def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Reto: Dos Triángulos", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana

# Crear ventana
ventana = iniciar_ventana()

# Bucle principal
while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.9, 0.9, 0.9, 1)  # Fondo gris claro

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

    glfw.swap_buffers(ventana)
    glfw.poll_events()

# Cerrar
glfw.terminate()
