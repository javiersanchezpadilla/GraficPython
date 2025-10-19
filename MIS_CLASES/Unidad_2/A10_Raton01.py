""" Detección de Ratón 
    controlar el ratón con GLFW sigue una lógica similar, utilizando también el concepto de 
    callbacks (llamadas de retorno).

    Hay tres formas principales de capturar la interacción del ratón:

    1. DETECCIÓN DE BOTONES DEL RATÓN (Clics)
    Para saber cuándo se presiona o suelta un botón del ratón (clic), se usa la función 

        glfw.set_mouse_button_callback().

    Identificación de botones del ratón

    Botón               Constante GLFW
    -----------------------------------------
    Izquierdo       glfw.MOUSE_BUTTON_LEFT
    Derecho         glfw.MOUSE_BUTTON_RIGHT
    Medio (Rueda)   glfw.MOUSE_BUTTON_MIDDLE


    2. DETECCIÓN DE MOVIMIENTO DEL RATÓN
    Para saber dónde está el ratón en la ventana, se usa la función 
    
        glfw.set_cursor_pos_callback(). 
        
    Esta es esencial para arrastrar objetos o para una vista de cámara en 3D.

    3. DETECCIÓN DE LA RUEDA DE DESPLAZAMIENTO (Scroll)
    Para detectar el movimiento de la rueda del ratón (scroll), se usa la función 
    
        glfw.set_scroll_callback().

    Esta estructura te permite gestionar la interacción completa del ratón de forma 
    eficiente y no invasiva para el bucle principal
"""

import glfw
from OpenGL.GL import *

# Estas variables globales almacenan la posición del cursor
cursor_x = 0
cursor_y = 0


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


# **************************************************
# ***   DETECCIÓN DE BOTONES DEL RATÓN (Clics)   ***
# **************************************************

# Esta función recibe el código del botón (button), 
# la acción (action) y los modificadores (mods).

def mouse_button_callback(window, button, action, mods):
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        print("¡Clic izquierdo presionado!")
    elif button == glfw.MOUSE_BUTTON_LEFT and action == glfw.RELEASE:
        print("¡Clic izquierdo soltado!")
    elif button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.PRESS:
        print("¡Clic derecho presionado!")
    elif button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.RELEASE:
        print("¡Clic derecho soltado!")


# Esta función recibe la posición actual del cursor como coordenadas 'x' y 'y' 
# de la pantalla (en píxeles, no en coordenadas OpenGL de -1 a 1).
# Se requieren dos variables globales para almacenar la posición del cursor
# cursor_x = 0
# cursor_y = 0

def cursor_pos_callback(window, xpos, ypos):
    global cursor_x, cursor_y
    cursor_x = xpos
    cursor_y = ypos
    print(f"Cursor en: ({cursor_x}, {cursor_y})")
    # OJO: Si usas la posición del cursor (cursor_x, cursor_y) en el dibujo, 
    # debes convertir esos píxeles a coordenadas de OpenGL (-1.0 a 1.0).


# Esta función te da el desplazamiento horizontal (xoffset) y vertical (yoffset). 
# El yoffset es típicamente usado para hacer zoom in/out o cambiar de arma.

def scroll_callback(window, xoffset, yoffset):
    if yoffset > 0:
        print("Scroll hacia ARRIBA (Zoom In)")
    elif yoffset < 0:
        print("Scroll hacia ABAJO (Zoom Out)")


# 1. DETECCIÓN DE TECLAS
def key_callback(window, key, scancode, action, mods):
    
    # Solo procesamos eventos cuando la tecla es PRESIONADA o REPETIDA
    if action == glfw.PRESS or action == glfw.REPEAT:
        # 1. Identificación de Teclas
        if key == glfw.KEY_UP:
            print("Flecha Arriba presionada")
        elif key == glfw.KEY_DOWN:
            print("Flecha Abajo presionada")
        elif key == glfw.KEY_LEFT:
            print("Flecha Izquierda presionada")
        elif key == glfw.KEY_RIGHT:
            print("Flecha Derecha presionada")
        elif key == glfw.KEY_ESCAPE:
            print("Escape presionado - Cerrando ventana")
            glfw.set_window_should_close(window, True)



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
    ventana = iniciar_ventana()

    # ***************************
    # * Registro del CallbackS  *
    # ***************************

    # 1. Registrar para Teclado
    glfw.set_key_callback(ventana, key_callback)

    # 2. Registrar para Clics
    glfw.set_mouse_button_callback(ventana, mouse_button_callback)
    
    # 3. Registrar para Movimiento
    glfw.set_cursor_pos_callback(ventana, cursor_pos_callback)
    
    # 4. Registrar para Scroll
    glfw.set_scroll_callback(ventana, scroll_callback)
    

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
