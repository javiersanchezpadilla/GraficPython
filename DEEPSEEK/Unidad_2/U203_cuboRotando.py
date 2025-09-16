""" Un Cubo 3D Sencillo
    Para dibujar un cubo, usamos GL_QUADS (cuadriláteros) 
    y coordenadas 3D.

"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Sistema de coordenadas

angle = 0

def animate():
    global angle
    angle += 0.5
    glutPostRedisplay()  # Vuelve a llamar a draw_cube


def draw_cube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(angle, 1, 1, 1)  # Rotación animada

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
    glutIdleFunc(animate)  # Llama a animate en cada frame
    glutMainLoop()


if __name__ == "__main__":
    main()

