""" Matemáticas para artistas: Representación matricial
    Imagínate que las transformaciones (traslación, escalado, etc.) son como pequeñas 
    instrucciones que le das a OpenGL. En lugar de darle una lista de instrucciones 
    sueltas, OpenGL prefiere guardarlas todas juntas en una "tabla mágica" llamada matriz.

    Una matriz, en este contexto, es solo una cuadrícula de números. En OpenGL, usamos 
    matrices de 4x4. Cada matriz puede "guardar" una transformación, como mover algo, 
    girarlo o cambiar su tamaño.

    Cuando quieres aplicar varias transformaciones a un objeto, no necesitas hacerlas una 
    por una. En cambio, OpenGL combina todas esas matrices en una sola matriz final. 
    Es como si todas tus instrucciones de mover y escalar se fusionaran en una sola 
    instrucción súper potente.

    El orden en que haces esto es clave.

    Si primero escalas y luego trasladas: traslación * escalado * vértice
    Si primero trasladas y luego escalas: escalado * traslación * vértice

    Como la multiplicación de matrices no es conmutativa (es decir, el orden importa, 
    A * B no es lo mismo que B * A), el resultado final será diferente.

    Aquí está la magia:

    glPushMatrix(): Es como guardar la posición y el tamaño actuales de tu objeto en una pila.
    glPopMatrix(): Es como volver a la posición y el tamaño que guardaste antes.

    Esto te permite dibujar un objeto, guardarlo, hacerle cambios (como moverlo), dibujar 
    otro objeto, y luego restaurar la posición para el siguiente objeto, sin que se afecten 
    entre sí."""

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

        # Triángulo central (no se mueve ni rota)
        glColor3f(0.0, 1.0, 0.0)
        dibujar_triangulo()

        # Guarda la matriz actual para que el triángulo central no se vea afectado
        glPushMatrix()

        # Dibujamos un triángulo pequeño que orbita
        glRotatef(angulo, 0.0, 0.0, 1.0)
        glTranslatef(0.4, 0.0, 0.0) # Lo movemos a 0.4 unidades del centro
        glScalef(0.2, 0.2, 1.0) # Lo hacemos pequeño
        glColor3f(1.0, 0.0, 0.0)
        dibujar_triangulo()

        # Restaura la matriz para que las siguientes figuras no se vean afectadas
        glPopMatrix()

        angulo += 1

        pygame.display.flip()
        pygame.time.wait(100)

main()
