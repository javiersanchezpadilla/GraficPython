""" Pruebas de perspectiva con gluPerspective 

    Este programa muestra que no es necesario definir limites para una escena en OpenGL
    nosotros determinamos los limites conforme vamos haciendo uso de los trazos en pantalla
    mediante el uso de gluPerepective() (perspectiva) y gluLookAt() (Cámara), determinamos
    desde donde vamos a estar viendo la escena, esto nos permite lograr ver todos los elementos
    o no, por esta razon ya no se definen limites con coordenadas ortogonales, todo parte del 
    principio del uso de coordenadas normalizadas y de ahí decidimos el limite de los trazos.

"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *       # <-- Aqui estamos importando la biblioteca GLUT FreeGLUT para las figuras precargadas.


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(600, 600, "Uso de la perspectiva", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)

    # Activar buffer de profundidad, necesario para trabajar en 3D y calcular la profundidad de los
    # objetos en la escena.
    glEnable(GL_DEPTH_TEST)
    glutInit()  # Inicializar GLUT para usar figuras precargadas
    return ventana


# Para cambiar la perspectiva
def cambiar_perspectiva(fov=45):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fov, 600/600, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    # Configurar cámara
    glLoadIdentity()
    gluLookAt(
        5, 12, 65,    # Cámara POSICIONADA para ver toda la escena
        0, 0, 0,       # Mira al CENTRO de la escena
        0, 1, 0        # Vector "arriba"
    )
    



# Función para dibujar un cuadro
def dibujar_figuras_precargadas(angulo_rotacion):

    # dibuja el contorno de los ejes (un cubo conteniendo los ejes, todo de -15 a 15)
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_LINES)
    glVertex3f(-15.0, -15.0, -15.0)
    glVertex3f(-15.0, 15.0, -15.0)
    glVertex3f(-15.0, 15.0, -15.0)
    glVertex3f(15.0, 15.0, -15.0)
    glVertex3f(15.0, 15.0, -15.0)
    glVertex3f(15.0, -15.0, -15.0)
    glVertex3f(15.0, -15.0, -15.0)
    glVertex3f(-15.0, -15.0, -15.0)
    glVertex3f(-15.0, -15.0, -15.0)
    glVertex3f(-15.0, -15.0, 15.0)
    glVertex3f(-15.0, 15.0, -15.0)
    glVertex3f(-15.0, 15.0, 15.0)
    glVertex3f(15.0, 15.0, -15.0)
    glVertex3f(15.0, 15.0, 15.0)
    glVertex3f(15.0, -15.0, -15.0)
    glVertex3f(15.0, -15.0, 15.0)
    glVertex3f(-15.0, 15.0, 15.0)
    glVertex3f(-15.0, -15.0, 15.0)
    glVertex3f(-15.0, 15.0, 15.0)
    glVertex3f(15.0, 15.0, 15.0)
    glVertex3f(15.0, 15.0, 15.0)
    glVertex3f(15.0, -15.0, 15.0)
    glVertex3f(-15.0, -15.0, 15.0)
    glVertex3f(15.0, -15.0, 15.0)

    glVertex3f(-15.0, 15.0, 0.0)
    glVertex3f(-15.0, -15.0, 0.0)
    glVertex3f(-15.0, 0.0, -15.0)
    glVertex3f(-15.0, -0.0, 15.0)

    glVertex3f(15.0, 15.0, 0.0)
    glVertex3f(15.0, -15.0, 0.0)
    glVertex3f(15.0, 0.0, -15.0)
    glVertex3f(15.0, 0.0, 15.0)

    glVertex3f(-15.0, 0.0, -15.0)
    glVertex3f(15.0, 0.0, -15.0)
    glVertex3f(0.0, 15.0, -15.0)
    glVertex3f(0.0, -15.0, -15.0)

    glVertex3f(0.0, 15.0, -15.0)
    glVertex3f(0.0, 15.0, 15.0)
    glVertex3f(-15.0, 15.0, 0.0)
    glVertex3f(15.0, 15.0, 0.0)

    glVertex3f(0.0, -15.0, 15.0)
    glVertex3f(0.0, 15.0, 15.0)
    glVertex3f(-15.0, 0.0, 15.0)
    glVertex3f(15.0, 0.0, 15.0)

    glVertex3f(-15.0, -15.0, 0.0)
    glVertex3f(15.0, -15.0, 0.0)
    glVertex3f(0.0, -15.0, -15.0)
    glVertex3f(0.0, -15.0, 15.0)    
    glEnd()

    # Dibuja los ejes de coordenadas "x", "y" y "z"
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-15.0, 0.0, 0.0)
    glVertex3f(15.0, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0,-15.0, 0.0)
    glVertex3f(0.0, 15.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f( 0.0, 0.0, -15.0)
    glVertex3f(0.0, 0.0, 15.0)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(angulo_rotacion, 1.0, 1.0, 1.0)
    glutWireCone(5, 5, 30, 30)
    glPopMatrix()



def programa_principal():
    ventana = iniciar_ventana() 
    # configurar_coordenadas_ventana(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)
    angulo_lento = 0.0

    cambiar_perspectiva(45)

    while not glfw.window_should_close(ventana):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        dibujar_figuras_precargadas(angulo_lento) 
        angulo_lento += 0.8

        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()


if __name__ == "__main__":
    programa_principal()
