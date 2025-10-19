""" El objetivo de este programa es mostrar cómo controlar el ratón utilizando la biblioteca GLFW en Python.
    Al igual que con el teclado, la forma de detectar e identificar las acciones del ratón es a través de funciones callback 
    (llamadas de retorno) que GLFW invoca cuando ocurren eventos relacionados con el ratón.
    
    la función de conversión de coordenadas es un punto donde muchos se confunden al principio. 
    No es intuitiva porque combina dos sistemas de coordenadas que funcionan de manera opuesta.
    La clave es entender que estás haciendo un mapeo de un rango a otro.

    def convertir_a_opengl(x_pix, y_pix, ancho, alto):
        # 1. Conversión de X: Mapea [0, ancho] a [-1.0, 1.0]
        x_norm = (x_pix / ancho) * 2.0 - 1.0
        
        # 2. Conversión de Y: Mapea [0, alto] a [-1.0, 1.0] E INVierte el eje
        y_norm = 1.0 - (y_pix / alto) * 2.0
        
        return x_norm, y_norm
    
        
    1. CONVERSIÓN DEL EJE 'X' (HORIZONTAL)

    El objetivo es mapear el rango de píxeles [0, ancho] al rango normalizado de OpenGL [-1.0, 1.0].
    
    Píxel (xpix)                Valor Normalizado (xnorm) 
    -----------------------------------------------------
    0 (Extremo Izquierdo)           -1.0
    ancho/2 (Centro)                 0.0
    ancho (Extremo Derecho)          1.0    

    La Lógica en Pasos:
    1. Normalización a [0, 1]:      Xpix / ancho
    Esto convierte la coordenada de píxel en un porcentaje de 0 a 1.
    Ej: 400 píxeles en una ventana de 800 de ancho se convierten en 400/800 = 0.5 
    
    2. Mapeo a [0, 2]:              ( Xpix / ancho ) 2.0 
    Multiplicar por 2.0 convierte el rango de [0, 1] a [0, 2].  Ej: 0.5 ⋅ 2.0 = 1.0.
    
    3. Mapeo a [-1, 1]:             (( Xpix / ancho) 2.0 ) - 1.0 ) 
    Restar 1.0 desplaza el rango de [0, 2] a [-1.0, 1.0]. 
    Ej: 1.0 - 1.0 = 0.0 (el centro).
    

    2. CONVERSIÓN DEL EJE 'y' (VERTICAL) E INVERSIÓN
    
    El objetivo es similar, pero con una inversión necesaria debido a la diferencia 
    en cómo se miden las coordenadas:
    
    Sistema                 Valor Alto (1.0)            Valor Bajo (-1.0)
    ------------------------------------------------------------------------
    Píxeles (Pantalla)      y_pix = 0 (Arriba)          y_pix = alto (Abajo)
    OpenGL (Clip)           y_norm = 1.0 (Arriba)       y_norm = -1.0 (Abajo)

    La Lógica en Pasos (Invertida):
    
    1. Mapeo a [0, 2] (Igual que X):        ( y_pix / alto ) 2.0
    Ej: Si y_pix =0 (Arriba), el resultado es 0.0. Si y_pix = alto (Abajo), el resultado es 2.0
    
    2. Inversión y Mapeo a [-1, 1]:         1.0 - ((y_pix / alto ) 2.0)
    Al restar el resultado del paso anterior de 1.0, logramos la inversión:
    
        Si el resultado es 0.0 (y_pix = 0, Arriba), entonces 1.0 - 0.0 = 1.0 (Arriba en OpenGL)
        Si el resultado es 2.0 (y_pix = alto, Abajo), entonces 1.0 - 2.0 = -1.0 (Abajo en OpenGL).
        
    Esta fórmula garantiza que el punto superior izquierdo de tu ventana de píxeles (0, 0) 
    se mapee al punto superior izquierdo de OpenGL (-1.0, 1.0), manteniendo la consistencia de 
    tu aplicación gráfica.
"""

import glfw
from OpenGL.GL import *
import math
import random

# Variables globales para el estado del ratón y el color
cursor_x_pixeles = 400  # Posición inicial en el centro de la ventana (píxeles)
cursor_y_pixeles = 300
color_r, color_g, color_b = 1.0, 0.0, 0.0  # Rojo inicial
ventana_ancho = 800
ventana_alto = 600


def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(ventana_ancho, ventana_alto, "Control de Ratón con GLFW", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


# 1. Callback para el movimiento del cursor
def cursor_pos_callback(window, xpos, ypos):
    global cursor_x_pixeles, cursor_y_pixeles
    # Almacenamos la posición en píxeles
    cursor_x_pixeles = xpos
    cursor_y_pixeles = ypos


# 2. Callback para los clics del ratón
def mouse_button_callback(window, button, action, mods):
    global color_r, color_g, color_b
    
    # Si se presiona el botón izquierdo, cambiamos el color a uno aleatorio
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        color_r = random.random()
        color_g = random.random()
        color_b = random.random()


def dibujar_circulo(x_norm, y_norm, radio):
    """ Dibuja un círculo usando la ecuación paramétrica.
        Las coordenadas deben estar en el rango de OpenGL (-1 a 1).
    """
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(color_r, color_g, color_b)
    
    # Centro del círculo
    glVertex2f(x_norm, y_norm)
    
    # Dibuja la circunferencia
    for i in range(36): # 36 puntos para una circunferencia decente
        angulo = 2.0 * math.pi * i / 36
        x = x_norm + radio * math.cos(angulo)
        y = y_norm + radio * math.sin(angulo)
        glVertex2f(x, y)
        
    glEnd()


# Función para convertir coordenadas de píxeles a coordenadas de OpenGL (-1.0 a 1.0)
# Esta función es crucial. Convierte las coordenadas del sistema de píxeles 
# (donde y=0 es la parte superior) al sistema de coordenadas de OpenGL 
# (donde y=1 es la parte superior, y el rango es -1 a 1).
# La clave es entender que estás haciendo un mapeo de un rango a otro.
def convertir_a_opengl(x_pix, y_pix, ancho, alto):
    # 1. Conversión de X: Mapea [0, ancho] a [-1.0, 1.0]
    x_norm = (x_pix / ancho) * 2.0 - 1.0
    
    # 2. Conversión de Y: Mapea [0, alto] a [-1.0, 1.0] E INVierte el eje
    y_norm = 1.0 - (y_pix / alto) * 2.0
    
    return x_norm, y_norm



def main():
    ventana = iniciar_ventana()
    
    # --- Registro de Callbacks ---
    glfw.set_cursor_pos_callback(ventana, cursor_pos_callback)
    glfw.set_mouse_button_callback(ventana, mouse_button_callback)
    # -----------------------------
    
    while not glfw.window_should_close(ventana):
        glClearColor(0.1, 0.1, 0.1, 1.0) # Fondo gris oscuro
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Convertimos la posición actual del cursor (en píxeles) a la posición de OpenGL
        x_opengl, y_opengl = convertir_a_opengl(cursor_x_pixeles, cursor_y_pixeles, ventana_ancho, ventana_alto)
        
        # Dibujamos el círculo en la posición del cursor
        dibujar_circulo(x_opengl, y_opengl, 0.1)
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
    