""" Un cubo está hecho de 6 caras, y cada cara es un cuadrado. Para que OpenGL sepa qué dibujar, 
    necesitamos definir los 8 vértices que forman el cubo y luego dibujar las 6 caras usando esos 
    vértices.

    Aquí hay algunos puntos clave que debes notar en el código:

    glTranslatef(0.0, 0.0, -5.0): Trasladamos nuestro cubo 5 unidades en la dirección z negativa. 
    Esto lo aleja de la cámara para que podamos verlo, de lo contrario, la cámara estaría dentro 
    del cubo y no veríamos nada.

    glBegin(GL_QUADS): Para dibujar el cubo, usaremos la primitiva GL_QUADS, que dibuja un cuadrado 
    por cada cuatro vértices que le pases.

    glVertex3f(): Fíjate que ahora usamos glVertex3f() con tres coordenadas, (x, y, z), para cada 
    vértice.

    Código completo. Lo único nuevo es la función dibujar_cubo() y la llamada a esa función en el bucle principal."""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def dibujar_cubo():
    glBegin(GL_QUADS)
    # Cara frontal (rojo)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    
    # Cara trasera (verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    
    # Cara superior (azul)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    
    # Cara inferior (amarillo)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    
    # Cara derecha (cian)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    
    # Cara izquierda (magenta)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)

    # gluPerspective(45, (800/600), 0.1, 50.0): La lente de la cámara
    # Este comando es el que realmente configura esa lente. Le dice a 
    # OpenGL qué tipo de vista quieres:

    # 45  El ángulo de visión (Field of View o FOV). Un ángulo de 45 grados 
    #     es un valor común, similar a lo que el ojo humano ve. Un ángulo más 
    #     grande sería como usar una lente de gran angular, y uno más pequeño 
    #     como un zoom.

    # (800/600)  La relación de aspecto de la ventana. Esto asegura que el 
    #            mundo 3D no se vea estirado o comprimido.

    # 0.1 y 50.0  Los planos de recorte. OpenGL solo dibujará los objetos que 
    #             estén entre 0.1 y 50.0 unidades de distancia 
    # de la cámara. Todo lo que esté fuera de ese rango no se mostrará.

    gluPerspective(45, (800/600), 0.1, 50.0)


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        
        dibujar_cubo()
        
        pygame.display.flip()

main()