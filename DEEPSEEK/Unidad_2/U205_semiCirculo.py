""" Dibujaremos un semicírculo con OpenGL
    Usaremos GL_TRIANGLE_FAN para crear un semicírculo.

    Explicación de las partes clave:
1. Configuración de GLFW:

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)

    Define la versión de OpenGL a usar (2.0 en este caso, buena para compatibilidad).

2. Sistema de coordenadas:

    glOrtho(-2, 2, -1.5, 1.5, -1, 1)
    Establece un sistema de coordenadas donde:

    X va desde -2 (izquierda) hasta 2 (derecha)
    Y va desde -1.5 (abajo) hasta 1.5 (arriba)

    3. Función dibujar_semicirculo:
    angulo_apertura: Puedes cambiar de 180° (medio círculo) a cualquier valor:

90 = cuarto de círculo
270 = tres cuartos
-180 = semicírculo invertido
"""

import math
import glfw
from OpenGL.GL import *

def dibujar_semicirculo(x, y, radio, segmentos=50, angulo_apertura=180):
    """
    Dibuja un semicírculo usando GL_TRIANGLE_FAN
    x, y: Centro del semicírculo
    radio: Radio del semicírculo
    segmentos: Número de triángulos para suavizar la forma
    angulo_apertura: Ángulo de apertura en grados (180 = medio círculo)
    """
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.8, 1.0)  # Color azul claro
    glVertex2f(x, y)  # Centro del semicírculo
    
    # Convertir el ángulo de apertura a radianes
    angulo_apertura_rad = math.radians(angulo_apertura)
    
    for i in range(segmentos + 1):
        # Calcular el ángulo actual (desde 0 hasta angulo_apertura)
        fraccion = i / segmentos
        angulo = fraccion * angulo_apertura_rad
        
        # Calcular las coordenadas del punto en el borde
        x_borde = x + math.cos(angulo) * radio
        y_borde = y + math.sin(angulo) * radio
        
        glVertex2f(x_borde, y_borde)
    glEnd()

def main():
    # Inicializar GLFW
    if not glfw.init():
        print("Error al inicializar GLFW")
        return -1
    
    # Configurar versión de OpenGL (puedes usar versiones más modernas)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
    
    # Crear ventana
    window = glfw.create_window(800, 600, "Semicírculo en OpenGL", None, None)
    if not window:
        print("Error al crear la ventana")
        glfw.terminate()
        return -1
    
    # Hacer la ventana el contexto actual
    glfw.make_context_current(window)
    
    # Configurar el viewport (área de dibujo)
    glViewport(0, 0, 800, 600)
    
    # Configurar proyección ortográfica 2D
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-4, 4, -3, 3, -1, 1)  # Coordenadas: left, right, bottom, top
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Bucle principal de renderizado
    while not glfw.window_should_close(window):
        # Limpiar el buffer de color
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Dibujar un semicírculo en el centro de la pantalla
        dibujar_semicirculo(0.0, 0.0, 0.8, 50, 180)  # Radio 0.8, 180° de apertura
        
        # Dibujar otro semicírculo más pequeño a la derecha (90°)
        dibujar_semicirculo(1.5, 0.0, 0.4, 30, 90)   # Cuarto de círculo
        
        # Dibujar semicírculo invertido a la izquierda
        glColor3f(1.0, 0.5, 0.0)  # Cambiar color a naranja
        dibujar_semicirculo(-1.5, 0.0, 0.6, 40, -180)  # Hacia abajo

        # Prueba diferentes ángulos:
        # dibujar_semicirculo(0, 0, 0.8, 50, 270)  # Tres cuartos de círculo
        # dibujar_semicirculo(0, 0, 0.8, 50, 360)  # Círculo completo
        # dibujar_semicirculo(0, 0, 0.8, 50, 45)   # Octavo de círculo

        # Más segmentos = más suave (pero más pesado)
        # dibujar_semicirculo(0, 0, 0.8, 100, 180)  # Muy suave
        
        # Intercambiar buffers y procesar eventos
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    # Limpiar y terminar
    glfw.terminate()
    return 0

if __name__ == "__main__":
    main()