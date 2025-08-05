""" Ahora que tenemos nuestro lienzo (la ventana), podemos empezar a dibujar en él. 
    En OpenGL, todo se dibuja a partir de puntos, líneas y triángulos. Es como si los puntos fueran 
    los pequeños bloques de LEGO, y las líneas y triángulos las formas más grandes que puedes crear 
    con ellos. Con estos bloques básicos, puedes construir cualquier cosa, desde un personaje de 
    videojuego hasta un paisaje completo.

    Para dibujar estas formas, necesitamos seguir tres pasos:

    1) Decirle a OpenGL lo que vamos a dibujar: Con el comando glBegin(....), le decimos a OpenGL qué 
       tipo de forma queremos dibujar (puntos, líneas, triángulos, etc.).

    2) Definir los vértices: Un vértice es un punto en el espacio. Usamos el comando glVertex2f(x, y) 
       para decirle a OpenGL dónde se encuentra cada punto de nuestra forma. Los números dentro del 
       paréntesis son las coordenadas x e y en la ventana.

    3) Terminar de dibujar: Con el comando glEnd(), le decimos a OpenGL que hemos terminado de definir 
       la forma y que ya puede dibujarla.
"""

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
        
        # Definimos los 3 vértices del triángulo (x, y)
        glVertex2f(-0.5, -0.5)  # vertice 1
        glVertex2f(0.5, -0.5)   # vertice 2
        glVertex2f(0.0, 0.5)    # vertice 3
        
        glEnd() # Le decimos a OpenGL que ya hemos terminado

        pygame.display.flip()
        pygame.time.wait(10)

main()

