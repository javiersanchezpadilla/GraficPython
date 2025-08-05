""" En este ejemp"""

import pygame
from pygame.locals import *     # Importamos todas las funciones de Pygame
from OpenGL.GL import *         # Importamos todas las funciones de OpenGL

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # El color que vamos a usar (en este caso, rojo)
    glColor3f(1.0, 0.0, 0.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Aquí está la magia de OpenGL
        glBegin(GL_TRIANGLES)  # Le decimos a OpenGL que vamos a dibujar triángulos
        
        # glColor3f(0.5, 0.5, 0.5)
        # Definimos los 3 vértices del triángulo (x, y)
        glVertex2f(-0.9, 0.9)  # vertice 1
        glVertex2f(0.9, -0.9)   # vertice 2
        glVertex2f(-0.9, -0.9)  # vertice 3
        
        # glColor3f(1.0, 1.0, 0.0)
        glVertex2f(-0.9, 0.9)  # vertice 1
        glVertex2f(0.9, 0.9)   # vertice 2
        glVertex2f(0.9, -0.9)  # vertice 3

        glEnd() # Le decimos a OpenGL que ya hemos terminado

        pygame.display.flip()
        pygame.time.wait(10)

main()

