""" Como dibujar un circulo con OpenGL
"""

import math
from OpenGL.GL import *


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Sistema de coordenadas


def dibujar_circulo(x, y, radio, segmentos=50):
    glBegin(GL_TRIANGLE_FAN)  # 👈 1. Inicia el modo de dibujo
    glColor3f(1.0, 1.0, 0.0)  # 👈 2. Color amarillo (RGB)
    glVertex2f(x, y)  # 👈 3. Centro del círculo
    
    for i in range(segmentos + 1):  # 👈 4. Bucle para los vértices
        angulo = 2 * math.pi * i / segmentos  # 👈 5. Calcula el ángulo
        glVertex2f(
            x + math.cos(angulo) * radio,  # 👈 6. Coordenada X del borde
            y + math.sin(angulo) * radio   # 👈 7. Coordenada Y del borde
        )
    glEnd()  # 👈 8. Finaliza el dibujo


def dibujar():
    glClear(GL_COLOR_BUFFER_BIT)
    dibujar_circulo(0, 0, 0.5, 50)  # Círculo en (0,0) con radio 0.5
    glutSwapBuffers()



glutInit()
glutCreateWindow("Círculo en OpenGL")
glutDisplayFunc(dibujar)
glutMainLoop()


