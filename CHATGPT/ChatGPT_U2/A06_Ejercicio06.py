""" Ejercicios extra
    Cambia el color del techo a verde y la pared a amarillo.
    Haz que las ventanas tengan marcos dibujando un cuadrado extra alrededor de ellas.
    Añade un sol en la esquina superior derecha usando GL_TRIANGLE_FAN."""

import glfw
from OpenGL.GL import *

# Inicializar ventana
def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Casa 2D con primitivas", None, None)
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

    glfw.swap_buffers(ventana)  # Intercala los buffers
    glfw.poll_events()          # Procesa eventos

glfw.terminate()
