""" versión interactiva:
    Un solo cubo en pantalla.
    Con la tecla ESPACIO podrás alternar entre proyección perspectiva y 
    ortográfica en tiempo real.

    Cómo probarlo

    Ejecuta el programa.
    Verás el cubo girando en pantalla.
    Presiona ESPACIO para alternar entre: Perspectiva (realista)
    Ortográfica (técnica, sin profundidad)
"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Inicializar GLFW
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(600, 600, "Alternar Perspectiva / Ortográfica", None, None)
glfw.make_context_current(window)

# Estado de la proyección
modo_perspectiva = True

def key_callback(window, key, scancode, action, mods):
    global modo_perspectiva
    if key == glfw.KEY_SPACE and action == glfw.PRESS:
        modo_perspectiva = not modo_perspectiva  # Alternar modo

glfw.set_key_callback(window, key_callback)

# Función para dibujar un cubo
def dibujar_cubo():
    glBegin(GL_QUADS)

    # Cara frontal (rojo)
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

    # Cara inferior (amarillo)
    glColor3f(1, 1, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)

    # Cara derecha (cyan)
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

# Activar buffer de profundidad
glEnable(GL_DEPTH_TEST)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    ancho, alto = glfw.get_framebuffer_size(window)

    # --- Configurar proyección ---
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if modo_perspectiva:
        gluPerspective(60, ancho / alto, 0.1, 50)   # Perspectiva
    else:
        glOrtho(-2, 2, -2, 2, -5, 5)                 # Ortográfica

    # --- Cámara ---
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

    # Rotación animada
    glRotatef(glfw.get_time() * 40, 1, 1, 0)
    dibujar_cubo()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
