""" RELLENO DE POLIGONOS.

    Ejemplo 3: Cuadrado con degradado complejo
    En este caso, cada esquina tiene un color, creando una mezcla en todo el 
    polígono.
"""
import glfw
from OpenGL.GL import *

def dibujar_cuadrado_arcoiris():
    glBegin(GL_QUADS)
    
    glColor3f(1, 0, 0) # Rojo (Abajo Izquierda)
    glVertex2f(-0.5, -0.5)
    
    glColor3f(0, 1, 0) # Verde (Abajo Derecha)
    glVertex2f(0.5, -0.5)
    
    glColor3f(0, 0, 1) # Azul (Arriba Derecha)
    glVertex2f(0.5, 0.5)
    
    glColor3f(1, 1, 0) # Amarillo (Arriba Izquierda)
    glVertex2f(-0.5, 0.5)
    
    glEnd()

def main():
    if not glfw.init(): return
    ventana = glfw.create_window(600, 600, "Cuadrado Arcoiris", None, None)
    glfw.make_context_current(ventana)

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        dibujar_cuadrado_arcoiris()
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()

main()
