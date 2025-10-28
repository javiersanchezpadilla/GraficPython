""" En este ejercicio se dibujaran dos cuadros que se moveran horizontalmente en direcciones opuestas.
    Cuando los cuadros colisionen entre si, rebotaran y cambiaran de direccion.
    Cada cuadro estara formado por cuatro vertices y tendra un color diferente.
"""

import glfw
from OpenGL.GL import *

# Definición de los cuadros con sus atributos en un diccionario
cuadro1 = {
    'pos_x': -0.9,
    'velocidad': 0.06,
    'tamanio': 0.2,
    'color_r': 1.0,
    'color_g': 0.0,
    'color_b': 0.0
}

cuadro2 = {
    'pos_x': 0.7,
    'velocidad': -0.01,
    'tamanio': 0.2,
    'color_r': 0.0,
    'color_g': 0.0,
    'color_b': 1.0
}


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


def dibujar_cuadro(cuadro):
    #Dibuja un cuadrado usando sus atributos.
    glBegin(GL_QUADS)
    glColor3f(cuadro['color_r'], cuadro['color_g'], cuadro['color_b'])
    
    x = cuadro['pos_x']
    tam = cuadro['tamanio']
    
    glVertex2f(x, tam)
    glVertex2f(x + tam, tam)
    glVertex2f(x + tam, -tam)
    glVertex2f(x, -tam)
    glEnd()


def actualizar_posicion(cuadro):
    # Actualiza la posición del cuadro y lo hace rebotar en los bordes de la pantalla.
    cuadro['pos_x'] += cuadro['velocidad']
    
    if cuadro['pos_x'] + cuadro['tamanio'] >= 1.0 or cuadro['pos_x'] <= -1.0:
        cuadro['velocidad'] *= -1

def detectar_colision():
    # Detecta si los dos cuadros están colisionando.
    # Verificamos si los cuadros se están tocando o superponiendo
    # La colisión ocurre cuando el borde de uno se cruza con el del otro
    colision = False
    
    # Colisión por la derecha del cuadro 1
    if cuadro1['pos_x'] + cuadro1['tamanio'] >= cuadro2['pos_x'] and cuadro1['pos_x'] < cuadro2['pos_x']:
        colision = True
        
    # Colisión por la izquierda del cuadro 1
    if cuadro1['pos_x'] <= cuadro2['pos_x'] + cuadro2['tamanio'] and cuadro1['pos_x'] > cuadro2['pos_x']:
        colision = True
        
    return colision


def programa_principal():
    ventana = iniciar_ventana()
    
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # 1. Actualizar la posición de cada cuadro
        actualizar_posicion(cuadro1)
        actualizar_posicion(cuadro2)
        
        # 2. Detectar colisión entre ellos
        if detectar_colision():
            cuadro1['velocidad'] *= -1
            cuadro2['velocidad'] *= -1

        # 3. Dibujar ambos cuadros
        dibujar_cuadro(cuadro1)
        dibujar_cuadro(cuadro2)
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()


if __name__ == "__main__":
    programa_principal()

