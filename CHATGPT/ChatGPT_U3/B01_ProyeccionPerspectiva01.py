""" Ejemplo en OpenGL (MUY BÁSICO)

    Este código solo dibuja dos cuadrados (en realidad son polígonos en 3D, pero planos), 
    uno más cercano y otro más lejos, y podrás alternar entre perspectiva y ortográfica 
    con la tecla ESPACIO.

    Qué vas a notar al probarlo

    Al inicio está en perspectiva:
    El cuadrado rojo (cercano) se verá más grande.
    El cuadrado azul (lejano) se verá más pequeño.
    Si presionas ESPACIO cambia a ortográfica:
    Ambos cuadrados (rojo y azul) se ven del mismo tamaño, aunque estén a distinta distancia.

    👉 Con esto queda clara la diferencia:

    Perspectiva = realismo.
    Ortográfica = precisión.
"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Inicializar GLFW
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(600, 600, "Perspectiva vs Ortográfica (Ejemplo simple)", None, None)
glfw.make_context_current(window)

modo_perspectiva = True

def key_callback(window, key, scancode, action, mods):
    global modo_perspectiva
    if key == glfw.KEY_SPACE and action == glfw.PRESS:
        modo_perspectiva = not modo_perspectiva

glfw.set_key_callback(window, key_callback)

def dibujar_escena():
    # Cuadrado cercano (rojo)
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -3)  # Más cercano (z=-3)
    glVertex3f( 1, -1, -3)
    glVertex3f( 1,  1, -3)
    glVertex3f(-1,  1, -3)
    glEnd()

    # Cuadrado lejano (azul)
    glColor3f(0, 0, 1)
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -7)  # Más lejano (z=-7)
    glVertex3f( 1, -1, -7)
    glVertex3f( 1,  1, -7)
    glVertex3f(-1,  1, -7)
    glEnd()

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    ancho, alto = glfw.get_framebuffer_size(window)

    # --- Configurar proyección ---
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if modo_perspectiva:
        gluPerspective(60, ancho / alto, 0.1, 50)   # Perspectiva
    else:
        glOrtho(-2, 2, -2, 2, -10, 10)              # Ortográfica

    # --- Cámara ---
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0)

    dibujar_escena()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
