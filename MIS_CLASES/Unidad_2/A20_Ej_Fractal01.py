import glfw
from OpenGL.GL import *
import math

def rama(x,y,angulo,longitud,n):
    if n==0:
        return
    x2=x+math.cos(math.radians(angulo))*longitud
    y2=y+math.sin(math.radians(angulo))*longitud
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(x2,y2)
    glEnd()
    rama(x2,y2,angulo+30,longitud*0.7,n-1)
    rama(x2,y2,angulo-30,longitud*0.7,n-1)
def dibujar():
    glClear(GL_COLOR_BUFFER_BIT)
    rama(0,-0.9,90,0.3,8)
if not glfw.init():
    exit()
ventana = glfw.create_window(800,600,"Fractal",None,None)
glfw.make_context_current(ventana)
while not glfw.window_should_close(ventana):
    dibujar()
    glfw.swap_buffers(ventana)
    glfw.poll_events()
glfw.terminate()
