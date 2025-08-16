""" Le vamos a añadir un movimiento vertical general que actúe sobre todas las medusas al mismo 
    tiempo, como si una corriente marina las empujara lentamente hacia arriba y abajo."""


import glfw
from OpenGL.GL import *
import math

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

ventana = glfw.create_window(800, 600, "Cardumen con Corriente Marina", None, None)
if not ventana:
    glfw.terminate()
    raise Exception("No se pudo crear la ventana")

glfw.make_context_current(ventana)

# Colores de cada medusa
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

    # Corriente marina general (muy lenta y suave)
    corriente = math.sin(t * 0.5) * 0.2

    # Dibujar medusas
    for i in range(5):
        desfase = i * 1.2
        tiempo = t + desfase

        # Radio que respira
        radio = 0.5 + math.sin(tiempo) * 0.3

        # Movimiento circular + ondulación
        x = math.cos(tiempo) * radio
        y = math.sin(tiempo) * radio + math.sin(tiempo * 3) * 0.2

        # Aplicar corriente marina a todas
        y += corriente

        # Dibujar medusa
        glColor3f(*colores[i])
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)
        for ang in range(0, 361, 10):
            ang_rad = math.radians(ang)
            glVertex2f(x + math.cos(ang_rad) * 0.08, y + math.sin(ang_rad) * 0.08)
        glEnd()

    glfw.swap_buffers(ventana)

glfw.terminate()
