""" Este código permite hacer uso de las figuras precargadas en FreeGlut 

    Si es el caso en windows tenemos que instalar los paquetes para que reconozca GLUT 

        pip install PyOpenGL PyOpenGL-accelerate PyGLUT
"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *       # <-- Aqui estamos importando la biblioteca GLUT FreeGLUT para las figuras precargadas.


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Formas Básicas con transformaciones", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)

    # Activar buffer de profundidad, necesario para trabajar en 3D y calcular la profundidad de los
    # objetos en la escena.
    glEnable(GL_DEPTH_TEST)
    glutInit()                      # Inicializar GLUT para usar figuras precargadas
    return ventana


# Para cambiar la perspectiva
def cambiar_perspectiva(ancho, alto, fov=45):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fov, ancho/alto, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)      # Configurar cámara
    glLoadIdentity()
    gluLookAt(
        0, 0, 35,                   # Cámara POSICIONADA para ver toda la escena
        0, 0, 0,                    # Mira al CENTRO de la escena
        0, 1, 0                     # Vector "arriba"
    )
    


# Función para dibujar un cuadro
def dibujar_figuras_precargadas(angulo_rotacion):

    # Dibuja los ejes de coordenadas "x", "y" y "z"
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)        # Eje "x" en color verde
    glVertex3f(-15.0, 0.0, 0.0)
    glVertex3f(15.0, 0.0, 0.0)

    glColor3f(1.0, 0.0, 0.0)        # Eje "y" en color rojo
    glVertex3f(0.0,-15.0, 0.0)
    glVertex3f(0.0, 15.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)        # Eje "z" en color azul
    glVertex3f( 0.0, 0.0, -15.0)
    glVertex3f(0.0, 0.0, 15.0)
    glEnd()

    glColor3f(1.0,1.0,0.0)



def programa_principal():
    ventana = iniciar_ventana() 
    # configurar_coordenadas_ventana(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)
    angulo_lento = 0.0
    # Configurar perspectiva
    ancho, alto = glfw.get_window_size(ventana)
    cambiar_perspectiva(ancho, alto, 45)

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        dibujar_figuras_precargadas(angulo_lento) 
        angulo_lento += 0.8
        if angulo_lento >=360:
            angulo_lento = 0

        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()

if __name__ == "__main__":
    programa_principal()
