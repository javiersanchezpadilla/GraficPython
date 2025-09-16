""" Ahora vamos a pasar de la teoría del gluLookAt a un ejemplo 
    práctico en OpenGL donde la cámara orbita alrededor de un cubo.

    📌 Idea del ejemplo
    **  Tenemos un cubo en el centro (0,0,0).
    **  La cámara (eye) va a moverse en círculo alrededor de él usando 
        funciones trigonométricas (cos y sin).
    **  center se queda fijo en (0,0,0) (el cubo).

    De esta forma, da la sensación de que la cámara gira alrededor del objeto.
    
    Resultado esperado
    **  El cubo permanece fijo en el centro.
    **  La cámara se mueve en círculo alrededor del cubo, dando la sensación de 
        que lo rodeamos.

    Puedes jugar con:
        radio → qué tan lejos está la cámara.
        angulo += 0.01 → qué tan rápido orbita la cámara.
        eyeY → altura de la cámara.
    
    """

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Inicializar GLFW
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(600, 600, "Cámara Orbital con gluLookAt", None, None)
glfw.make_context_current(window)

# Variables para la cámara
angulo = 0  # ángulo de órbita
radio = 6   # distancia de la cámara al objeto

def draw_cube():
    glBegin(GL_QUADS)

    # Frente (rojo)
    glColor3f(1,0,0)
    glVertex3f(-1,-1, 1)
    glVertex3f( 1,-1, 1)
    glVertex3f( 1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Atrás (verde)
    glColor3f(0,1,0)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1, 1,-1)
    glVertex3f( 1, 1,-1)
    glVertex3f( 1,-1,-1)

    # Izquierda (azul)
    glColor3f(0,0,1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1,-1)

    # Derecha (amarillo)
    glColor3f(1,1,0)
    glVertex3f(1,-1,-1)
    glVertex3f(1, 1,-1)
    glVertex3f(1, 1, 1)
    glVertex3f(1,-1, 1)

    # Arriba (cian)
    glColor3f(0,1,1)
    glVertex3f(-1,1,-1)
    glVertex3f(-1,1, 1)
    glVertex3f( 1,1, 1)
    glVertex3f( 1,1,-1)

    # Abajo (magenta)
    glColor3f(1,0,1)
    glVertex3f(-1,-1,-1)
    glVertex3f( 1,-1,-1)
    glVertex3f( 1,-1, 1)
    glVertex3f(-1,-1, 1)

    glEnd()

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 50)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Calcular posición de la cámara (orbital)
    eyeX = radio * math.cos(angulo)
    eyeZ = radio * math.sin(angulo)
    eyeY = 3   # altura fija

    gluLookAt(eyeX, eyeY, eyeZ,   # posición de la cámara
              0, 0, 0,            # centro (cubo)
              0, 1, 0)            # vector "arriba"

    draw_cube()

    # Incrementar ángulo para animar la órbita
    angulo += 0.01

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
