""" Puntos Clave:
    near y far en gluPerspective() deben contener tu escena

    Posición de cámara en gluLookAt() debe estar fuera del volumen -15 a 15
    Dirección de mirada debe apuntar al centro de tu escena
    Con estos ajustes la escena de -15 a 15 se verá perfectamente, La clave está en posicionar 
    la cámara adecuadamente para que pueda "ver" todo el volumen de tu mundo 3D.

"""


import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL import GLUT
import math

if not glfw.init():
    exit()

ventana = glfw.create_window(800, 600, "Rango -15 a 15", None, None)
glfw.make_context_current(ventana)

GLUT.glutInit()

glEnable(GL_DEPTH_TEST)

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar perspectiva para rango -15 a 15
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 1.0, 100.0)
    
    # Posicionar cámara para ver toda la escena
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(25, 20, 25, 0, 0, 0, 0, 1, 0)
    
    # Dibujar una esfera grande que ocupe parte del espacio
    glColor3f(0.2, 0.6, 1.0)
    GLUT.glutSolidSphere(10, 32, 32)  # Radio 10, dentro de -15 a 15
    
    # Dibujar un toro más pequeño
    glColor3f(1.0, 0.5, 0.2)
    glTranslatef(5, 0, 5)
    GLUT.glutSolidTorus(2, 5, 16, 32)
    
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()