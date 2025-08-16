"""  fondo marino animado para que nuestras medusas naden dentro de un ambiente más realista.
    Incluiremos:

    🌊 Degradado del fondo (cielo marino)
    🪨 Suelo con rocas
    🌿 Algas que se mueven con la corriente
    🪼 Medusas flotando (usaremos las que ya hicimos)

    Qué hace este código

    Fondo degradado
    Simula profundidad del agua, más clara arriba y más oscura abajo.
    Suelo con rocas
    Añade un área inferior para dar contexto.
    Algas animadas
        Usan sin(t + y * 0.2) para moverse suavemente como con la corriente.
    Medusas
        Se mueven como en los ejemplos anteriores, pero con una corriente general vertical.
"""

import glfw
from OpenGL.GL import *
import math
import random

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

ventana = glfw.create_window(800, 600, "Fondo Marino Animado", None, None)
if not ventana:
    glfw.terminate()
    raise Exception("No se pudo crear la ventana")

glfw.make_context_current(ventana)

# Datos para medusas
colores_medusas = [
    (0.2, 1.0, 0.7),
    (1.0, 0.5, 0.3),
    (0.7, 0.3, 1.0),
    (1.0, 1.0, 0.3),
    (0.3, 0.8, 1.0)
]

# Posiciones iniciales aleatorias para medusas
offsets = [random.uniform(0, 5) for _ in range(5)]

# Función para dibujar degradado del fondo
def dibujar_fondo():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.3, 0.6)  # Azul oscuro abajo
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glColor3f(0.0, 0.6, 1.0)  # Azul claro arriba
    glVertex2f(1, 1)
    glVertex2f(-1, 1)
    glEnd()

# Función para dibujar suelo con rocas
def dibujar_suelo():
    glColor3f(0.4, 0.3, 0.2)  # Marrón
    glBegin(GL_QUADS)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(1, -0.6)
    glVertex2f(-1, -0.6)
    glEnd()

    # Rocas
    glColor3f(0.3, 0.3, 0.3)
    for x in [-0.8, -0.5, 0.0, 0.4, 0.8]:
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, -0.6)
        for ang in range(0, 361, 20):
            ang_rad = math.radians(ang)
            glVertex2f(x + math.cos(ang_rad) * 0.1, -0.6 + math.sin(ang_rad) * 0.05)
        glEnd()

# Función para dibujar algas animadas
def dibujar_algas(t):
    glColor3f(0.0, 0.8, 0.2)  # Verde
    for x in [-0.9, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8]:
        glBegin(GL_LINE_STRIP)
        for y in range(0, 40):
            yf = -0.6 + y * 0.02
            x_offset = math.sin(t + y * 0.2) * 0.02
            glVertex2f(x + x_offset, yf)
        glEnd()

# Función para dibujar medusas
def dibujar_medusas(t):
    corriente = math.sin(t * 0.5) * 0.2
    for i in range(5):
        tiempo = t + offsets[i]
        radio = 0.5 + math.sin(tiempo) * 0.3
        x = math.cos(tiempo) * radio
        y = math.sin(tiempo) * radio + math.sin(tiempo * 3) * 0.2 + corriente

        glColor3f(*colores_medusas[i])
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)
        for ang in range(0, 361, 10):
            ang_rad = math.radians(ang)
            glVertex2f(x + math.cos(ang_rad) * 0.08, y + math.sin(ang_rad) * 0.08)
        glEnd()

# Bucle principal
while not glfw.window_should_close(ventana):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    t = glfw.get_time()

    dibujar_fondo()
    dibujar_suelo()
    dibujar_algas(t)
    dibujar_medusas(t)

    glfw.swap_buffers(ventana)

glfw.terminate()
