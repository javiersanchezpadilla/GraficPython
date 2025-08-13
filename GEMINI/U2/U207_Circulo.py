""" En este ejercicio, vamos a dibujar un circulo mediante GL_TRIANGLE_FAN

    1. GL_TRIANGLE_FAN. Qué hace: Es un modo de dibujo que conecta todos los 
       vértices alrededor de un punto central formando triángulos.

    Visualización:

    El primer vértice (el centro) se conecta con cada par de vértices siguientes 
    para crear triángulos.

    Ejemplo con 4 segmentos:

    Centro -> V1 -> V2  (Triángulo 1)
    Centro -> V2 -> V3  (Triángulo 2)
    ...

    2. glColor3f(1.0, 1.0, 0.0). Define el color del círculo en RGB.

    3. glVertex2f(x, y). Es el centro del círculo. Todos los triángulos partirán 
       de aquí.

    4. Bucle for i in range(segmentos + 1). segmentos: Número de divisiones del 
       círculo (más segmentos = círculo más suave).

       + 1: Para cerrar el círculo (el último vértice se conecta con el primero).

    5. Cálculo del Ángulo (angulo = 2 * math.pi * i / segmentos)
            2 * math.pi: Un círculo completo en radianes (360°).
            i / segmentos: Fracción del círculo que corresponde al vértice actual.

    Ejemplo: Si segmentos = 4, los ángulos serán: 0°, 90°, 180°, 270°, 360°(0°).

    6. y 7. Coordenadas del Borde (math.cos(angulo) * radio, math.sin(angulo) * radio)
            math.cos(angulo) * radio: Calcula la posición X en el borde del círculo.
            math.sin(angulo) * radio: Calcula la posición Y en el borde del círculo.

    Fórmula:

    x_borde = x_centro + cos(ángulo) * radio
    y_borde = y_centro + sin(ángulo) * radio

    8. glEnd(). Finaliza el dibujo y OpenGL renderiza todos los triángulos juntos.

    ¿Por qué funciona?
    GL_TRIANGLE_FAN crea una "rueda de triángulos" desde el centro hasta el borde.
    Cada iteración del bucle añade un vértice en el borde del círculo, formando un 
    nuevo triángulo con el centro y el vértice anterior. Al unir todos los triángulos, 
    obtienes un círculo (mas bien un poligono de muchos lados que se asemeja a un círculo).

    Ejemplo Visual (Con 8 Segmentos):
    
        Centro (x, y)
       *
      /|\
     / | \
    /  |  \
   *---*---*  <- Vértices en el borde. Cada triángulo comparte el centro y dos vértices 
   contiguos del borde.

    ¿Cómo mejorar el círculo? Aumenta segmentos para más suavidad (ej: segmentos=100).
    Usa shaders para efectos como gradientes o bordes antialiasing.
"""

import glfw
from OpenGL.GL import *
import math

def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Escena 2D con OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana

# Función para dibujar un círculo usando GL_TRIANGLE_FAN
def dibujar_circulo(x, y, radio, r, g, b, segmentos=50):
    glBegin(GL_TRIANGLE_FAN)                    # Inicia el modo de dibujo
    glColor3f(r, g, b)                          # Establece el color del círculo       
    glVertex2f(x, y)                            # Centro del círculo
    for i in range(segmentos + 1):              # Bucle para los vertices del círculo
        angulo = 2 * math.pi * i / segmentos    # Calcula el ángulo para cada segmento
        glVertex2f(
            x + math.cos(angulo) * radio,       # Coordenanda x del borde
            y + math.sin(angulo) * radio        # Coordenanda y del borde
            )
    glEnd()


ventana = iniciar_ventana()

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.8, 0.9, 1.0, 1)  # Fondo celeste

    dibujar_circulo(0.7, 0.0, 0.25, 0.0, 0.6, 0.0)      # Círculo verde
    dibujar_circulo(0.75, 0.75, 0.15, 1.0, 1.0, 0.0)    # Círculo amarillo

    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()

