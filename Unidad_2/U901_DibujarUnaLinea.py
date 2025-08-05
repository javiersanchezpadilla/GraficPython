""" Debemos importar las siguientes librerias en el entorno de trabajo

    pip3 install pygame PyOpenGL

"""


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# --- Variables Globales ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600


def dibuja_linea(x1, y1, x2, y2, rojo, verde, azul):
    """
    Dibuja una línea de (x1, y1) a (x2, y2) con un color específico.
    """
    glColor3f(rojo, verde, azul)
    glBegin(GL_LINES)
    glVertex2i(x1, y1)
    glVertex2i(x2, y2)
    glEnd()

def dibuja_cuadricula():
    """
    Dibuja una cuadrícula simple.
    """

    glColor3f(0.0, 1.0, 1.0) # Cian
    # Dibujar líneas verticales
    for x in range(0, 201, 10):
        glBegin(GL_LINES)
        glVertex2i(x, 0)
        glVertex2i(x, 150)
        glEnd()

    # Dibujar líneas horizontales
    for y in range(0, 151, 10):
        glBegin(GL_LINES)
        glVertex2i(0, y)
        glVertex2i(200, y)
        glEnd()

def segmento_de_linea():
    """
    Función de renderizado principal.
    """
    glClear(GL_COLOR_BUFFER_BIT)

    # Línea 1 (roja)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2i(180, 15)
    glVertex2i(10, 145)
    glEnd()

    # Línea 2 (verde)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2i(0, 75)
    glVertex2i(200, 75)
    glEnd()

    # Línea 3 (azul)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2i(100, 150)
    glVertex2i(100, 0)
    glEnd()

    # Usando la función auxiliar dibuja_linea (negra)
    dibuja_linea(0, 50, 200, 50, 0.0, 0.0, 0.0)

    # Dibujando la cuadrícula
    dibuja_cuadricula()

    pygame.display.flip() # Equivalente a glutSwapBuffers() o glFlush() en modo single buffer

# --- Configuración de la Ventana (equivalente a main y Inicializa) ---

def inicializa():
    """
    Configuración inicial de OpenGL.
    """
    glClearColor(1.0, 1.0, 1.0, 0.0)                                            # Defini el color de fondo de la ventana (blanco)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 200.0, 0.0, 150.0)                                          # Proyección 2D

def main():
    """
    Función principal que inicializa la ventana y el bucle de eventos.
    Equivalente a tu función main() de C++
    """
    pygame.init()                                                               # glutInit()
    pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), DOUBLEBUF | OPENGL)  # glutInitDisplayMode()
    pygame.display.set_caption("Ejemplo de Lineas en OpenGL (Python)")          # nombre de la ventana

    inicializa()

    while True: # Bucle principal de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        segmento_de_linea()
        pygame.time.wait(10) # Pausa para no consumir CPU al 100%

if __name__ == "__main__":
    main()