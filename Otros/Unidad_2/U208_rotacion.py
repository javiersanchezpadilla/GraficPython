""" Rotación: Haciendo que las cosas giren
    Cuando queremos que un obejto gire sobre sí mismo. En OpenGL, esto se hace con un comando muy 
    similar a los que ya hemos visto: glRotatef().

    El comando glRotatef() toma cuatro valores:

    glRotatef(ángulo, x, y, z)

        ángulo: Es el número de grados que quieres que gire tu objeto. 
                Un valor positivo, girará en el sentido contrario a las agujas del reloj. 
                Un valor negativo, lo hará en el sentido de las agujas del reloj.

        x, y, z: Estos tres números definen un "eje de rotación". En 2D, el giro siempre es sobre 
                 el punto central de la pantalla (el eje z), así que siempre usaremos (0.0, 0.0, 1.0).

    Por ejemplo, si quieres girar un objeto 45 grados en sentido contrario a las agujas del reloj, usarías:

    glRotatef(45.0, 0.0, 0.0, 1.0)

    Y si quieres que gire 90 grados en el sentido de las agujas del reloj, harías:

    glRotatef(-90.0, 0.0, 0.0, 1.0)

    Al igual que con la traslación y el escalado, la rotación se aplica a todo lo que se dibuje después 
    de llamar a la función. Es como si pusieras una pequeña ruleta debajo de tu lienzo y lo giraras. 
    Todo lo que dibujes a partir de ese momento estará girado."""

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
    angulo = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0) # Color blanco

        glRotatef(angulo, 0.0, 0.0, 1.0) # Rotamos el triángulo
        dibujar_triangulo()

        angulo += 1 # Aumentamos el ángulo para el siguiente fotograma

        pygame.display.flip()
        pygame.time.wait(200)

main()