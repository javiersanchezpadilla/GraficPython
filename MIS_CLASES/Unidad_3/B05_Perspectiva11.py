""" Mis pruebas de perspectiva con gluPerspective """

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *       # <-- Aqui estamos importando la biblioteca GLUT FreeGLUT para las figuras precargadas.


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(600, 600, "Uso de los puertos de vision", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)

    # Activar buffer de profundidad, necesario para trabajar en 3D y calcular la profundidad de los
    # objetos en la escena.
    glEnable(GL_DEPTH_TEST)
    glutInit()  # Inicializar GLUT para usar figuras precargadas
    return ventana


def configurar_coordenadas_ventana(menos_x, mas_x, menos_y, mas_y, menos_z=-1.0, mas_z=1.0):
    # Configura la proyección para usar coordenadas de píxeles (ventana).
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(left, right, bottom, top, near, far)
    # Esto mapea [0, ancho] en X y [0, alto] en Y
    glOrtho(menos_x, mas_x, menos_y, mas_y, menos_z, mas_z)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# Función para dibujar un cuadro
def dibujar_figuras_precargadas(angulo_rotacion):

    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
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
    glPopMatrix()

    glColor3f(1.0,1.0,1.0)
	# Texto(6,-6,14,"FUNCIONES PRECARGADAS EN OPENGL");

    glColor3f(1.0,1.0,0.0)
    # Texto(1,-14,12,"Cono");
    glColor3f(0.0, 1.0, 0.0)
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(angulo_rotacion, 1.0, 1.0, 1.0)
    glutWireCone(5, 5, 30, 30)
    glPopMatrix()




def programa_principal():
    ventana = iniciar_ventana() 
    configurar_coordenadas_ventana(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)
    angulo_lento = 0.0

    while not glfw.window_should_close(ventana):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        dibujar_figuras_precargadas(angulo_lento) 
        angulo_lento += 0.8

        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()


if __name__ == "__main__":
    programa_principal()
