""" Aplicación de la rotación sobre dos puntos
    En este ejercicio no se actualiza el angulo de rotación, para lograr que los puntos roten indefinidamente
    lo que se cambia el punto original por el punto rotado en cada iteración del bucle principal,lo que 
    hace que se tenga que calcular de nuevo la rotación con base al mismo angulo inicial, pero sobre
    una nueva posición del punto (que es la calculada en la iteración anterior), esto es, tenemos (x, y)
    y se calcula (x', y') con el angulo inicial, luego en la siguiente iteración se toma (x', y') como
    el nuevo punto original (x, y) pero asignando (x=x', y=y') y se vuelve a calcular (x', y') 
    con el mismo angulo inicial, y así sucesivamente.
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

    return (x_final, y_final)



def dibuja_punto(x, y):
    """
    Dibuja un punto en las coordenadas (x, y).
    """
    glPointSize(5)  # Tamaño del punto
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def dibuja_ejes():
    """
    Dibuja los ejes coordenados.
    """
    glBegin(GL_LINES)                   # Dibuja los ejes
    glColor3f(1.0, 1.0, 1.0)            # Ejes en color blanco
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()


def dibuja(pivote, punto1, punto2, angulo_en_grados01, angulo_en_grados02):
    """
    Rota un punto (x, y) alrededor de un pivote (p_x, p_y) por un ángulo.
    """
    glClearColor(0.0, 0.0, 0.0, 1.0)    # Limpia la pantalla
    glClear(GL_COLOR_BUFFER_BIT)        # Si quitamos esta linea, veremos el rastro del punto
    glColor3f(1.0, 1.0, 0.0)            # Color amarillo brillante

    dibuja_ejes()
    punto_rotado1 = rotar_punto(punto1[0], punto1[1], pivote[0], pivote[1], angulo_en_grados01)
    dibuja_punto(punto_rotado1[0], punto_rotado1[1])
    punto_rotado2 = rotar_punto(punto2[0], punto2[1], pivote[0], pivote[1], angulo_en_grados02)
    dibuja_punto(punto_rotado2[0], punto_rotado2[1])

    return punto_rotado1, punto_rotado2

    

if __name__ == "__main__":
    ventana = iniciar_ventana()

    angulo_en_grados01 = 2.0
    angulo_en_grados02 = 0.5
    pivote = (0.0, 0.0)
    punto1 = (0.7, 0.7)
    punto2 = (0.5, 0.5)

    while not glfw.window_should_close(ventana):
        # aunque punto1 y punto2 son tuplas, al hacer la asignación
        # punto1 = punto_rotado1, se convierten en listas
        # para permitir la actualización de sus valores
        punto1, punto2 = dibuja(pivote, punto1, punto2, angulo_en_grados01, angulo_en_grados02)
        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()
