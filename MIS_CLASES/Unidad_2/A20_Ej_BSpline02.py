# Importamos las librerías necesarias
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

# Puntos de control de la curva B-spline
control_points = [
    [-0.9, -0.4],
    [-0.6, 0.6],
    [-0.2, -0.5],
    [0.2, 0.7],
    [0.6, -0.3],
    [0.9, 0.4]
]


def bspline_basis(i, k, t, knots):
    """
    Función base de Cox–de Boor para calcular
    las funciones base de una B-spline.
    
    i = índice del punto de control
    k = grado de la curva
    t = parámetro
    knots = vector de nodos
    """
    
    if k == 0:
        if knots[i] <= t < knots[i+1]:
            return 1.0
        return 0.0
    
    denom1 = knots[i+k] - knots[i]
    denom2 = knots[i+k+1] - knots[i+1]
    
    term1 = 0
    term2 = 0
    
    if denom1 != 0:
        term1 = ((t - knots[i]) / denom1) * bspline_basis(i, k-1, t, knots)
    
    if denom2 != 0:
        term2 = ((knots[i+k+1] - t) / denom2) * bspline_basis(i+1, k-1, t, knots)
    
    return term1 + term2


def bspline_point(t, points, degree, knots):
    """
    Calcula un punto de la curva B-spline
    usando la combinación de funciones base.
    """
    
    x = 0
    y = 0
    
    for i in range(len(points)):
        b = bspline_basis(i, degree, t, knots)
        x += points[i][0] * b
        y += points[i][1] * b
    
    return [x, y]


def display():
    """
    Función que dibuja los puntos de control,
    el polígono de control y la curva B-spline.
    """
    
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Dibujar puntos de control
    glPointSize(8)
    glColor3f(1, 0, 0)
    
    glBegin(GL_POINTS)
    for p in control_points:
        glVertex2f(p[0], p[1])
    glEnd()
    
    # Dibujar líneas del polígono de control
    glColor3f(0.6, 0.6, 0.6)
    
    glBegin(GL_LINE_STRIP)
    for p in control_points:
        glVertex2f(p[0], p[1])
    glEnd()
    
    # Parámetros de la B-spline
    degree = 3
    n = len(control_points)
    
    # Crear vector de nodos uniforme
    knots = list(range(n + degree + 1))
    
    # Dibujar curva B-spline
    glColor3f(0, 1, 0)
    
    glBegin(GL_LINE_STRIP)
    
    for t in np.linspace(degree, n, 200):
        p = bspline_point(t, control_points, degree, knots)
        glVertex2f(p[0], p[1])
    
    glEnd()
    
    glutSwapBuffers()


def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.1, 0.1, 0.1, 1)


def main():
    
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    
    glutCreateWindow(b"Curva B-Spline - OpenGL")
    
    init()
    
    glutDisplayFunc(display)
    
    glutMainLoop()


main()
