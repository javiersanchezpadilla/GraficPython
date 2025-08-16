""" patrón de espiral “respirando”, donde el radio no crece indefinidamente, sino que se expande 
    y se contrae como si la espiral estuviera viva."""

import glfw
from OpenGL.GL import *
import math

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

ventana = glfw.create_window(800, 600, "Espiral Respirando", None, None)
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

    # Radio que oscila (0.2 a 0.8)
    radio = 0.5 + math.sin(t) * 0.3

    # Movimiento circular usando el radio oscilante
    x = math.cos(t * 2) * radio
    y = math.sin(t * 2) * radio

    # Dibujar círculo
    glColor3f(0.9, 0.3, 0.8)  # Color morado-rosado
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  # Centro
    for ang in range(0, 361, 10):
        ang_rad = math.radians(ang)
        glVertex2f(x + math.cos(ang_rad) * 0.1, y + math.sin(ang_rad) * 0.1)
    glEnd()

    glfw.swap_buffers(ventana)

glfw.terminate()

