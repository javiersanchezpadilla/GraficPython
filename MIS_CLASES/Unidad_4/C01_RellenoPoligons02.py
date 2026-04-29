""" RELLENO DE POLIGONOS.

    2. Relleno con Color Degradado (Smooth Shading)
    -----------------------------------------------
    El color degradado ocurre cuando los colores se mezclan suavemente entre 
    un punto y otro. Es como si pusieras pintura roja en una esquina y azul 
    en otra, y las barrieras con un pincel en el centro.

    ¿Cómo funciona?: Le asignas un glColor3f distinto a cada vértice.
    Concepto clave: OpenGL hace un proceso llamado 'Interpolación'. 
    Si el punto A es Rojo y el punto B es Azul, el píxel que está justo en 
    medio será Morado automáticamente.

    Ejemplo 2: Triángulo con degradado (Interpolación)
"""
import glfw
from OpenGL.GL import *

def dibujar_triangulo_degradado():
    glBegin(GL_TRIANGLES)
    
    # Vertice 1: Rojo
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.6, -0.5)
    
    # Vertice 2: Verde
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.6, -0.5)
    
    # Vertice 3: Azul
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.6)
    
    glEnd()

def main():
    if not glfw.init(): return
    ventana = glfw.create_window(600, 600, "Color Degradado", None, None)
    glfw.make_context_current(ventana)

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        dibujar_triangulo_degradado()
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()

main()
