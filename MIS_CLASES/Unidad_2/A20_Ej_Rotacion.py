import glfw
from OpenGL.GL import *
angulo = 0
def dibujar():
    global angulo
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glRotatef(angulo,0,0,1)
    glBegin(GL_QUADS)
    glColor3f(0,0,1)
    glVertex2f(-0.3,-0.3)
    glVertex2f(0.3,-0.3)
    glVertex2f(0.3,0.3)
    glVertex2f(-0.3,0.3)
    glEnd()
    glPopMatrix()
    angulo += 1
if not glfw.init():
    exit()
ventana = glfw.create_window(800,600,"Rotacion",None,None)
glfw.make_context_current(ventana)
while not glfw.window_should_close(ventana):
    dibujar()
    glfw.swap_buffers(ventana)
    glfw.poll_events()
glfw.terminate()
