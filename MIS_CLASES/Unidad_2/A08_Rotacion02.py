""" Ecuación de Rotación Alrededor de un Pivote (p_x, p_y) que no es el origen

    El proceso es como "engañar" al sistema de coordenadas para que piense que el pivote 
    es el origen, rotar, y luego devolver el punto a su lugar.

    El pivote es P=(p_x, p_y)

    El punto a rotar es A=(x,y)
    El ángulo de rotación es angulo_en_grados convertido a radianes

    PASO 1: Trasladar al Origen (Restar el Pivote)
    Restamos las coordenadas del pivote a las coordenadas del punto para que el pivote actúe 
    como si estuviera en (0,0), básicamente Mueve el punto (x, y) para que el punto de 
    rotación (p_x, p_y) se convierta en el origen

        x_trasladado = x - p_x
        y_trasladado = y - p_y

    PASO 2. Rotar el punto trasladado (Aplica la ecuación de rotación sobre el punto trasladado)
    Aplicamos la ecuación de rotación al punto trasladado.

    x_prima = x_trasladado * math.cos(angulo_rad) - y_trasladado * math.sin(angulo_rad)
    y_prima = x_trasladado * math.sin(angulo_rad) + y_trasladado * math.cos(angulo_rad)
    
    PASO 3: Trasladar de Vuelta (Sumar el Pivote)
    Finalmente, sumamos las coordenadas del pivote a las nuevas coordenadas para devolver 
    el punto al sistema de coordenadas original.

    x_final = x_prima + p_x
    y_final = y_prima + p_y

    IMPORTANTE!!! No olvidar que en este ejercicio su ocupa directamente la a traves de la libreria math
    la conversion de grados a radianes con math.radians(angulo_en_grados), pero en el ejercicio A08_Rotacion01.py
    se hizo manualmente con angulo_grados * (pi / 180)
"""

import glfw
from OpenGL.GL import *
import math 


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


def rotar_punto(x, y, p_x, p_y, angulo_grados):
    """
    Rota un punto (x, y) alrededor de un pivote (p_x, p_y) por un ángulo.
    """

    glClearColor(0.0, 0.0, 0.0, 1.0)    # Limpia la pantalla
    #glClear(GL_COLOR_BUFFER_BIT)       # Si quitamos esta linea, veremos el rastro del punto
    glColor3f(1.0, 1.0, 0.0)            # Color amarillo brillante

    glBegin(GL_LINES)                   # Dibuja los ejes
    glColor3f(1.0, 1.0, 1.0)            # Ejes en color blanco
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)    

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
  
    
    # Dibuja un punto en las coordenadas (x, y)
    glPointSize(5)  # Tamaño del punto
    glBegin(GL_POINTS)
    glVertex2f(x_final, y_final)
    glEnd()

    return (x_final, y_final)


if __name__ == "__main__":
    ventana = iniciar_ventana()
    angulo_en_grados = 1    # Ángulo de rotación en grados

    # Ejemplo con los puntos (0.8, 0.8) y pivote en (0.5, 0.5)
    punto_original = (0.8, 0.8)
    pivote = (0.5, 0.5)

    while not glfw.window_should_close(ventana):
        rotar_punto(punto_original[0], punto_original[1], pivote[0], pivote[1], angulo_en_grados)
        angulo_en_grados += 0.9  # Incrementa el ángulo para la próxima rotación
        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()
