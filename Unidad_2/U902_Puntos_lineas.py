""" Este programa te mostrará cómo crear una ventana, establecer una proyección 2D 
    y dibujar una serie de puntos y líneas para formar una figura simple."""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# --- Variables Globales ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

def inicializar_opengl():
    """
    Configuración inicial de OpenGL.
    Establece el color de fondo y la proyección 2D.
    """
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Color de fondo negro
    glMatrixMode(GL_PROJECTION)      # Activa la matriz de proyección
    glLoadIdentity()                 # Resetea la matriz
    # gluOrtho2D(left, right, bottom, top)
    # Proyección 2D: establece un sistema de coordenadas donde el origen (0,0) está en la esquina inferior izquierda
    gluOrtho2D(0.0, float(ANCHO_VENTANA), 0.0, float(ALTO_VENTANA))

def dibujar_primitivas():
    """
    Dibuja diferentes primitivas de OpenGL: puntos y líneas.
    """
    # 1. Dibujar un punto rojo grande
    glColor3f(1.0, 0.0, 0.0)  # Color rojo
    glPointSize(10.0)         # Tamaño del punto
    glBegin(GL_POINTS)
    glVertex2f(100.0, 100.0)
    glEnd()

    # 2. Dibujar una línea azul que va de un lado a otro
    glColor3f(0.0, 0.0, 1.0)  # Color azul
    glLineWidth(5.0)          # Grosor de la línea
    glBegin(GL_LINES)
    glVertex2f(50.0, 300.0)
    glVertex2f(750.0, 300.0)
    glEnd()

    # 3. Dibujar una línea en forma de V (GL_LINE_STRIP)
    glColor3f(0.0, 1.0, 0.0)  # Color verde
    glBegin(GL_LINE_STRIP)
    glVertex2f(400.0, 500.0)
    glVertex2f(500.0, 400.0)
    glVertex2f(600.0, 500.0)
    glEnd()

def main():
    """
    Función principal que inicia la aplicación.
    """
    pygame.init()
    pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Primitivas 2D Basicas")

    inicializar_opengl()

    # Bucle principal de la aplicación
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)  # Limpia la pantalla
        dibujar_primitivas()          # Llama a la función de dibujo
        pygame.display.flip()         # Actualiza la pantalla

        pygame.time.wait(10)

if __name__ == "__main__":
    main()
