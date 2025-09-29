""" En este ejercicio dibujaremos cuadros de diferentes colores usando la primitiva GL_QUADS.
    Cada cuadro estara formado por cuatro vertices.
    Los cuadros se dibujaran en las cuatro esquinas de la ventana.
    Se usaran colores aleatorios para cada cuadro.
    Ademas las cordenadas de los vertices se almacenaran en listas para facilitar su manejo.
    En este caso dibujaremos un cuadro cada medio segundo en una posicion y con un tamaño aleatorio.
    Haremos uso de la funcion time.sleep(segundos) para crear la pausa entre cuadros.
"""

import glfw
from OpenGL.GL import *
import random
import time


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


def dibuja_cuadro(vert_esq_sup_izq, tamanio):
    """ Dibuja cuadros. 
        param vert_esq_sup_izq: tupla (x, y) con la esquina superior izquierda del cuadro
        param tamanio: tamaño del cuadro (lado)
    """     
    glBegin(GL_QUADS)
    glColor3f(random.random(), random.random(), random.random())   # Color aleatorio del cuadro
    glVertex2f(vert_esq_sup_izq[0], vert_esq_sup_izq[1])                         # Coordenada de dibujo
    glVertex2f(vert_esq_sup_izq[0] + tamanio, vert_esq_sup_izq[1])             # Coordenada de dibujo
    glVertex2f(vert_esq_sup_izq[0] + tamanio, vert_esq_sup_izq[1] - tamanio) # Coordenada de dibujo
    glVertex2f(vert_esq_sup_izq[0], vert_esq_sup_izq[1] - tamanio)             # Coordenada de dibujo
    glEnd()


def dibuja():
    posicion_x = random.uniform(-1, 0.5)
    posicion_y = random.uniform(-0.5, 1)
    tamanio = random.uniform(0.1, 0.5)
    dibuja_cuadro((posicion_x, posicion_y + tamanio), tamanio)


if __name__ == "__main__":
    ventana = iniciar_ventana()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    while not glfw.window_should_close(ventana):
        
        dibuja()         
        glfw.swap_buffers(ventana)
        glfw.poll_events()
        time.sleep(0.5)             # Espera medio segundo antes de dibujar el siguiente cuadro


    glfw.terminate()
