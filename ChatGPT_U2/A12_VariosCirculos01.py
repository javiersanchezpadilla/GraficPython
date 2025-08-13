""" Ahora vamos a agregar varios círculos, cada uno con un desfase de tiempo distinto, 
    para que se muevan como un cardumen o grupo de medusas flotando."""

import glfw
from OpenGL.GL import *
import math

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

ventana = glfw.create_window(800, 600, "Cardumen de Medusas", None, None)
if not ventana:
    glfw.terminate()
    raise Exception("No se pudo crear la ventana")

glfw.make_context_current(ventana)

# Colores para cada medusa
colores = [
    (0.2, 1.0, 0.7),
    (1.0, 0.5, 0.3),
    (0.7, 0.3, 1.0),
    (1.0, 1.0, 0.3),
    (0.3, 0.8, 1.0)
]

# Bucle principal
while not glfw.window_should_close(ventana):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Tiempo global
    t = glfw.get_time()

    # Dibujar varias medusas
    for i in range(5):
        desfase = i * 1.2  # Cada medusa empieza en un tiempo distinto
        tiempo = t + desfase

        # Radio oscilante
        radio = 0.5 + math.sin(tiempo) * 0.3

        # Movimiento con ondulación
        x = math.cos(tiempo) * radio
        y = math.sin(tiempo) * radio + math.sin(tiempo * 3) * 0.2

        # Dibujar círculo
        glColor3f(*colores[i])
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)
        for ang in range(0, 361, 10):
            ang_rad = math.radians(ang)
            glVertex2f(x + math.cos(ang_rad) * 0.08, y + math.sin(ang_rad) * 0.08)
        glEnd()

    glfw.swap_buffers(ventana)

glfw.terminate()
