import glfw
from OpenGL.GL import *
import numpy as np
puntos = np.array([
[-0.2,-0.2,1],
[0.2,-0.2,1],
[0.2,0.2,1],
[-0.2,0.2,1]
])
matriz = np.array([
[1,0,0.3],
[0,1,0.2],
[0,0,1]
])
nuevo = puntos @ matriz.T
def dibujar():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    for p in nuevo:
        glVertex2f(p[0],p[1])
    glEnd()
if not glfw.init():
    exit()
ventana = glfw.create_window(800,600,"Transformacion Matricial",None,None)
glfw.make_context_current(ventana)
while not glfw.window_should_close(ventana):
    dibujar()
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
