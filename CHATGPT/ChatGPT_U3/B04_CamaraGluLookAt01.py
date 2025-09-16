""" Código de ejemplo en OpenGL

    Un cubo que podemos mirar desde distintos puntos moviendo 
    la cámara con las teclas:
    
    Controles

    Flechas → mover la cámara izquierda/derecha/arriba/abajo.
    W → acercar.
    S → alejar.

    Así empezarás a sentir que te mueves dentro de la escena en lugar 
    de solo mover objetos.
    
    """

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Inicializar GLFW
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(600, 600, "Ejemplo de Cámara (gluLookAt)", None, None)
glfw.make_context_current(window)

# Posición inicial de la cámara
eyeX, eyeY, eyeZ = 0, 0, 5

def key_callback(window, key, scancode, action, mods):
    global eyeX, eyeY, eyeZ
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            eyeY += 1   # mover arriba
        elif key == glfw.KEY_DOWN:
            eyeY -= 1   # mover abajo
        elif key == glfw.KEY_LEFT:
            eyeX -= 1   # mover izquierda
        elif key == glfw.KEY_RIGHT:
            eyeX += 1   # mover derecha
        elif key == glfw.KEY_W:
            eyeZ -= 1   # acercar
        elif key == glfw.KEY_S:
            eyeZ += 1   # alejar

glfw.set_key_callback(window, key_callback)

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
    gluLookAt(eyeX, eyeY, eyeZ, 0, 0, 0, 0, 1, 0)

    draw_cube()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
