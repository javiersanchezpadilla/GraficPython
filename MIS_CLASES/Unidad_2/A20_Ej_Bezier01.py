import glfw
from OpenGL.GL import *
import numpy as np
puntos = [(-0.8,-0.5),(-0.3,0.8),(0.3,-0.8),(0.8,0.5)]
def bezier(t):
    x = (1-t)**3*puntos[0][0] + 3*(1-t)**2*t*puntos[1][0] + 3*(1-t)*t**2*puntos[2][0] + t**3*puntos[3][0]
    y = (1-t)**3*puntos[0][1] + 3*(1-t)**2*t*puntos[1][1] + 3*(1-t)*t**2*puntos[2][1] + t**3*puntos[3][1]
    return x,y
def dibujar():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)

    for i in range(100):
        t=i/100
        x,y=bezier(t)
        glVertex2f(x,y)
    glEnd()
if not glfw.init():
    exit()
ventana = glfw.create_window(800,600,"Bezier",None,None)
glfw.make_context_current(ventana)
while not glfw.window_should_close(ventana):
    dibujar()
    glfw.swap_buffers(ventana)
    glfw.poll_events()
glfw.terminate()
