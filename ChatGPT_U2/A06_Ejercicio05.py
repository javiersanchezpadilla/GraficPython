""" Vamos a crear nuestro Reto Nivel 2: dibujar una casa 2D en OpenGL usando 
    únicamente primitivas básicas (GL_TRIANGLES y GL_QUADS).
    Objetivo
    Usar varias primitivas en la misma escena.
    Trabajar con posicionamiento relativo usando coordenadas normalizadas.
    Aplicar colores diferenciados para cada parte de la casa."""

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
    glColor3f(0.9, 0.7, 0.5)  # Color marrón claro
    glVertex2f(-0.4, -0.5)
    glVertex2f(0.4, -0.5)
    glVertex2f(0.4, 0.0)
    glVertex2f(-0.4, 0.0)
    glEnd()

    # ---- Techo ----
    glBegin(GL_TRIANGLES)
    glColor3f(0.7, 0.2, 0.2)  # Color rojo oscuro
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
