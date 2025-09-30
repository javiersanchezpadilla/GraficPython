""" En este ejercicio se dibujara un cuadro el cual se animara moviendose de izquierda a derecha.
    El cuadro se dibujara en el centro de la ventana.
    y rebotara al llegar a los bordes de la ventana.
"""

import glfw
from OpenGL.GL import *
import numpy as np
import time

# Variables globales para el estado del cuadro
posicion_x = -0.9       # Posición inicial en el lado izquierdo
velocidad_x = 0.01      # Velocidad de movimiento
tamanio_cuadro = 0.2


def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Mi primera ventana como funcion en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


def dibujar_cuadro(x, tamanio):
    """
    La función `dibujar_cuadro` dibuja un cuadrado en la posición x con un tamaño específico.
    
    :param x: El parámetro `x` en la función `dibujar_cuadro` representa la coordenada x del
    Posición donde se dibujará el cuadrado. Determina la posición horizontal de la esquina superior izquierda.
    esquina del cuadrado en la pantalla o lienzo
    :param tamanio: El parámetro `tamanio` representa el tamaño del cuadrado que deseas dibujar. Es
    Se utiliza para determinar las dimensiones del cuadrado en relación con su posición `x`. el valor de
    `tamanio` determinará el ancho y alto del cuadrado

    """
    #Dibuja un cuadrado en la posición x.
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x, tamanio)
    glVertex2f(x + tamanio, tamanio)
    glVertex2f(x + tamanio, -tamanio)
    glVertex2f(x, -tamanio)
    glEnd()


def programa_principal():
    """
    Esta función de Python crea una animación simple de un cuadrado que se mueve horizontalmente dentro 
    de una ventana. utilizando OpenGL.
    """
    global posicion_x, velocidad_x
    ventana = iniciar_ventana()
    
    while not glfw.window_should_close(ventana):
        # 1. Limpiar la pantalla con el color de fondo
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        # 2. Actualizar la posición
        posicion_x += velocidad_x
        
        # Invertir la dirección si el cuadro llega a un borde
        if posicion_x + tamanio_cuadro >= 1.0 or posicion_x <= -1.0:
            velocidad_x *= -1

        # 3. Dibujar el cuadro en la nueva posición
        dibujar_cuadro(posicion_x, tamanio_cuadro)
        
        # 4. Intercambiar búferes para mostrar el resultado
        glfw.swap_buffers(ventana)
        
        # Procesar eventos (clics, etc.)
        glfw.poll_events()
    
    glfw.terminate()


# LLamado al programa principal de control
if __name__ == "__main__":
    programa_principal()
