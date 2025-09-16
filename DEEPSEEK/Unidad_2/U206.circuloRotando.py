""" Semicirculos rotando con OpenGL y GLUT en Python 

    Características de la animación:
    1.  Rotación Continua (Semicírculo Izquierdo)
        Rota 90 grados por segundo continuamente

        (tiempo_actual * 90) % 360 asegura que siempre esté entre 0° y 360°

    2. Oscilación (Semicírculo Central)
        Usa la función math.sin() para crear movimiento de vaivén
        Oscila entre -45° y 45° con un periodo de π segundos

    3. Degradado de Color (Semicírculo Derecho)
        Los colores cambian gradualmente de azul → púrpura → rojo
        intensidad = fraccion controla la transición de color

    Rota 180 grados por segundo

    CAMBIAR LAS VELOCIDADES DE ROTACIÓN:
    # Rotación más lenta (45°/segundo)
    rotacion1 = (tiempo_actual * 45) % 360

    # Rotación más rápida (360°/segundo)
    rotacion1 = (tiempo_actual * 360) % 360

    Diferentes degradados de color:
    python
    # Degradado verde-amarillo
    glColor3f(intensidad, 1.0, 0.0)

    # Degradado arcoíris
    glColor3f(
        math.sin(intensidad * math.pi),       # R
        math.sin(intensidad * math.pi + 2),   # G  
        math.sin(intensidad * math.pi + 4)    # B
    )
    Cambiar ángulos de apertura:
    python
    # Medialuna (ángulo pequeño)
    dibujar_semicirculo_animado(0, 0, 1.0, 50, 60, rotacion, True)

    # Casi círculo completo
    dibujar_semicirculo_animado(0, 0, 1.0, 50, 320, rotacion, True)
"""

import math
import glfw
from OpenGL.GL import *
import time

def dibujar_semicirculo_animado(x, y, radio, segmentos=50, angulo_apertura=180, rotacion=0, color_degradado=False):
    """
    Dibuja un semicírculo con rotación y opción de degradado
    x, y: Centro del semicírculo
    radio: Radio
    segmentos: Número de triángulos
    angulo_apertura: Ángulo de apertura en grados
    rotacion: Ángulo de rotación en grados
    color_degradado: Si True, aplica degradado de color
    """
    glBegin(GL_TRIANGLE_FAN)
    
    # Convertir ángulos a radianes
    rotacion_rad = math.radians(rotacion)
    angulo_apertura_rad = math.radians(angulo_apertura)
    
    # Centro (siempre blanco)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x, y)
    
    for i in range(segmentos + 1):
        # Calcular ángulo con rotación
        fraccion = i / segmentos
        angulo = rotacion_rad + fraccion * angulo_apertura_rad
        
        # Aplicar degradado de color si está activado
        if color_degradado:
            # Degradado de azul a rojo según la posición angular
            intensidad = fraccion  # 0.0 a 1.0
            glColor3f(intensidad, 0.5, 1.0 - intensidad)
        else:
            # Color fijo azul
            glColor3f(0.0, 0.8, 1.0)
        
        # Calcular coordenadas del borde
        x_borde = x + math.cos(angulo) * radio
        y_borde = y + math.sin(angulo) * radio
        
        glVertex2f(x_borde, y_borde)
    glEnd()

def main():
    # Inicializar GLFW
    if not glfw.init():
        print("Error al inicializar GLFW")
        return -1
    
    # Configurar ventana
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
    
    window = glfw.create_window(1000, 800, "Semicírculos Animados", None, None)
    if not window:
        print("Error al crear la ventana")
        glfw.terminate()
        return -1
    
    glfw.make_context_current(window)
    glViewport(0, 0, 1000, 800)
    
    # Configurar proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3, 3, -2, 2, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Variables para la animación
    tiempo_inicio = time.time()
    
    # Bucle principal
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Calcular tiempo transcurrido para animaciones
        tiempo_actual = time.time() - tiempo_inicio
        
        # Semicírculo 1: Rotación continua (360° cada 4 segundos)
        rotacion1 = (tiempo_actual * 90) % 360  # 90°/segundo
        
        # Semicírculo 2: Oscilación (va y viene)
        rotacion2 = math.sin(tiempo_actual * 2) * 45  # Oscila entre -45° y 45°
        
        # Semicírculo 3: Rotación rápida con degradado
        rotacion3 = tiempo_actual * 180 % 360  # 180°/segundo
        
        # Dibujar los tres semicírculos
        
        # 1. Semicírculo con rotación continua (izquierda)
        dibujar_semicirculo_animado(-2.0, 0.5, 0.7, 60, 180, rotacion1, False)
        
        # 2. Semicírculo oscilante (centro)
        dibujar_semicirculo_animado(0.0, -0.5, 0.8, 40, 220, rotacion2, False)
        
        # 3. Semicírculo con degradado y rotación rápida (derecha)
        dibujar_semicirculo_animado(2.0, 0.0, 0.9, 80, 270, rotacion3, True)
        
        # Dibujar información en texto (coordenadas simples)
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        # Ejes coordenados
        glVertex2f(-3, 0); glVertex2f(3, 0)  # Eje X
        glVertex2f(0, -2); glVertex2f(0, 2)  # Eje Y
        glEnd()
        
        # Actualizar y procesar eventos
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()
    return 0

if __name__ == "__main__":
    main()
