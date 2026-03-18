import glfw
from OpenGL.GL import *
tx = 0
def dibujar():
    global tx
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(tx, 0, 0)
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex2f(-0.2,-0.2)
    glVertex2f(0.2,-0.2)
    glVertex2f(0.2,0.2)
    glVertex2f(-0.2,0.2)
    glEnd()
    glPopMatrix()
    tx += 0.01
    if tx > 1:
        tx = -1
if not glfw.init():
    exit()
ventana = glfw.create_window(800,600,"Traslacion",None,None)
glfw.make_context_current(ventana)
while not glfw.window_should_close(ventana):
    dibujar()
    glfw.swap_buffers(ventana)
    glfw.poll_events()
glfw.terminate()
