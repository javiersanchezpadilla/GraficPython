""" Aplicación de la rotación sobre un cuadrado

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



def rotar_vertices(x, y, p_x, p_y, angulo_grados):
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



def dibuja_cuadrado(vertice):
    """
    Dibuja un punto en las coordenadas (x, y).
    """
    glBegin(GL_QUADS)
    glVertex2f(vertice[0], vertice[1])
    glVertex2f(vertice[2], vertice[3])
    glVertex2f(vertice[4], vertice[5])
    glVertex2f(vertice[6], vertice[7])
    glEnd()



def dibuja(pivote, vertices, angulo_en_grados):
    """
    Rota un punto (x, y) alrededor de un pivote (p_x, p_y) por un ángulo.
    """
    glClearColor(0.0, 0.0, 0.0, 1.0)    # Limpia la pantalla
    glClear(GL_COLOR_BUFFER_BIT)       # Si quitamos esta linea, veremos el rastro del punto
    glColor3f(0.0, 1.0, 1.0)            # Color amarillo brillante

    # Primero dibuja los vertices originales del cuadro
    dibuja_cuadrado(vertices)

    # Luego rota cada vertice y actualiza sus coordenadas para la siguiente iteración
    vertices[0], vertices[1] = rotar_vertices(vertices[0], vertices[1], pivote[0], pivote[1], angulo_en_grados)
    vertices[2], vertices[3] = rotar_vertices(vertices[2], vertices[3], pivote[0], pivote[1], angulo_en_grados)
    vertices[4], vertices[5] = rotar_vertices(vertices[4], vertices[5], pivote[0], pivote[1], angulo_en_grados)
    vertices[6], vertices[7] = rotar_vertices(vertices[6], vertices[7], pivote[0], pivote[1], angulo_en_grados)

   

if __name__ == "__main__":
    ventana = iniciar_ventana()
    # si queremos que rota en sentido inverso, cambiar el signo del angulo
    angulo_en_grados = 2.0
    pivote = (0.0, 0.0)
    vertices = [-0.5, 0.5, 0.5, 0.5, 0.5, -0.5, -0.5, -0.5]

    while not glfw.window_should_close(ventana):
        dibuja(pivote, vertices, angulo_en_grados)
        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()
