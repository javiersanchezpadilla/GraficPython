""" Este ejemplo se usa la siguiente configuración.
    Con coordenadas de -15 a 15 en todos los ejes, tu escena tiene un tamaño de 30x30x30 unidades. 
    Si usas la configuración por defecto, probablemente no veas nada o se vea muy pequeño/grande.

    Configuraciones alternativas de la camara.
    OPCIÓN 1: Vista desde arriba
    gluLookAt(0, 30, 0,  0, 0, 0,  0, 0, -1)

    OPCIÓN 2: Vista frontal  
    gluLookAt(0, 0, 30,  0, 0, 0,  0, 1, 0)

    OPCIÓN 3: Vista en diagonal
    gluLookAt(20, 15, 20,  0, 0, 0,  0, 1, 0)

    OPCIÓN 4: Cámara orbitando
    angulo = tiempo * 0.5
    cam_x = 25 * math.cos(angulo)
    cam_z = 25 * math.sin(angulo)
    gluLookAt(cam_x, 15, cam_z,  0, 0, 0,  0, 1, 0)
"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def configurar_perspectiva(ancho, alto):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # CLAVE: Ajustar los planos near y far para que contengan tu escena
    gluPerspective(
        45,              # Ángulo de visión
        ancho/alto,      # Relación de aspecto
        1.0,             # NEAR: un poco menos que tu coordenada Z mínima visible
        50.0             # FAR: un poco más que tu coordenada Z máxima visible
    )
    
    glMatrixMode(GL_MODELVIEW)



def dibujar_ejes():
    """Dibuja ejes coordenados para referencia"""
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)          # Eje X (Rojo)
    glVertex3f(-15, 0, 0)
    glVertex3f(15, 0, 0)
    
    glColor3f(0, 1, 0)          # Eje Y (Verde)
    glVertex3f(0, -15, 0)
    glVertex3f(0, 15, 0)
    
    glColor3f(0, 0, 1)          # Eje Z (Azul)
    glVertex3f(0, 0, -15)
    glVertex3f(0, 0, 15)
    glEnd()



def dibujar_cubo_en(x, y, z, tamaño=1.0):
    """Dibuja un cubo en posición específica"""

    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(tamaño, tamaño, tamaño)
    
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)                                  # Cara frontal (roja)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    
    glColor3f(0, 1, 0)                                  # Cara trasera (verde)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    
    # Resto de caras (FALTA DESARROLLAR ESTA PARTE, PERO CON ESTO SE ENTIENDE)
    glEnd()
    glPopMatrix()



# Configuración principal
if not glfw.init():
    exit()

ventana = glfw.create_window(800, 600, "Escena -15 a 15", None, None)
glfw.make_context_current(ventana)

glEnable(GL_DEPTH_TEST)

tiempo = 0

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar perspectiva
    ancho, alto = glfw.get_window_size(ventana)
    configurar_perspectiva(ancho, alto)
    
    # Configurar cámara - ¡ESTO ES CLAVE!
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        25, 25, 25,    # Cámara POSICIONADA para ver toda la escena
        0, 0, 0,       # Mira al CENTRO de la escena
        0, 1, 0        # Vector "arriba"
    )
    
    # Rotar toda la escena
    tiempo += 0.01
    glRotatef(math.sin(tiempo) * 10, 0, 1, 0)
    
    # Dibujar ejes coordenados
    dibujar_ejes()
    
    # Dibujar objetos en diferentes posiciones de -15 a 15
    dibujar_cubo_en(-10, -10, -10, 2.0)  # Esquina inferior izquierda trasera
    dibujar_cubo_en(10, 10, 10, 2.0)     # Esquina superior derecha delantera
    dibujar_cubo_en(0, 0, 0, 3.0)        # Centro
    dibujar_cubo_en(-15, 0, 0, 1.0)      # Extremo eje X negativo
    dibujar_cubo_en(0, 15, 0, 1.0)       # Extremo eje Y positivo
    
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
