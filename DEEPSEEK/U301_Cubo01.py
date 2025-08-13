""" Dibujando un cubo sencillo en 2D

    Explicación:
    glRotatef(): Rota el cubo para verlo en 3D.
    GL_QUADS: Dibuja cuadriláteros (6 caras para un cubo).
    GL_DEPTH_TEST: Habilita el buffer de profundidad para que las caras traseras no se 3
    dibujen sobre las delanteras.

"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_cube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(30, 1, 1, 0)  # Rotación para ver en 3D
    
    glBegin(GL_QUADS)
    # Cara frontal (verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    
    # Cara trasera (roja)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    # (Agrega más caras aquí...)
    glEnd()
    
    glutSwapBuffers()  # Usado en modo GLUT_DOUBLE

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow("Cubo 3D en OpenGL")
    glEnable(GL_DEPTH_TEST)  # Habilita el test de profundidad
    glutDisplayFunc(draw_cube)
    glutMainLoop()

if __name__ == "__main__":
    main()
