""" Este código permite hacer uso de las figuras precargadas en FreeGlut 
    El objetivo es iluminar la escena"""

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
def dibujar_figuras_precargadas(angulo_lento):

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
                                    # Trazo del cono
    glPushMatrix()
    glTranslatef(-13.0, 9.0, 0.0)
    glRotatef(angulo_lento, 1, 1, 1)
    glutWireCone(1.5, 2.5, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-13.0, 4.0, 0.0)
    glRotatef(angulo_lento, 1.0, 1.0, 1.0)
    glutSolidCone(1.5, 2.5, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-7.0, 9.0, 0.0)
    glRotatef(angulo_lento, 1, 1, 1)
    glutWireCube(2.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-7.0, 4.0, 0.0)
    glRotatef(angulo_lento, 1.0, 1.0, 1.0)
    glutSolidCube(2.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.0, 9.0, 0.0)
    glScalef(0.9, 0.9, 0.9)
    glRotatef(angulo_lento, 1, 1, 1)
    glutWireDodecahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.0, 4.0, 0.0)
    glScalef(0.9, 0.9, 0.9)
    glRotatef(angulo_lento, 1, 1, 1)
    glutSolidDodecahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.0, 9.0, 0.0)
    glScalef(1.6, 1.6, 1.6)
    glRotatef(angulo_lento, 1, 1, 1)
    glutWireIcosahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.0, 4.0, 0.0)
    glScalef(1.6, 1.6, 1.6)
    glRotatef(angulo_lento, 1, 1, 1)
    glutSolidIcosahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(8.0, 9.0, 0.0)
    glScalef(1.6, 1.6, 1.6)
    glRotatef(angulo_lento, 1, 1, 1)
    glutWireOctahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(8.0, 4.0, 0.0)
    glScalef(1.6, 1.6, 1.6)
    glRotatef(angulo_lento, 1, 1, 1)
    glutSolidOctahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(13.0, 9.0, 0.0)
    glScalef(1.6, 1.6, 1.6)
    glRotatef(angulo_lento, 1, 1, 1)
    glutWireSphere(1.0, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(13.0, 4.0, 0.0)
    glScalef(1.6, 1.6, 1.6)
    glRotatef(angulo_lento, 1, 1, 1)
    glutSolidSphere(1.0, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-11.3, -5.0, 0.0)
    glRotatef(angulo_lento, 1, 1, 1)
    glutWireTeapot(1.6)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-11.3, -11.0, 0.0)
    glRotatef(angulo_lento, 1, 1, 1)
    glutSolidTeapot(1.6)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-4.0, -5.0, 0.0)
    glScalef(2.0, 2.0, 2.0)
    glRotatef(angulo_lento, 1, 1, 1)
    glutWireTetrahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-4.0, -11.0, 0.0)
    glScalef(2.0, 2.0, 2.0)
    glRotatef(angulo_lento, 1, 1, 1)
    glutSolidTetrahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(6.5, -4.8, 0.0)
    glRotatef(angulo_lento, 1, 1, 1)
    glutWireTorus(0.7, 1.4, 10, 15)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(6.5, -11.0, 0.0)
    glRotatef(angulo_lento, 1, 1, 1)
    glutSolidTorus(0.7, 1.4, 10, 15)
    glPopMatrix()



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

