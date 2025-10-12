""" Aplicación de la rotación sobre un cuadrado
    En este ejemplo el cuadrado rota alrededor de un pivote externo (0, 0) y
    también alrededor de un pivote interno (-0.7, 0.8)

"""

import glfw
from OpenGL.GL import *
import math 
from random import random



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



def rotar_vertice(x, y, p_x, p_y, angulo_grados):
    """
    Calcula la rotación de un punto (x, y) alrededor de un pivote (p_x, p_y) por un ángulo.
    """
    # 1. Convertir el ángulo a radianes
    angulo_rad = math.radians(angulo_grados)
   
    # 2. Trasladar al origen
    x_trasladado = x - p_x
    y_trasladado = y - p_y
    
    # 3. Rotar
    x_prima = x_trasladado * math.cos(angulo_rad) - y_trasladado * math.sin(angulo_rad)
    y_prima = x_trasladado * math.sin(angulo_rad) + y_trasladado * math.cos(angulo_rad)
    
    # 4. Trasladar de vuelta
    x_final = x_prima + p_x
    y_final = y_prima + p_y

    return [x_final, y_final]


def dibuja_ejes():
    """
    Dibuja los ejes coordenados.
    """
    glBegin(GL_LINES)                   # Dibuja los ejes
    glColor3f(0.3, 0.3, 0.4)            # Ejes en color gris
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()



def dibuja_cuadrado(vertice, pivote_ext, pivote_int):
    """
    Dibuja un cuadrado de acuerdo a las coordenadas de vertice.
    """
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(vertice[0], vertice[1])
    glVertex2f(vertice[2], vertice[3])
    glVertex2f(vertice[4], vertice[5])
    glVertex2f(vertice[6], vertice[7])
    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(pivote_ext[0], pivote_ext[1])
    glVertex2f(pivote_int[0], pivote_int[1])
    glEnd()



def dibuja(pivote_ext, angulo_ext, pivote_int, angulo_int, vertices):
    """
    Rota un punto (x, y) alrededor de un pivote (p_x, p_y) por un ángulo.
    """
    glClearColor(0.0, 0.0, 0.0, 1.0)    # Limpia la pantalla
    glClear(GL_COLOR_BUFFER_BIT)       # Si quitamos esta linea, veremos el rastro del punto
    glColor3f(0.0, 1.0, 1.0)            # Color amarillo brillante

    dibuja_ejes()
    # Primero dibuja los vertices originales del cuadro
    dibuja_cuadrado(vertices, pivote_ext, pivote_int)

    # Luego rota cada vertice y actualiza sus coordenadas para la siguiente iteración
    vertices[0], vertices[1] = rotar_vertice(vertices[0], vertices[1], pivote_ext[0], pivote_ext[1], angulo_ext)
    vertices[2], vertices[3] = rotar_vertice(vertices[2], vertices[3], pivote_ext[0], pivote_ext[1], angulo_ext)
    vertices[4], vertices[5] = rotar_vertice(vertices[4], vertices[5], pivote_ext[0], pivote_ext[1], angulo_ext)
    vertices[6], vertices[7] = rotar_vertice(vertices[6], vertices[7], pivote_ext[0], pivote_ext[1], angulo_ext)
    pivote_int[0], pivote_int[1] = rotar_vertice(pivote_int[0], pivote_int[1], pivote_ext[0], pivote_ext[1], angulo_ext)
   
    # Ahora rotamos con referencia al centro del cuadrado
    vertices[0], vertices[1] = rotar_vertice(vertices[0], vertices[1], pivote_int[0], pivote_int[1], angulo_int)
    vertices[2], vertices[3] = rotar_vertice(vertices[2], vertices[3], pivote_int[0], pivote_int[1], angulo_int)
    vertices[4], vertices[5] = rotar_vertice(vertices[4], vertices[5], pivote_int[0], pivote_int[1], angulo_int)
    vertices[6], vertices[7] = rotar_vertice(vertices[6], vertices[7], pivote_int[0], pivote_int[1], angulo_int)
    


if __name__ == "__main__":
    ventana = iniciar_ventana()
    # si queremos que rota en sentido inverso, cambiar el signo del angulo
    angulo_grados_externo = 2.0
    angulo_grados_interno = -5.0
    pivote_externo = [0.0, 0.0]
    pivote_interno = [-0.65, 0.65]
    vertices = [-0.7, 0.7, -0.6, 0.7, -0.6, 0.6, -0.7, 0.6]

    while not glfw.window_should_close(ventana):
        dibuja(pivote_externo, angulo_grados_externo, pivote_interno, angulo_grados_interno, vertices)
        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()
