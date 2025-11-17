"""
    ¿Cómo Instalar las Dependencias?

    pip install PyOpenGL PyOpenGL_accelerate glfw

    Explicación Visual, Imagina que:

        Ángulo 45°      Como mirar a través de un telescopio corto
        Ángulo 90°      Visión periférica normal
        Cerca=0.1       No ves objetos más cerca de 10cm
        Lejos=100       No ves objetos más lejos de 100 metros

    Efectos de Cambiar los Parámetros

    # Visión de ángulo amplio (como ojo de pez)
    gluPerspective(120, ancho/alto, 0.1, 100.0)

    # Visión telescópica (como mirar con binoculares)
    gluPerspective(20, ancho/alto, 0.1, 100.0)

    # Campo de visión muy cercano
    gluPerspective(45, ancho/alto, 10.0, 100.0)  # Solo objetos lejanos


"""


import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Variables globales
rotation_x = 0.0
rotation_y = 0.0


def inicializar_ventana():
    if not glfw.init():
        return None
    
    # Crear ventana
    ventana = glfw.create_window(800, 600, "Ejemplo de Perspectiva - OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        return None
    
    glfw.make_context_current(ventana)
    return ventana


def configurar_perspectiva(ancho, alto):
    # Configurar viewport
    glViewport(0, 0, ancho, alto)
    
    # Configurar proyección en perspectiva
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # ¡Aquí está la magia de la perspectiva!
    gluPerspective(
        45,                 # 45° - ángulo de visión (como unos binoculares)
        ancho/alto,         # Relación de aspecto (forma de la ventana)
        0.1,                # Distancia mínima visible (muy cercano)
        100.0               # Distancia máxima visible (muy lejano)
    )
    
    # Volver al modo de modelo/vista
    glMatrixMode(GL_MODELVIEW)


def dibujar_cubo():
    # Dibujar un cubo simple con caras de colores
    glBegin(GL_QUADS)
    
    # Cara frontal (roja)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    
    # Cara trasera (verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    
    # Cara superior (azul)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    
    # Cara inferior (amarilla)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    
    # Cara derecha (magenta)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    
    # Cara izquierda (cyan)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    
    glEnd()


def main():
    ventana = inicializar_ventana()
    if not ventana:
        return
    
    # Configurar perspectiva inicial
    ancho, alto = glfw.get_window_size(ventana)
    configurar_perspectiva(ancho, alto)
    
    # Habilitar depth testing para perspectiva correcta
    glEnable(GL_DEPTH_TEST)
    
    while not glfw.window_should_close(ventana):
        # Limpiar buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Configurar cámara
        gluLookAt(
            0, 0, 5,    # Posición de la cámara (x, y, z)
            0, 0, 0,    # Punto al que mira (x, y, z)
            0, 1, 0     # Vector "arriba" (x, y, z)
        )
        
        # Rotar el cubo
        global rotation_x, rotation_y
        rotation_x += 0.5
        rotation_y += 0.3

        # Lo que se busca con estas dos rotaciones son distintas velocidades, 
        # una para el eje "x"
        glRotatef(rotation_x, 1, 0, 0)
        # y la otra para el eje "y"
        glRotatef(rotation_y, 0, 1, 0)
        # glRotatef(rotation_x, 1, 1, 0)
        
        # Dibujar escena
        dibujar_cubo()
        
        # Intercambiar buffers y procesar eventos
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()


if __name__ == "__main__":
    main()