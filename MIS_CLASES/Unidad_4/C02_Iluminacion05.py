""" Ejemplo usando todas las fuentes de luz.

"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *       # importamos las librerias de glut (no olvidar inicializar glutInit())
import math

def configurar_8_luces():
    """Configura las 8 luces disponibles en OpenGL"""
    
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    
    # Lista de colores para las 8 luces
    colores_luces = [
        [1.0, 1.0, 1.0, 1.0],  # LIGHT0 - Blanco
        [1.0, 0.0, 0.0, 1.0],  # LIGHT1 - Rojo
        [0.0, 1.0, 0.0, 1.0],  # LIGHT2 - Verde
        [0.0, 0.0, 1.0, 1.0],  # LIGHT3 - Azul
        [1.0, 1.0, 0.0, 1.0],  # LIGHT4 - Amarillo
        [1.0, 0.0, 1.0, 1.0],  # LIGHT5 - Magenta
        [0.0, 1.0, 1.0, 1.0],  # LIGHT6 - Cian
        [0.5, 0.5, 0.5, 1.0],  # LIGHT7 - Gris
    ]
    
    # Posiciones en un círculo
    radio = 5.0
    altura = 3.0
    
                                # Activamos las luces desde GL_LIGHT0, GL_LIGHT1, GL_LIGHT2, ... , GL_LIGHT7
    for i in range(8):
        luz_id = GL_LIGHT0 + i
        glEnable(luz_id)
        
        # Calcular posición en círculo
        angulo = (i / 8.0) * 2 * math.pi
        x = math.cos(angulo) * radio
        z = math.sin(angulo) * radio
        
        # Configurar posición
        glLightfv(luz_id, GL_POSITION, [x, altura, z, 1.0])
        
        # Configurar color
        glLightfv(luz_id, GL_DIFFUSE, colores_luces[i])
        glLightfv(luz_id, GL_SPECULAR, colores_luces[i])
        
        # Atenuación diferente para cada luz
        atenuacion = 0.5 + (i * 0.1)
        glLightf(luz_id, GL_CONSTANT_ATTENUATION, atenuacion)

# Uso mínimo para probar
if not glfw.init():
    exit()

ventana = glfw.create_window(800, 600, "8 Luces OpenGL", None, None)
glfw.make_context_current(ventana)


                        # ***********************************************************************
glutInit()              # Activamos GLUT                                                    *****
                        # recordar que el caso de windows tienen que crear una ventanita    *****
                        # glutCreateWindow(b"La ventanita")
                        # ***********************************************************************




configurar_8_luces()

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 100.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 10, 10, 0, 0, 0, 0, 1, 0)
    
    # Dibujar esfera para ver efecto combinado
    glutSolidSphere(2, 32, 32)
    
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()