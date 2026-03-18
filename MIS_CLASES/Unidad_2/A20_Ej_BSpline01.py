import glfw
from OpenGL.GL import *
import numpy as np
p=[(-0.8,-0.5),(-0.4,0.6),(0.2,-0.7),(0.8,0.5)]
def bspline(t):
    b0=((1-t)**3)/6
    b1=(3*t**3-6*t**2+4)/6
    b2=(-3*t**3+3*t**2+3*t+1)/6
    b3=t**3/6
    x=b0*p[0][0]+b1*p[1][0]+b2*p[2][0]+b3*p[3][0]
    y=b0*p[0][1]+b1*p[1][1]+b2*p[2][1]+b3*p[3][1]

    return x,y
def dibujar():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)
    for i in range(100):
        t=i/100
        x,y=bspline(t)
        glVertex2f(x,y)
    glEnd()
if not glfw.init():
    exit()
ventana = glfw.create_window(800,600,"B-Spline",None,None)
glfw.make_context_current(ventana)
while not glfw.window_should_close(ventana):
    dibujar()
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
