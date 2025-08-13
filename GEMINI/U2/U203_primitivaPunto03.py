""" pantalla con muchos puntos """

import glfw
from OpenGL.GL import *
import random 

def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Primitivas en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana

def dibuja_puntos():
       
    for i in range(1000):
        rojo = random.random()
        verde = random.random()
        azul = random.random()
        glColor3f(rojo, verde, azul)        # Color aleatorio del punto
        valor_x = random.random() * 2 - 1   # Genera un valor entre -1 y 1
        valor_y = random.random() * 2 - 1   # Genera un valor entre -1 y 1
        
        glBegin(GL_POINTS)
        glVertex2f(valor_x, valor_y)  # Coordenada de dibujo
        glEnd()


# Aquí pondremos el código para dibujar primitivas
ventana = iniciar_ventana()

glClear(GL_COLOR_BUFFER_BIT)                # Borra solo una vez la pantalla
glClearColor(0, 0, 0, 1)                    # Fondo negro

while not glfw.window_should_close(ventana):
    dibuja_puntos() 
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
