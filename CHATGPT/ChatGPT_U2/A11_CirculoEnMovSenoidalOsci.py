""" Vamos a combinar onda senoidal + radio oscilante, para que el círculo se mueva como una 
    medusa flotando o una partícula orgánica en el agua.

    Explicación del movimiento
    Radio oscilante
        radio = 0.5 + sin(t) * 0.3 → la distancia al centro sube y baja, dando efecto de “respiración”.
        Movimiento horizontal
        x = cos(t) * radio → gira en un círculo modificado por el radio cambiante.
    Movimiento vertical combinado
        y = sin(t) * radio → parte del movimiento circular.
        + sin(t * 3) * 0.2 → pequeña ondulación vertical más rápida que simula un vaivén natural.
    Efecto final
        El círculo se desplaza de forma impredecible pero suave, parecido al desplazamiento de una 
        criatura marina.
    
    """

import glfw
from OpenGL.GL import *
import math

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

ventana = glfw.create_window(800, 600, "Movimiento tipo Medusa", None, None)
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

    # Radio que oscila suavemente (efecto de respiración)
    radio = 0.5 + math.sin(t) * 0.3

    # Movimiento circular
    x = math.cos(t) * radio

    # Combinamos con onda senoidal para Y
    y = math.sin(t) * radio + math.sin(t * 3) * 0.2

    # Dibujar círculo
    glColor3f(0.2, 1.0, 0.7)  # Verde agua
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  # Centro
    for ang in range(0, 361, 10):
        ang_rad = math.radians(ang)
        glVertex2f(x + math.cos(ang_rad) * 0.1, y + math.sin(ang_rad) * 0.1)
    glEnd()

    glfw.swap_buffers(ventana)

glfw.terminate()

