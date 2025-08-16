""" Vamos a armar un programa en Python con OpenGL donde dibujamos el 
    mismo cubo dos veces en la misma ventana:

    A la izquierda → proyección en perspectiva
    A la derecha → proyección ortográfica

    De esta manera podrás comparar ambos métodos en tiempo real.

    Qué observarás

    Izquierda (Perspectiva): El cubo se verá con profundidad realista, 
    las caras más alejadas parecerán más pequeñas.

    Derecha (Ortográfica): El cubo se verá como en un dibujo técnico, 
    sin efecto de profundidad.
"""


import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Inicializar GLFW
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(900, 450, "Comparación: Perspectiva vs Ortográfica", None, None)
glfw.make_context_current(window)

# Función para dibujar un cubo
def dibujar_cubo():
    glBegin(GL_QUADS)

    # Cara frontal
    glColor3f(1, 0, 0)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)

    # Cara trasera
    glColor3f(0, 1, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)

    # Cara superior
    glColor3f(0, 0, 1)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)

    # Cara inferior
    glColor3f(1, 1, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)

    # Cara derecha
    glColor3f(0, 1, 1)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)

    # Cara izquierda
    glColor3f(1, 0, 1)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)

    glEnd()

# Activar profundidad
glEnable(GL_DEPTH_TEST)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    ancho, alto = glfw.get_framebuffer_size(window)

    # --- Lado izquierdo: Perspectiva ---
    glViewport(0, 0, ancho // 2, alto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, ancho / (2 * alto), 0.1, 50)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

    glRotatef(glfw.get_time() * 40, 1, 1, 0)
    dibujar_cubo()

    # --- Lado derecho: Ortográfica ---
    glViewport(ancho // 2, 0, ancho // 2, alto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -5, 5)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

    glRotatef(glfw.get_time() * 40, 1, 1, 0)
    dibujar_cubo()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
