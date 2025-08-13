""" Esta función inicializa una ventana OpenGL usando GLFW.
    La estemos utilizando para dibujar primitivas en OpenGL.
    
    Las coordenadas están normalizadas: X e Y van de -1 a 1.
    Un triángulo verde apuntando hacia arriba.
    
        Concepto	                Descripción
    glBegin(...)	    Inicia el dibujo de una primitiva
    glVertex2f(x,y)	    Establece una coordenada 2D
    glColor3f(r,g,b)	Establece el color (valores entre 0 y 1)
    glEnd()	            Finaliza la primitiva

    Coordenadas	De -1 a 1 tanto en X como Y
    """

import glfw
from OpenGL.GL import *

def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Primitivas en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana

# Aquí pondremos el código para dibujar primitivas
ventana = iniciar_ventana()

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.9, 0.9, 0.9, 1)  # Fondo gris claro

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)  # Verde
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glEnd()

    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
