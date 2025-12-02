""" Stack Overflow
    OpenGL permite hasta 8 fuentes de luz simultáneas (de GL_LIGHT0 a GL_LIGHT7)
    En este ejemplo se habilitaran tres fuentes de luz


    Casos de Uso Comunes para el manejo de mas luces:
    -------------------------------------------------
    ESCENARIO DE VIDEOJUEGO:
        glEnable(GL_LIGHT0)  # Sol/luz ambiente
        glEnable(GL_LIGHT1)  # Linterna del jugador (foco)
        glEnable(GL_LIGHT2)  # Lámparas estáticas
        glEnable(GL_LIGHT3)  # Efectos especiales (explosiones, etc.)

    ESCENA DE INTERIOR:
        glEnable(GL_LIGHT0)  # Luz general del techo
        glEnable(GL_LIGHT1)  # Lámpara de mesa
        glEnable(GL_LIGHT2)  # Pantalla de computadora
        glEnable(GL_LIGHT3)  # Luz de ventana

    EFECTOS ESPECIALES:
        glEnable(GL_LIGHT0)  # Luz base
        glEnable(GL_LIGHT1)  # Luz roja intermitente (alarma)
        glEnable(GL_LIGHT2)  # Luz azul (neón)
        glEnable(GL_LIGHT3)  # Luz verde (radioactivo)

"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *       # importamos las librerias de glut (no olvidar inicializar glutInit())
import math
import time

def configurar_multiples_luces():
    """Configura 3 luces diferentes en la escena"""
    
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)
    
    # ========== LUZ 0 (BLANCA - Sol/ambiente) ==========
    glEnable(GL_LIGHT0)
    
    # Luz direccional (como el sol)
    glLightfv(GL_LIGHT0, GL_POSITION, [0.5, 1.0, 0.3, 0.0])  # w=0.0 = direccional
    
    # Color AMBIENTE suave
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    
    # Color DIFUSO blanco cálido
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.9, 0.9, 0.8, 1.0])
    
    # Color ESPECULAR para brillos
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    
    # ========== LUZ 1 (ROJA - Foco posicional) ==========
    glEnable(GL_LIGHT1)
    
    # Luz posicional roja (como una lámpara)
    glLightfv(GL_LIGHT1, GL_POSITION, [-3.0, 2.0, 0.0, 1.0])  # w=1.0 = posicional
    
    # Color rojo puro
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1.0, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [1.0, 0.3, 0.3, 1.0])
    
    # Atenuación (se debilita con distancia)
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 1.0)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.1)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, 0.01)
    
    # ========== LUZ 2 (AZUL - Foco con dirección) ==========
    glEnable(GL_LIGHT2)
    
    # Luz azul tipo foco/reflector
    glLightfv(GL_LIGHT2, GL_POSITION, [3.0, 2.0, 0.0, 1.0])
    
    # Color azul
    glLightfv(GL_LIGHT2, GL_DIFFUSE, [0.2, 0.2, 1.0, 1.0])
    glLightfv(GL_LIGHT2, GL_SPECULAR, [0.3, 0.3, 1.0, 1.0])
    
    # Configurar como FOCO DIRECCIONAL
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, [0.0, -1.0, 0.0])  # Apunta hacia abajo
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 30.0)  # Ángulo de 30 grados
    glLightf(GL_LIGHT2, GL_SPOT_EXPONENT, 2.0)  # Intensidad dentro del cono

def dibujar_esfera_en(x, y, z, radio):
    """Dibuja una esfera en posición específica"""
    glPushMatrix()
    glTranslatef(x, y, z)
    glutSolidSphere(radio, 32, 32)
    glPopMatrix()

def dibujar_posicion_luz(numero, x, y, z, color):
    """Dibuja una esfera pequeña donde está la luz"""
    glDisable(GL_LIGHTING)
    glColor3f(color[0], color[1], color[2])
    glPushMatrix()
    glTranslatef(x, y, z)
    glutSolidSphere(0.15, 8, 8)
    glPopMatrix()
    glEnable(GL_LIGHTING)

# CONFIGURACIÓN PRINCIPAL
if not glfw.init():
    exit()

ventana = glfw.create_window(1000, 700, "8 LUCES en OpenGL - GL_LIGHT0 a GL_LIGHT7", None, None)
glfw.make_context_current(ventana)

                        # ***********************************************************************
glutInit()              # Activamos GLUT                                                    *****
                        # recordar que el caso de windows tienen que crear una ventanita    *****
                        # glutCreateWindow(b"La ventanita")
                        # ***********************************************************************




configurar_multiples_luces()
tiempo_inicio = time.time()

print("=== INFORMACIÓN ===")
print("OpenGL soporta hasta 8 luces: GL_LIGHT0 a GL_LIGHT7")
print("Cada luz tiene propiedades independientes")
print("==================")

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar perspectiva
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1000/700, 0.1, 100.0)
    
    # Configurar cámara
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 5, 10,  0, 0, 0,  0, 1, 0)
    
    # Mover luces con el tiempo
    tiempo = time.time() - tiempo_inicio
    
    # Luz 1 (roja) - Se mueve en círculo horizontal
    luz1_x = math.cos(tiempo) * 3
    luz1_z = math.sin(tiempo) * 3
    glLightfv(GL_LIGHT1, GL_POSITION, [luz1_x, 2.0, luz1_z, 1.0])
    
    # Luz 2 (azul) - Se mueve verticalmente
    luz2_y = 1.5 + math.sin(tiempo * 1.5) * 1.5
    glLightfv(GL_LIGHT2, GL_POSITION, [3.0, luz2_y, 0.0, 1.0])
    
    # Dibujar objetos principales
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 50)
    
    # Esfera central
    dibujar_esfera_en(0, 0, 0, 1.5)
    
    # Cubos alrededor
    for i in range(4):
        angulo = i * math.pi / 2
        x = math.cos(angulo) * 3
        z = math.sin(angulo) * 3
        glPushMatrix()
        glTranslatef(x, 0, z)
        glutSolidCube(1.0)
        glPopMatrix()
    
    # Dibujar posiciones de las luces
    dibujar_posicion_luz(1, luz1_x, 2.0, luz1_z, [1.0, 0.2, 0.2])  # Roja
    dibujar_posicion_luz(2, 3.0, luz2_y, 0.0, [0.2, 0.2, 1.0])    # Azul
    
    # Título informativo
    glfw.set_window_title(ventana, 
        f"3 Luces Activas - Luz1: ({luz1_x:.1f}, 2.0, {luz1_z:.1f}) - "
        f"Luz2: (3.0, {luz2_y:.1f}, 0.0)")
    
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()