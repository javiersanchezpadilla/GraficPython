""" Dando vida a las formas y colores
    Imagina que estás pintando en un lienzo y quieres cambiar de color el pincel. 
    En OpenGL, hacemos esto de una manera similar.
    Para decirle a OpenGL qué color queremos usar, empleamos el comando glColor3f(). 
    Este comando toma tres números entre 0.0 y 1.0. Estos números representan la cantidad 
    de rojo, verde y azul que queremos en nuestro color.
        El primer número es para el rojo.
        El segundo es para el verde.
        El tercero es para el azul.

    Piensa en estos números como si fueran el "grado de intensidad" de cada color. 
    Un valor de 0.0 significa "nada de ese color", mientras que 
    un valor de 1.0 significa "la máxima cantidad de ese color".
    
    Ejemplos
    Rojo puro       glColor3f(1.0, 0.0, 0.0)
    Verde puro      glColor3f(0.0, 1.0, 0.0)
    Azul puro       glColor3f(0.0, 0.0, 1.0)
    Blanco          glColor3f(1.0, 1.0, 1.0) (¡la mezcla de los tres!)
    Negro           glColor3f(0.0, 0.0, 0.0) (¡la ausencia de los tres!)
    Amarillo        glcolor3f(1.0, 1.0, 0.0)
    Violeta         glcolor3f(1.0, 0.0, 1.0)

    La clave es que, una vez que llamas a glColor3f(), todas las formas que dibujes después 
    tendrán ese color, hasta que lo cambies de nuevo.
    """

import pygame
from pygame.locals import *
from OpenGL.GL import *

def dibujar_triangulo(vertices):
    glBegin(GL_TRIANGLES)
    glVertex2f(vertices[0], vertices[1])
    glVertex2f(vertices[2], vertices[3])
    glVertex2f(vertices[4], vertices[5])
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar un triángulo rojo
        glColor3f(1.0, 0.0, 0.0) # Color rojo
        lados=[-1.0, 0.0, -0.75, 0.5, -0.5, 0.0 ]
        dibujar_triangulo(lados)

        glColor3f(0.0, 0.0, 1.0) # Color azul
        lados=[0.0, 0.0, 0.25, 0.5, 0.5, 0.0 ]
        dibujar_triangulo(lados)

        glColor3f(0.0, 1.0, 0.0) # Color verde
        lados=[-0.5, 1.0, 0.0, 1.0, -0.25, 0.5 ]
        dibujar_triangulo(lados)

        glColor3f(1.0, 1.0, 0.0) # Color amarillo
        lados=[0.5, 1.0, 1.0, 1.0, 0.75, 0.5 ]
        dibujar_triangulo(lados)        

        glColor3f(1.0, 0.0, 1.0) # Color violeta
        lados=[-0.5, -1.0, -0.25, -0.5, 0.0, -1.0 ]
        dibujar_triangulo(lados)

        glColor3f(0.5, 0.5, 0.5) # Color azul
        lados=[0.5, -1.0, 0.75, -0.5, 1.0, -1.0 ]
        dibujar_triangulo(lados)

        pygame.display.flip()

main()