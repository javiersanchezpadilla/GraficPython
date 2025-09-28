""" En este ejercicio ahora dibujaremos trazos mediant el uso de puntos.
    Las coordenadas están normalizadas: X e Y van de -1 a 1.
    Sera necesario usar funciones matematicas como cos() y sin() para dibujar un circulo.

    Tambien usaremos la pendiente m y la interseccion b para dibujar lineas.
    La ecuacion de la recta es: y = m*x + b
    donde m = (y2 - y1) / (x2 - x1)  y   b = y1 - m*x1
    
    La ecuacion del circulo es: (x - xc)^2 + (y - yc)^2 = r^2
    donde (xc, yc) son las coordenadas del centro y r es el radio.

    Para dibujar las lineas y el circulo usaremos puntos muy cercanos entre si.
    Con este ejemplo se podrá entender que la ejecución de un programa en OpenGL
    es un ciclo infinito, donde se dibuja, se actualiza la ventana y se procesan los eventos.
    """

import glfw
from OpenGL.GL import *
from math import cos, sin


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


def dibuja_punto(x, y):
    """ Dibuja un punto en las coordenadas (x, y) con el tamaño especificado.
        :param x: Coordenada X del punto (de -1 a 1)
        :param y: Coordenada Y del punto (de -1 a 1)
    """
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def dibuja_linea(x1, y1, x2, y2, step=0.01):
    """ Dibuja una línea entre los puntos (x1, y1) y (x2, y2) usando puntos.
        :param x1: Coordenada X del primer punto (de -1 a 1)
        :param y1: Coordenada Y del primer punto (de -1 a 1)
        :param x2: Coordenada X del segundo punto (de -1 a 1)
        :param y2: Coordenada Y del segundo punto (de -1 a 1)
        :param step: Incremento para interpolar los puntos en la línea
    """
    if x1 == x2:                            # Línea vertical
        if y1 > y2:
            y1, y2 = y2, y1
        y = y1
        while y <= y2:
            dibuja_punto(x1, y)
            y += step
    else:
        m = (y2 - y1) / (x2 - x1)           # Pendiente
        b = y1 - m * x1                     # Intersección con Y
        if x1 > x2:
            x1, x2 = x2, x1
        x = x1
        while x <= x2:
            y = m * x + b
            dibuja_punto(x, y)
            x += step

def dibuja_circulo(xc, yc, r, step=0.01):
    """ Dibuja un círculo centrado en (xc, yc) con radio r usando puntos.
        :param xc: Coordenada X del centro del círculo (de -1 a 1)
        :param yc: Coordenada Y del centro del círculo (de -1 a 1)
        :param r: Radio del círculo
        :param step: Incremento para interpolar los puntos en el círculo
    """
    theta = 0.0
    while theta <= 2 * 3.14159:
        x = xc + r * cos(theta)
        y = yc + r * sin(theta)
        dibuja_punto(x, y)
        theta += step


def dibuja_trazos():
    """ Dibuja trazos a lo largo del eje X y Y. """
    glColor3f(1, 0, 0)                      # Color rojo
    dibuja_linea(-0.9, -0.5, 0.9, 0.5)      # Línea diagonal
    glColor3f(0, 1, 0)                      # Color verde
    dibuja_linea(-0.5, -0.9, 0.5, 0.9)      # Línea diagonal
    glColor3f(0, 0, 1)                      # Color azul
    dibuja_linea(-0.9, 0.0, 0.9, 0.0)       # Línea horizontal
    glColor3f(1, 1, 0)                      # Color amarillo
    dibuja_linea(0.0, -0.9, 0.0, 0.9)       # Línea vertical
    
    glColor3f(1, 0, 1)                      # Color magenta
    dibuja_circulo(0.0, 0.0, 0.5)            # Círculo centrado en el origen    



if __name__ == "__main__":
    ventana = iniciar_ventana()
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        dibuja_trazos()         
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
