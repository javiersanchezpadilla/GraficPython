from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

# Tamaño de la ventana
width = 800
height = 600

# Número máximo de iteraciones
max_iter = 100


def mandelbrot(c):
    """
    Calcula el número de iteraciones antes de que
    la secuencia diverja en el conjunto de Mandelbrot.
    """
    z = 0

    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i

    return max_iter


def display():
    """
    Dibuja el fractal de Mandelbrot píxel por píxel
    """
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)

    for x in range(width):
        for y in range(height):

            # Convertir coordenadas de pantalla a plano complejo
            real = (x - width/2) / (width/4)
            imag = (y - height/2) / (height/4)

            c = complex(real, imag)

            m = mandelbrot(c)

            # Color basado en número de iteraciones
            color = m / max_iter
            glColor3f(color, color*0.5, 1-color)

            glVertex2f(
                (x / width) * 2 - 1,
                (y / height) * 2 - 1
            )

    glEnd()

    glFlush()


def init():
    glClearColor(0, 0, 0, 1)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"Fractal Mandelbrot")

    init()

    glutDisplayFunc(display)

    glutMainLoop()


main()
