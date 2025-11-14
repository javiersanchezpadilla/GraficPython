""" ESTE CÓDIGO NO EVIARLO YA QUE ES MI CLASE.

    El siguiente código permite hacer uso del concepto de las transformaciones en una escena 3D. 
    Usando OpenGL y GLFW, se dibujan varias figuras (cuadros, triángulos, líneas) en distintas posiciones.   
    Este es el código base para trabajar con la transformación de rotación.

    Los pasos a seguir para trabajar con transformaciones son:
    ----------------------------------------------------------
    1. Antes de dibujar el objeto, guardar la matriz actual con glPushMatrix().
    2. Aplicar las transformaciones deseadas (traslación, rotación, escalamiento).
    3. Dibujar el objeto en la nueva posición.
    4. Restaurar la matriz original con glPopMatrix() para que las transformaciones no afecten a otros objetos.

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
def dibujar_cuadros(angulo_lento, angulo_rapido, escala, pos_x, pos_y):

    # glPushMatrix()
    # glRotatef(angulo_lento, 1.0, 1.0, 1.0)   # Inclinación inicial de la escena

    glColor3f(1.0, 1.0, 1.0)        # Ejes coordenados
    glBegin(GL_LINES)
    glVertex3f(-15.0, 0.0, 0.0)
    glVertex3f(15.0, 0.0, 0.0)
    glVertex3f(0.0, -15.0, 0.0)
    glVertex3f(0.0,  15.0, 0.0)
    glVertex3f(0.0, 0.0, -15.0)
    glVertex3f(0.0, 0.0, 15.0)
    glEnd()
    # glPopMatrix()


    glPushMatrix()
    glTranslatef(-3.0, 10.0, 0.0)               # Traslación
    glRotatef(angulo_lento, 0.0, 0.0, 1.0)      # Rotación
    glColor3f(1.0, 1.0, 0.0)                    # Cuadro amarillo
    glBegin(GL_QUADS)
    glVertex3f(-2.0, -2.0, 0.0)
    glVertex3f(-2.0, 2.0, 0.0)
    glVertex3f(2.0, 2.0, 0.0)
    glVertex3f(2.0, -2.0, 0.0)
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslatef(4.0, 10.0, 0.0)
    glRotatef(angulo_rapido, 0.0, 0.0, 1.0)      # Rotación
    glColor3f(0.3, 0.6, 0.1)        # Triángulo verde
    glBegin(GL_TRIANGLES)
    glVertex3f(-2.0, -2.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(2.0, -2.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-3.0, 3.0, 0.0)
    glScalef(escala, escala, escala)    # Escalamiento
    glRotatef(angulo_lento, 0.0, 0.0, 1.0)      # Rotacións
    glColor3f(0.0, 0.0, 1.0)            # Polígono azul
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(0.0, 3.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, -3.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(pos_x, 3.0, 0.0)
    glColor3f(1.0, 0.0, 1.0)        # Polígono magenta
    glBegin(GL_LINE_LOOP)
    glVertex3f(-2.0, 1.0, 0.0)
    glVertex3f(0.0, 3.0, 0.0)
    glVertex3f(2.0, 1.0, 0.0)
    glVertex3f(2.0, -1.0, 0.0)
    glVertex3f(0.0, -3.0, 0.0)
    glVertex3f(-2.0, -2.0, 0.0)
    glEnd()
    glPopMatrix()



    glColor3f(0.0, 1.0, 1.0)        # Polígono cian
    glPushMatrix()
    glTranslatef(-7.0, -7.0, 0.0)               # Traslación
    
    glRotatef(angulo_lento, 0.0, 0.0, 1.0)      # Rotación
    glBegin(GL_QUADS)
    glVertex3f(-2.0, -2.0, 0.0)
    glVertex3f(-2.0, 2.0, 0.0)
    glVertex3f(2.0, 2.0, 0.0)
    glVertex3f(2.0, -2.0, 0.0)
    glEnd()
    # glPopMatrix()
                  
    glPushMatrix()
    glTranslatef(-7.0, -2.0, 0.0)               # Traslación
    glRotatef(angulo_rapido, 0.0, 0.0, 1.0)      # Rotación
    glBegin(GL_QUADS)
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glEnd()
    glPopMatrix()
    glPopMatrix()
                  

def programa_principal():
    ventana = iniciar_ventana() 
    configurar_coordenadas_ventana(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)

    angulo_rotacion_lento = 0.1
    angulo_rotacion_rapido = -0.5

    escala = 0.1
    factor_escala = 0.01

    pos_x = 0.0
    factor_x = 0.09
    pos_y = 0.0

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        dibujar_cuadros(angulo_rotacion_lento, angulo_rotacion_rapido, escala, pos_x, pos_y) 
        angulo_rotacion_lento += 0.5
        angulo_rotacion_rapido += -1.0
        escala += factor_escala
        if escala > 2.0:
            factor_escala = -0.01
        elif escala < 0.1:
            factor_escala = 0.01

        pos_x += factor_x
        pos_y += 0.01
        if pos_x > 11.0:
            factor_x = -0.09
        elif pos_x < -11.0:
            factor_x = 0.09


        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    programa_principal()
