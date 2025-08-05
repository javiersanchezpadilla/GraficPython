""" Dibujando un Polígono Relleno

    En OpenGL, las primitivas son las formas básicas con las que construyes todo lo demás. Las más comunes en 2D son:

    GL_POINTS           Dibuja puntos.
    GL_LINES            Dibuja líneas sueltas.
    GL_LINE_STRIP       Dibuja una cadena de líneas conectadas.
    GL_LINE_LOOP        Como GL_LINE_STRIP, pero conecta el último vértice con el primero para formar un bucle.
    GL_TRIANGLES        Dibuja triángulos.
    GL_TRIANGLE_STRIP   Dibuja una serie de triángulos conectados de forma eficiente.
    GL_QUADS            Dibuja cuadriláteros.
    GL_POLYGON          Dibuja un polígono de 'N' lados.
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ... (Las variables globales y la función inicializar_opengl son las mismas) ...
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

def inicializar_opengl():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, float(ANCHO_VENTANA), 0.0, float(ALTO_VENTANA))

def dibujar_poligonos():
    """
    Dibuja diferentes polígonos.
    """
    # 1. Dibujar un triángulo amarillo (GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)  # Amarillo
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 400.0)
    glVertex2f(200.0, 400.0)
    glVertex2f(150.0, 500.0)
    glEnd()

    # 2. Dibujar un cuadrado morado (GL_QUADS)
    glColor3f(0.5, 0.0, 0.5)  # Morado
    glBegin(GL_QUADS)
    glVertex2f(300.0, 100.0)
    glVertex2f(500.0, 100.0)
    glVertex2f(500.0, 300.0)
    glVertex2f(300.0, 300.0)
    glEnd()

    # 3. Dibujar un polígono con colores en los vértices (GL_POLYGON)
    # OpenGL interpolará los colores entre los vértices.
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)  # Vértice 1 (Rojo)
    glVertex2f(650.0, 100.0)
    
    glColor3f(0.0, 1.0, 0.0)  # Vértice 2 (Verde)
    glVertex2f(750.0, 200.0)
    
    glColor3f(0.0, 0.0, 1.0)  # Vértice 3 (Azul)
    glVertex2f(700.0, 300.0)
    
    glColor3f(1.0, 1.0, 1.0)  # Vértice 4 (Blanco)
    glVertex2f(600.0, 200.0)
    glEnd()

def main_poligonos():
    """
    Función principal para el ejemplo de polígonos.
    """
    pygame.init()
    pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Poligonos 2D Basicos")
    inicializar_opengl()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT)
        dibujar_poligonos()
        pygame.display.flip()           # es un glutSwapBuffer()
        pygame.time.wait(10)            # pausa el programa para que no se ejecute a máxima velocidad.

if __name__ == "__main__":
    main_poligonos()