""" El arte de mover las cosas: Traslación y Escalado
    La traslación es mover un objeto de un lado a otro del escenario, sin cambiar su tamaño. 
    El escalado es como si la hicieras más grande o más pequeña. 
    
    En OpenGL, hacemos esto con comandos muy específicos.

    Traslación (mover las cosas)
    Para mover una forma, usamos el comando glTranslatef(x, y, z). Aquí, le decimos a OpenGL 
    cuánto queremos mover la forma en las direcciones x, y y z. Como estamos trabajando en 2D, 
    el valor de z casi siempre será 0.0.

        glTranslatef(0.5, 0.0, 0.0)     # Movería la forma 0.5 unidades a la derecha.
        glTranslatef(-0.5, 0.0, 0.0)    # Movería la forma 0.5 unidades a la izquierda.

    Escalado (hacer las cosas más grandes o más pequeñas)
    Para cambiar el tamaño de una forma, usamos glScalef(x, y, z). Con este comando, le decimos 
    a OpenGL cuánto queremos multiplicar el tamaño de la forma en cada dirección.

        glScalef(2.0, 1.0, 1.0)         # Duplicaría el ancho de la forma, pero mantendría su altura.
        glScalef(0.5, 0.5, 1.0)         # Haría la forma la mitad de su tamaño original, tanto en 
                                        # ancho como en alto.

    Es importante recordar que estas transformaciones se aplican a todo lo que se dibuje después de 
    llamar a estos comandos, no a las cosas que ya están en la pantalla. Piensa en ello como si 
    estuvieras ajustando la "cámara" antes de tomar una foto: todos los objetos que aparezcan en la 
    foto se verán afectados por el ajuste que hayas hecho."""

import pygame
from pygame.locals import *
from OpenGL.GL import *

def dibujar_triangulo():
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
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
        glColor3f(1.0, 1.0, 1.0) # Color blanco

        # Triángulo original (en el centro)
        dibujar_triangulo()

        # Guardamos la matriz actual (la del triángulo central)
        glPushMatrix() 

        # Triángulo escalado y trasladado
        glScalef(0.5, 0.5, 1.0) # Lo hacemos la mitad de grande
        glTranslatef(1.0, 1.0, 0.0) # Lo movemos a la esquina superior derecha
        dibujar_triangulo()

        # Restaura la matriz guardada, para que el triángulo original no se vea afectado
        glPopMatrix()

        pygame.display.flip()

main()