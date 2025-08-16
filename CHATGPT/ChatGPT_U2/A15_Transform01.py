""" En esta etapa vamos a aprender a combinar traslación, rotación y escalado para 
    armar escenas con varios objetos, cada uno con su propio comportamiento.

    Ejemplo práctico que haremos:
    🌍 Un planeta con su luna que lo orbita, mientras ambos giran alrededor del Sol.

    Conceptos clave

    1.  Uso de glPushMatrix y glPopMatrix
        Guardamos y recuperamos la transformación actual para no “contaminar” a los demás 
        objetos.
        Ejemplo: la Luna gira con el planeta, pero no afecta al Sol.
    2.  Transformaciones jerárquicas
        El planeta depende del Sol.
        La Luna depende del planeta.
        Esto es lo mismo que animación “esquelética” en 3D (padre → hijo → nieto).
    3.  Escalado (que veremos luego) permite hacer objetos más grandes o más pequeños sin 
        cambiar su sistema de referencia.

"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Inicialización de GLFW
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(700, 700, "Transformaciones combinadas", None, None)
glfw.make_context_current(window)

def dibujar_circulo(radio, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # centro
    for ang in range(361):
        rad = math.radians(ang)
        glVertex2f(math.cos(rad) * radio, math.sin(rad) * radio)
    glEnd()

# Bucle principal
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    tiempo = glfw.get_time()

    # --- Sol ---
    glPushMatrix()
    dibujar_circulo(0.2, (1, 1, 0))  # Amarillo
    glPopMatrix()

    # --- Planeta orbitando el Sol ---
    glPushMatrix()
    glRotatef(tiempo * 20, 0, 0, 1)   # órbita alrededor del sol
    glTranslatef(0.6, 0, 0)           # distancia del planeta
    glRotatef(tiempo * 60, 0, 0, 1)   # rotación sobre sí mismo
    dibujar_circulo(0.1, (0, 0, 1))   # Azul
       
    # --- Luna orbitando el planeta ---
    glPushMatrix()
    glRotatef(tiempo * 120, 0, 0, 1)  # órbita alrededor del planeta
    glTranslatef(0.2, 0, 0)           # distancia de la luna
    dibujar_circulo(0.05, (0.8, 0.8, 0.8))  # Gris
    glPopMatrix()

    glPopMatrix()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
