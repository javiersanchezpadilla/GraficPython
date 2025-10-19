""" En este ejercicio se dibujara un cuadro en el centro de la pantalla el cual se 
    movera mediante el uso de las flechas.
    El cuadro no podrá avanzar mas de los lados del limite de la pantalla.
    Dado que estamos utilizando la biblioteca GLFW, la forma de detectar e identificar 
    las teclas es a través de una función llamada callback de teclado.

    Los controles serán los siguientes:
    -------------------------------------------------------------------------------------------
    Flechas Arriba/Abajo/Izquierda/Derecha: Mover el cuadro en la dirección correspondiente.
    Tecla 'C': Centrar el cuadro en la posición inicial.
    Teclas 'F1', 'F2', 'F3': Cambiar el color del cuadro a rojo, verde o azul respectivamente.
    Tecla 'ESC': Cerrar la ventana y terminar el programa.  
"""

import glfw
from OpenGL.GL import *


valores_cuadro = {
    "pos_x": -0.1,      # Posición inicial en X
    "pos_y": 0.1,       # Posición inicial en Y
    "vel": 0.1,        # Velocidad de movimiento
    "tam": 0.2,         # Tamaño del cuadro
    "red":1.0,          # Color rojo
    "green":1.0,        # Color verde
    "blue":1.0 }        # Color azul



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



def key_callback(window, key, scancode, action, mods):

    global valores_cuadro
    posicion_x = valores_cuadro["pos_x"]
    posicion_y = valores_cuadro["pos_y"]
    velocidad = valores_cuadro["vel"]
    tamanio = valores_cuadro["tam"]
    
    if action == glfw.PRESS or action == glfw.REPEAT:
        
        # Moviendo el cuadro hacia arriba y abajo
        if key == glfw.KEY_UP or key == glfw.KEY_W:
            new_pos_y = posicion_y + velocidad
            if new_pos_y <= 1.0:
                posicion_y += velocidad
        elif key == glfw.KEY_DOWN or key == glfw.KEY_S:
            new_pos_y = posicion_y - tamanio - velocidad
            if new_pos_y >= -1.0:
                posicion_y -= velocidad
            
        # MOVIMIENTO HORIZONTAL
        elif key == glfw.KEY_LEFT or key == glfw.KEY_A:
            new_pos_x = posicion_x - velocidad
            if new_pos_x >= -1.0:
                posicion_x -= velocidad
        elif key == glfw.KEY_RIGHT or key == glfw.KEY_D:
            new_pos_x = posicion_x + tamanio + velocidad
            if new_pos_x <= 1.0:
                posicion_x += velocidad

        # CENTRAMOS EL CUADRO 
        elif key == glfw.KEY_C:
            posicion_x = -0.1
            posicion_y = 0.1   

        # CAMBIAMOS EL CUADRO A COLOR ROJO
        elif key == glfw.KEY_F1:
            valores_cuadro["red"] = 1.0
            valores_cuadro["green"] = 0.0
            valores_cuadro["blue"] = 0.0 
            
        # CAMBIAMOS EL CUADRO A COLOR VERDE
        elif key == glfw.KEY_F2:
            valores_cuadro["red"] = 0.0
            valores_cuadro["green"] = 1.0
            valores_cuadro["blue"] = 0.0 

        # CAMBIAMOS EL CUADRO A COLOR AZUL
        elif key == glfw.KEY_F3:
            valores_cuadro["red"] = 0.0
            valores_cuadro["green"] = 0.0
            valores_cuadro["blue"] = 1.0 


        # CONTROL DE VENTANA
        elif key == glfw.KEY_ESCAPE:
            # Cierra la ventana cuando se presiona ESC
            glfw.set_window_should_close(window, True)

    valores_cuadro["pos_x"] = posicion_x
    valores_cuadro["pos_y"] = posicion_y

    print(f"Posición X: {valores_cuadro['pos_x']}, Posición Y: {valores_cuadro['pos_y']}")




def dibujar_cuadro(cuadro):
    """
    La funcion `dibujar_cuadro` dibuja un cuadro en la posicion x, y con un tamanio y color especifico.
    :param cuadro: Un diccionario que contiene las propiedades del cuadro a dibujar, incluyendo
                   su posicion en x e y, tamanio y color (rojo, verde, azul).
    """
    # Dibuja los ejes de coordenadas
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_LINES)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()

    x = cuadro["pos_x"]
    y = cuadro["pos_y"]
    tam = cuadro["tam"]
    rojo = cuadro["red"]
    verde = cuadro["green"]
    azul = cuadro["blue"]

    #Dibuja un cuadrado en la posición x, y.
    glColor3f(rojo, verde, azul)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + tam, y)
    glVertex2f(x + tam, y - tam)
    glVertex2f(x, y - tam)
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
        dibujar_cuadro(valores_cuadro)
        
        # Intercambiar búferes para mostrar el resultado
        glfw.swap_buffers(ventana)
        
        # Procesar eventos (clics, etc.)
        glfw.poll_events()
    
    glfw.terminate()



# LLamado al programa principal de control
if __name__ == "__main__":
    programa_principal()
