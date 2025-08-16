""" Ejemplo básico: Cubo en 3D con cámara MEDIANTE PROYECCIÓN EN PERSPECTIVA

    Este ejemplo muestra cómo dibujar un cubo en 3D y aplicar una proyección 
    en perspectiva para simular profundidad. La cámara se mueve alrededor del 
    cubo, permitiendo ver sus caras desde diferentes ángulos.

    Este ejemplo dibuja un cubo en 3D y permite ver cómo la proyección 
    y la cámara cambian la visualización.
    
    QUÉ APRENDEMOS AQUÍ:

    1.  Proyección en perspectiva
        gluPerspective(45, 1, 0.1, 50) → ángulo de 45°, aspecto 1:1, plano cercano 0.1 y lejano 50.
        Esto hace que objetos lejanos se vean más pequeños.

    2.  Cámara (gluLookAt)
        gluLookAt(x, 2, z, 0, 0, 0, 0, 1, 0) significa:
            La cámara está en (x, 2, z) dando vueltas alrededor.
            Mira hacia (0,0,0) (el cubo).
            El vector “arriba” es (0,1,0), es decir, eje Y.

    3.  Prueba de profundidad (glEnable(GL_DEPTH_TEST))
        Para que las caras del cubo oculten correctamente las que están detrás.

    """

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Inicializar GLFW
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(700, 700, "Proyección y Cámara", None, None)
glfw.make_context_current(window)

# Función para dibujar un cubo
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

# Configuración inicial
glEnable(GL_DEPTH_TEST)  # Importante para 3D

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 50)  # fov, aspecto, cerca, lejos

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # --- Cámara (gluLookAt) ---
    tiempo = glfw.get_time()
    x = math.sin(tiempo) * 3
    z = math.cos(tiempo) * 3
    gluLookAt(x, 2, z,  0, 0, 0,  0, 1, 0)

    # --- Rotación del cubo ---
    glRotatef(tiempo * 50, 1, 1, 0)
    dibujar_cubo()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()



