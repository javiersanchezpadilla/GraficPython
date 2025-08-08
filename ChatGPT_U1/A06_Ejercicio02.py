""" En este ejemplo se dibujaran primitivas en OpenGL.
    para el uso de for la funcion range no admite flotantes, por lo que nos
    apoyaremos en la libreria numpy con la funcion np.arange() para crear un rango 
    de valores flotantes.
   
    """

import glfw
from OpenGL.GL import *
import numpy as np

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
    glClearColor(0.5, 0.5, 0.5, 0)  # Fondo gris claro

    glColor3f(0.1, 0.1, 0.1)                    # Dibujar una cuadrícula
    for punto in np.arange(-1.0, 1.0, 0.1):
        glBegin(GL_LINES)
        glVertex2f(punto, -1)
        glVertex2f(punto, 1)
        glVertex2f(-1, punto)
        glVertex2f(1, punto)
        glEnd()

        glColor3f(1.0,0.0,0.0);
        glBegin(GL_TRIANGLES);
        glVertex2i(1,160);
        glVertex2i(20,190);
        glVertex2i(40,160);
        glEnd();

#   glBegin(GL_LINES);
#     glVertex2i(60,170); glVertex2i(60,190);
#     glVertex2i(60,190); glVertex2i(80,190);
#     glVertex2i(80,190); glVertex2i(80,200);
#     glVertex2i(80,200); glVertex2i(100,180);
#     glVertex2i(100,180); glVertex2i(80,160);
#     glVertex2i(80,160); glVertex2i(80,170);
#     glVertex2i(80,170); glVertex2i(60,170);
#    glEnd();

#    glBegin(GL_LINE_STRIP);
#     glVertex2i(110,170); glVertex2i(110,190);
#     glVertex2i(130,190); glVertex2i(130,200);
#     glVertex2i(150,180); glVertex2i(130,160);
#     glVertex2i(130,170); glVertex2i(110,170);
#    glEnd();

#    glBegin(GL_LINE_LOOP);
#     glVertex2i(160,170); glVertex2i(160,190);
#     glVertex2i(180,190); glVertex2i(180,200);
#     glVertex2i(200,180); glVertex2i(180,160);
#     glVertex2i(180,170); 
#    glEnd();

#    glBegin(GL_QUADS);
#     glVertex2i(10, 90); glVertex2i(20,120);
#     glVertex2i(60,120); glVertex2i(50,90);
#    glEnd();

#    glBegin(GL_POLYGON);
#     glVertex2i(80, 90); glVertex2i(70,120);
#     glVertex2i(90,140); glVertex2i(110,120); glVertex2i(100,90);
#    glEnd();

#     glBegin(GL_POLYGON);
#     glVertex2i(10, 50); glVertex2i(20,70);  glVertex2i(40,70);
#     glVertex2i(50, 50); glVertex2i(40,30); glVertex2i(20,30);
#    glEnd();

#    glBegin(GL_LINE_LOOP);
#       glVertex2i(100,20); glVertex2i(130,20);  glVertex2i(130,50); glVertex2i(100,50);
#    glEnd();

#    glBegin(GL_LINE_LOOP);
#     glVertex2i(110, 30); glVertex2i(140,30); glVertex2i(140,60);  glVertex2i(110,60);
#    glEnd();


#    glBegin(GL_LINES);
#     glVertex2i(100, 20); glVertex2i(110,30); glVertex2i(130,20);  glVertex2i(140,30);
#     glVertex2i(130, 50); glVertex2i(140,60); glVertex2i(100,50);  glVertex2i(110,60);
#     glEnd();

#     glColor3f(1.0,1.0,1.0);
#     for (int x=130;x<190;x=x+3)
#         for (int y=70; y<140; y=y+3)
#             { glBegin(GL_POINTS);
#                  glVertex2i(x,y);
#               glEnd();
#             }

#     glBegin(GL_TRIANGLE_STRIP);
#        glVertex2i(120, 120); glVertex2i(130,150); glVertex2i(140,120);
#        glVertex2i(160, 150);
#        glVertex2i(180, 110);
#        glVertex2i(200,160);
#     glEnd();


















    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
