""" Vamos a modificar el código para que cada medusa emita una burbuja que sube desde 
    su posición.
    Estas burbujas serán independientes de las burbujas del fondo.
    
    Cambios clave

    burbujas_medusas → lista que guarda una burbuja por medusa.
    En dibujar_medusas() actualizamos la posición de cada burbuja para que salga justo debajo.
    dibujar_burbujas_medusas() mueve cada burbuja hacia arriba y la reinicia en su medusa 
    cuando llega arriba.
    """

import glfw
from OpenGL.GL import *
import math
import random

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

ventana = glfw.create_window(800, 600, "Medusas con burbujas propias", None, None)
if not ventana:
    glfw.terminate()
    raise Exception("No se pudo crear la ventana")

glfw.make_context_current(ventana)

# Datos de medusas
colores_medusas = [
    (0.2, 1.0, 0.7),
    (1.0, 0.5, 0.3),
    (0.7, 0.3, 1.0),
    (1.0, 1.0, 0.3),
    (0.3, 0.8, 1.0)
]
offsets_medusas = [random.uniform(0, 5) for _ in range(5)]

# Datos de burbujas del fondo
burbujas_fondo = [
    {"x": random.uniform(-1, 1), "y": random.uniform(-1, 1), "r": random.uniform(0.01, 0.04), "vel": random.uniform(0.1, 0.3)}
    for _ in range(15)
]

# Burbujas que salen de medusas
burbujas_medusas = [
    {"x": 0, "y": -1, "r": 0.02, "vel": 0.25} for _ in range(5)
]

# Oscilación independiente de algas
algas_offsets = [random.uniform(0, 2*math.pi) for _ in range(7)]

# ---- Funciones de dibujo ----

def dibujar_fondo():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.3, 0.6)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glColor3f(0.0, 0.6, 1.0)
    glVertex2f(1, 1)
    glVertex2f(-1, 1)
    glEnd()

def dibujar_suelo():
    glColor3f(0.4, 0.3, 0.2)
    glBegin(GL_QUADS)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(1, -0.6)
    glVertex2f(-1, -0.6)
    glEnd()

    glColor3f(0.3, 0.3, 0.3)
    for x in [-0.8, -0.5, 0.0, 0.4, 0.8]:
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, -0.6)
        for ang in range(0, 361, 20):
            ang_rad = math.radians(ang)
            glVertex2f(x + math.cos(ang_rad) * 0.1, -0.6 + math.sin(ang_rad) * 0.05)
        glEnd()

def dibujar_algas(t):
    glColor3f(0.0, 0.8, 0.2)
    for idx, x in enumerate([-0.9, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8]):
        glBegin(GL_LINE_STRIP)
        for y in range(0, 40):
            yf = -0.6 + y * 0.02
            x_offset = math.sin(t + algas_offsets[idx] + y * 0.2) * 0.02
            glVertex2f(x + x_offset, yf)
        glEnd()

def dibujar_burbujas_fondo():
    glColor3f(0.8, 0.9, 1.0)
    for burbuja in burbujas_fondo:
        burbuja["y"] += burbuja["vel"] * 0.01
        if burbuja["y"] > 1.1:
            burbuja["y"] = -1
            burbuja["x"] = random.uniform(-1, 1)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(burbuja["x"], burbuja["y"])
        for ang in range(0, 361, 15):
            ang_rad = math.radians(ang)
            glVertex2f(burbuja["x"] + math.cos(ang_rad) * burbuja["r"],
                       burbuja["y"] + math.sin(ang_rad) * burbuja["r"])
        glEnd()

def dibujar_medusas(t):
    corriente = math.sin(t * 0.5) * 0.2
    for i in range(5):
        tiempo = t + offsets_medusas[i]
        radio = 0.5 + math.sin(tiempo) * 0.3
        x = math.cos(tiempo) * radio
        y = math.sin(tiempo) * radio + math.sin(tiempo * 3) * 0.2 + corriente

        # Guardar posición de medusa para su burbuja
        burbujas_medusas[i]["x"] = x
        burbujas_medusas[i]["y"] = y - 0.1  # Sale de abajo

        glColor3f(*colores_medusas[i])
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)
        for ang in range(0, 361, 10):
            ang_rad = math.radians(ang)
            glVertex2f(x + math.cos(ang_rad) * 0.08, y + math.sin(ang_rad) * 0.08)
        glEnd()

def dibujar_burbujas_medusas():
    glColor3f(0.8, 0.9, 1.0)
    for burbuja in burbujas_medusas:
        burbuja["y"] += burbuja["vel"] * 0.01
        if burbuja["y"] > 1.1:
            # Reaparece desde su medusa correspondiente
            idx = burbujas_medusas.index(burbuja)
            burbuja["y"] = burbujas_medusas[idx]["y"] - 0.1
            burbuja["x"] = burbujas_medusas[idx]["x"]

        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(burbuja["x"], burbuja["y"])
        for ang in range(0, 361, 15):
            ang_rad = math.radians(ang)
            glVertex2f(burbuja["x"] + math.cos(ang_rad) * burbuja["r"],
                       burbuja["y"] + math.sin(ang_rad) * burbuja["r"])
        glEnd()

# ---- Bucle principal ----
while not glfw.window_should_close(ventana):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    t = glfw.get_time()

    dibujar_fondo()
    dibujar_suelo()
    dibujar_algas(t)
    dibujar_burbujas_fondo()
    dibujar_medusas(t)
    dibujar_burbujas_medusas()

    glfw.swap_buffers(ventana)

glfw.terminate()

