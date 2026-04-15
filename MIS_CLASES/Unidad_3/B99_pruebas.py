""" El siguiente código permite hacer uso del concepto de las transformaciones en una escena 3D. 
    Usando OpenGL y GLFW, se dibujan varias figuras (cuadros, triángulos, líneas) en distintas posiciones.   
    Este es el código base para trabajar con transformaciones como traslaciones, rotaciones y escalamiento.
    """

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


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


# Función para dibujar figuras 
def dibujar_cuadros(angulo01, escalado):

    glColor3f(1.0, 1.0, 1.0)        # Ejes coordenados
    glBegin(GL_LINES)
    glVertex3f(-15.0, 0.0, 0.0)
    glVertex3f(15.0, 0.0, 0.0)
    glVertex3f(0.0, -15.0, 0.0)
    glVertex3f(0.0,  15.0, 0.0)
    glVertex3f(0.0, 0.0, -15.0)
    glVertex3f(0.0, 0.0, 15.0)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)        # Cuadro amarillo
    glPushMatrix()
    glTranslatef(-3.0, 10.0, 0.0)
    glRotatef(angulo01, 0, 0, 2)
    glBegin(GL_QUADS)
    glVertex3f(-2.0, -2.0, 0.0)
    glVertex3f(-2.0, 2.0, 0.0)
    glVertex3f(2.0, 2.0, 0.0)
    glVertex3f(2.0, -2.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.0, 10.0, 0.0)


    glScalef(escalado, escalado, escalado)
    glColor3f(0.3, 0.6, 0.1)        # Triángulo verde
    glBegin(GL_TRIANGLES)
    glVertex3f(-2.0, -2.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(2.0, -2.0, 0.0)
    glEnd()
    glPopMatrix()

    glColor3f(0.0, 0.0, 1.0)        # Polígono azul
    glBegin(GL_QUADS)
    glVertex3f(-3.0, 6.0, 0.0)
    glVertex3f(-2.0, 3.0, 0.0)
    glVertex3f(-3.0, 0.0, 0.0)
    glVertex3f(-4.0, 3.0, 0.0)
    glEnd()

    glColor3f(1.0, 0.0, 1.0)        # Polígono magenta
    glBegin(GL_LINE_LOOP)
    glVertex3f(3.0, 6.0, 0.0)
    glVertex3f(5.0, 4.0, 0.0)
    glVertex3f(5.0, 1.0, 0.0)
    glVertex3f(3.0, 0.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, 4.0, 0.0)
    glEnd()



def programa_principal():
    ventana = iniciar_ventana() 
    configurar_coordenadas_ventana(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)
    angulo_lento = 0.0
    escala = 1.0
    factor = 1

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        dibujar_cuadros(angulo_lento, escala) 

        angulo_lento += 0.9
        if angulo_lento >= 360.0:
            angulo_lento = 0.0

        escala += (0.09 * factor)
        if escala >= 2.0 or escala <= 0.2:
            factor = factor * (-1) 

        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    programa_principal()
