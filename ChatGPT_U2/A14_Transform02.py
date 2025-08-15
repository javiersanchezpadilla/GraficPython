""" Sistema Solar en 2D usando transformaciones independientes con glPushMatrix() y glPopMatrix().

    Esto nos permitirá:
    Tener un Sol fijo en el centro.
    Planetas que orbitan alrededor del Sol.
    Cada planeta rota sobre sí mismo.
    Opcional: una luna que orbita a un planeta.

    Conceptos clave

    Jerarquía de transformaciones:
    Usamos glPushMatrix() y glPopMatrix() para aislar movimientos.

    Rotación para órbita:
    glRotatef(tiempo * velocidad_orbita, 0, 0, 1)

    Traslación para distancia:
    glTranslatef(distancia, 0, 0)

    Rotación propia:
    glRotatef(tiempo * velocidad_rotacion, 0, 0, 1)
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

def dibujar_circulo(radio, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for ang in range(0, 361, 10):
        ang_rad = math.radians(ang)
        glVertex2f(math.cos(ang_rad) * radio, math.sin(ang_rad) * radio)
    glEnd()


# Aquí pondremos el código para dibujar primitivas
ventana = iniciar_ventana()

while not glfw.window_should_close(ventana):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    tiempo = glfw.get_time()

    # ☀️ Sol en el centro
    glPushMatrix()
    dibujar_circulo(0.2, 1.0, 0.8, 0.0)  # Amarillo
    glPopMatrix()

    # 🌍 Planeta que orbita
    glPushMatrix()
    glRotatef(tiempo * 30, 0, 0, 1)  # Órbita
    glTranslatef(0.6, 0, 0)  # Distancia al sol
    glRotatef(tiempo * 100, 0, 0, 1)  # Rotación sobre sí mismo
    dibujar_circulo(0.08, 0.0, 0.5, 1.0)  # Azul
    glPopMatrix()

    # 🪐 Planeta con luna
    glPushMatrix()
    glRotatef(tiempo * 20, 0, 0, 1)  # Órbita
    glTranslatef(1.0, 0, 0)  # Distancia al sol
    glRotatef(tiempo * 60, 0, 0, 1)  # Rotación propia
    dibujar_circulo(0.1, 0.8, 0.3, 0.0)  # Marrón

    # 🌙 Luna
    glPushMatrix()
    glRotatef(tiempo * 200, 0, 0, 1)  # Órbita de la luna
    glTranslatef(0.2, 0, 0)
    dibujar_circulo(0.03, 0.8, 0.8, 0.8)  # Gris
    glPopMatrix()

    glPopMatrix()

    glfw.swap_buffers(ventana)

glfw.terminate()
