# Importamos librerías necesarias
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

# Puntos de control de la curva de Bézier
control_points = [
    [-0.8, -0.5],
    [-0.4, 0.6],
    [0.4, -0.6],
    [0.8, 0.5]
]


def bezier(t, points):
    """
    Calcula un punto de la curva de Bézier cúbica
    usando la ecuación matemática de Bernstein.
    """
    
    p0, p1, p2, p3 = points
    
    x = (1-t)**3 * p0[0] + 3*(1-t)**2*t * p1[0] + 3*(1-t)*t**2 * p2[0] + t**3 * p3[0]
    y = (1-t)**3 * p0[1] + 3*(1-t)**2*t * p1[1] + 3*(1-t)*t**2 * p2[1] + t**3 * p3[1]
    
    return [x, y]


def display():
    """
    Función principal que dibuja la curva y los puntos de control
    """
    
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Dibujar puntos de control
    glPointSize(8)
    glColor3f(1, 0, 0)
    
    glBegin(GL_POINTS)
    for p in control_points:
        glVertex2f(p[0], p[1])
    glEnd()
    
    
    # Dibujar líneas entre puntos de control
    glColor3f(0.6, 0.6, 0.6)
    glBegin(GL_LINE_STRIP)
    for p in control_points:
        glVertex2f(p[0], p[1])
    glEnd()
    
    
    # Dibujar curva de Bézier
    glColor3f(0, 1, 0)
    glBegin(GL_LINE_STRIP)
    
    for t in np.linspace(0, 1, 100):
        punto = bezier(t, control_points)
        glVertex2f(punto[0], punto[1])
    
    glEnd()
    
    glutSwapBuffers()


def init():
    """
    Configuración inicial de OpenGL
    """
    glClearColor(0.1, 0.1, 0.1, 1)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    
    glutCreateWindow(b"Curva de Bezier - OpenGL")
    
    init()
    
    glutDisplayFunc(display)
    
    glutMainLoop()


main()