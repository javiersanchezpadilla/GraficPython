""" Ejemplo en OpenGL (MUY BÁSICO)

    Este código solo dibuja dos cuadrados (en realidad son polígonos en 3D, pero planos), 
    uno más cercano y otro más lejos, y podrás alternar entre perspectiva y ortográfica 
    con la tecla ESPACIO.

    Qué vas a notar al probarlo

    Al inicio está en perspectiva:
    El cuadrado rojo (cercano) se verá más grande.
    El cuadrado azul (lejano) se verá más pequeño.
    Si presionas ESPACIO cambia a ortográfica:
    Ambos cuadrados (rojo y azul) se ven del mismo tamaño, aunque estén a distinta distancia.

    Con esto queda clara la diferencia:

    Perspectiva = realismo.
    Ortográfica = precisión.
"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Manejo de tres dimensiones en OpenGL (PROFUNDIDAD)", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana



modo_perspectiva = True

def key_callback(window, key, scancode, action, mods):
    global modo_perspectiva
    if key == glfw.KEY_SPACE and action == glfw.PRESS:
        modo_perspectiva = not modo_perspectiva

glfw.set_key_callback(window, key_callback)

def dibujar_escena():
    # Cuadrado cercano (rojo)
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -3)  # Más cercano (z=-3)
    glVertex3f( 1, -1, -3)
    glVertex3f( 1,  1, -3)
    glVertex3f(-1,  1, -3)
    glEnd()

    # Cuadrado lejano (azul)
    glColor3f(0, 0, 1)
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -7)  # Más lejano (z=-7)
    glVertex3f( 1, -1, -7)
    glVertex3f( 1,  1, -7)
    glVertex3f(-1,  1, -7)
    glEnd()

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    ancho, alto = glfw.get_framebuffer_size(window)

    # --- Configurar proyección ---
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if modo_perspectiva:
        gluPerspective(60, ancho / alto, 0.1, 50)   # Perspectiva
    else:
        glOrtho(-2, 2, -2, 2, -10, 10)              # Ortográfica

    # --- Cámara ---
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0)

    dibujar_escena()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()


"""

import glfw
from OpenGL.GL import *



def key_callback(window, key, scancode, action, mods):
    
    # Solo procesamos eventos cuando la tecla es PRESIONADA o REPETIDA
    if action == glfw.PRESS or action == glfw.REPEAT:
        
        # 2. Identificación de Teclas
        if key == glfw.KEY_UP:
            print("Flecha Arriba presionada")
   

def dibujar_cuadro(x, tamanio):

    #Dibuja un cuadrado en la posición x.
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x, tamanio)
    glVertex2f(x + tamanio, tamanio)
    glVertex2f(x + tamanio, -tamanio)
    glVertex2f(x, -tamanio)
    glEnd()



def programa_principal():
    
    ventana = iniciar_ventana()
    # **********************************************
    # * ESTA LÍNEA ES CLAVE: Registro del Callback *
    # **********************************************
    glfw.set_key_callback(ventana, key_callback)
    
    while not glfw.window_should_close(ventana):
        # 1. Limpiar la pantalla con el color de fondo
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Dibujar el cuadro
        dibujar_cuadro(-0.5, 0.2)
        
        # Intercambiar búferes para mostrar el resultado
        glfw.swap_buffers(ventana)
        
        # Procesar eventos (clics, etc.)
        glfw.poll_events()
    
    glfw.terminate()


# LLamado al programa principal de control
if __name__ == "__main__":
    programa_principal()


"""