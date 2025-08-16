""" Explicación paso a paso:

    Configuración inicial:

    glutInit(): Inicializa GLUT.
    glutInitWindowSize(): Define el tamaño de la ventana.
    glClearColor(): Establece el color de fondo (blanco en este caso).

    Sistema de coordenadas:

    gluOrtho2D(-1, 1, -1, 1): Define un sistema de coordenadas donde:
    El centro es (0, 0).
    Los límites van desde -1 a 1 en ambos ejes (X e Y).

    Dibujo de la circunferencia:

    Usamos GL_LINE_LOOP para conectar los puntos y formar un círculo cerrado.
    Calculamos cada punto (x, y) con:

    python
    x = centro_x + radio * cos(θ)
    y = centro_y + radio * sin(θ)
    θ se recorre en pasos de 10 grados (convertidos a radianes).

    Ejecución:

    glutMainLoop(): Mantiene la ventana abierta."""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def dibujar_circunferencia():
    glClear(GL_COLOR_BUFFER_BIT)  # Limpia el buffer de color
    glColor3f(1.0, 0.0, 0.0)      # Color rojo (RGB)
    glBegin(GL_LINE_LOOP)         # Dibuja una línea cerrada (circunferencia)
    
    radio = 0.5                   # Radio de la circunferencia
    centro_x, centro_y = 0.0, 0.0  # Centro en (0, 0)
    
    # Generamos los puntos de la circunferencia usando seno y coseno
    for angulo in range(0, 360, 10):  # Incrementos de 10 grados
        theta = math.radians(angulo)  # Convertimos a radianes
        x = centro_x + radio * math.cos(theta)
        y = centro_y + radio * math.sin(theta)
        glVertex2f(x, y)             # Añade el punto al dibujo
    
    glEnd()
    glFlush()  # Renderiza inmediatamente

def inicializar():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Fondo blanco (RGBA)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Sistema de coordenadas

def main():
    glutInit()                         # Inicializa GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)       # Tamaño de la ventana
    glutInitWindowPosition(100, 100)   # Posición en la pantalla
    glutCreateWindow(b"Circunferencia con OpenGL")  # Título
    inicializar()
    glutDisplayFunc(dibujar_circunferencia)  # Llama a la función de dibujo
    glutMainLoop()                    # Bucle principal

if __name__ == "__main__":
    main()