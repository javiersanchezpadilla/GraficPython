""" círculo moviéndose usando sin y cos, para que veas claramente cómo las funciones matemáticas 
    controlan el movimiento.


"""

import glfw
from OpenGL.GL import *
import math

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

ventana = glfw.create_window(800, 600, "Movimiento con sin y cos", None, None)
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

    # Obtener tiempo en segundos
    t = glfw.get_time()

    # Calcular posición con sin y cos
    radio = 0.5
    x = math.cos(t) * radio
    y = math.sin(t) * radio

    # Dibujar el "sol"
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  # centro
    for ang in range(0, 361, 10):
        ang_rad = math.radians(ang)
        glVertex2f(x + math.cos(ang_rad) * 0.1, y + math.sin(ang_rad) * 0.1)
    glEnd()

    # Mostrar en pantalla
    glfw.swap_buffers(ventana)

glfw.terminate()
