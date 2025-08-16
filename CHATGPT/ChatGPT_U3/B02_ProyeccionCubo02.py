""" Hagamos el mismo ejemplo del cubo, pero ahora usando proyección ortográfica 
    en lugar de perspectiva. Así vas a notar clarísimo la diferencia.
    
    
    
    
    """

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Inicializar GLFW
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(700, 700, "Proyección Ortográfica", None, None)
glfw.make_context_current(window)

# Dibujar un cubo con colores diferentes en cada cara
def dibujar_cubo():
    glBegin(GL_QUADS)

    # Cara frontal (roja)
    glColor3f(1, 0, 0)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)

    # Cara trasera (verde)
    glColor3f(0, 1, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)

    # Cara superior (azul)
    glColor3f(0, 0, 1)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)

    # Cara inferior (amarilla)
    glColor3f(1, 1, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)

    # Cara derecha (cian)
    glColor3f(0, 1, 1)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)

    # Cara izquierda (magenta)
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

    # --- Proyección ORTOGRÁFICA ---
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -5, 5)  # izq, der, abajo, arriba, cerca, lejos

    # --- Cámara fija ---
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2, 2, 2,   # posición de la cámara
              0, 0, 0,   # hacia dónde mira
              0, 1, 0)   # vector "arriba"

    # --- Rotar el cubo ---
    tiempo = glfw.get_time()
    glRotatef(tiempo * 40, 1, 1, 0)
    dibujar_cubo()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
