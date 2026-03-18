import glfw
from OpenGL.GL import *
escala = 1
def dibujar():
    global escala
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glScalef(escala, escala, 1)
    glBegin(GL_QUADS)
    glColor3f(0,1,0)
    glVertex2f(-0.3,-0.3)
    glVertex2f(0.3,-0.3)
    glVertex2f(0.3,0.3)
    glVertex2f(-0.3,0.3)
    glEnd()
    glPopMatrix()
    escala += 0.01
    if escala > 2:
        escala = 1
if not glfw.init():
    exit()
ventana = glfw.create_window(800,600,"Escalamiento",None,None)
glfw.make_context_current(ventana)
while not glfw.window_should_close(ventana):
    dibujar()
    glfw.swap_buffers(ventana)
    glfw.poll_events()
glfw.terminate()
