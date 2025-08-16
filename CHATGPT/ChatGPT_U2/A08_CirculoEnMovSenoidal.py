""" hora vamos a modificar el ejemplo para que el círculo se mueva de izquierda a derecha mientras 
    sube y baja formando una onda senoidal."""

import glfw
from OpenGL.GL import *
import math

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

ventana = glfw.create_window(800, 600, "Movimiento en Onda Senoidal", None, None)
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

    # Movimiento en onda
    x = (t % 4) - 2        # Avance en X de -2 a +2 (reinicio cada 4s)
    y = math.sin(t * 2) * 0.5  # Onda en Y con amplitud 0.5

    # Dibujar círculo
    glColor3f(0.2, 0.6, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  # Centro
    for ang in range(0, 361, 10):
        ang_rad = math.radians(ang)
        glVertex2f(x + math.cos(ang_rad) * 0.1, y + math.sin(ang_rad) * 0.1)
    glEnd()

    glfw.swap_buffers(ventana)

glfw.terminate()
