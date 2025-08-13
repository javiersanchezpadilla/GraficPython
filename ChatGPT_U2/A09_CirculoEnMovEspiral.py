""" Ahora haremos un ejemplo donde el círculo sigue una trayectoria en espiral, combinando sin, cos
    y un radio que aumenta con el tiempo."""

import glfw
from OpenGL.GL import *
import math

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

ventana = glfw.create_window(800, 600, "Movimiento en Espiral", None, None)
if not ventana:
    glfw.terminate()
    raise Exception("No se pudo crear la ventana")

glfw.make_context_current(ventana)

# Bucle principal
while not glfw.window_should_close(ventana):
    glfw.poll_events()

    # Limpiar pantalla
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Tiempo
    t = glfw.get_time()

    # Radio que crece con el tiempo
    radio = 0.1 + (t * 0.05)  # Aumenta lentamente

    # Movimiento en espiral usando sin y cos
    x = math.cos(t * 2) * radio
    y = math.sin(t * 2) * radio

    # Dibujar círculo
    glColor3f(1, 0.5, 0.2)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  # Centro
    for ang in range(0, 361, 10):
        ang_rad = math.radians(ang)
        glVertex2f(x + math.cos(ang_rad) * 0.1, y + math.sin(ang_rad) * 0.1)
    glEnd()

    glfw.swap_buffers(ventana)

glfw.terminate()
