""" Ahora el cubo tendrá transformaciones"""


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
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    ancho, alto = display
    
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (ancho/alto), 0.1, 50.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Nueva variable para el ángulo de rotación
    rotacion_y = 0.0
    rotacion_x = 0.0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        
        # Rotamos el cubo en el eje Y y X
        glRotatef(rotacion_y, 0, 1, 0)
        glRotatef(rotacion_x, 1, 0, 0)
        
        dibujar_cubo()
        
        pygame.display.flip()
        
        # Incrementamos los ángulos de rotación en cada fotograma
        rotacion_y += 1.0
        rotacion_x += 0.5

        pygame.time.wait(100)

main()
