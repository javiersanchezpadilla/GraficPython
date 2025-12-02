""" Stack Overflow
    La función glLightfv() es como el panel de control completo de una luz en OpenGL
    No solo controla la posición, sino 10 propiedades diferentes

    Resumen de TODOS los usos de glLightfv():

    1. GL_POSITION - Posición y tipo de luz             
    glLightfv(GL_LIGHT0, GL_POSITION, [x, y, z, w])

    2. GL_AMBIENT - Luz ambiente (iluminación global)   
    glLightfv(GL_LIGHT0, GL_AMBIENT, [R, G, B, A])      [0.2, 0.2, 0.2, 1.0] Gris suave en toda la escena

    3. GL_DIFFUSE - Luz difusa (color principal)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [R, G, B, A])      [1.0, 1.0, 1.0, 1.0] Blanco brillante

    4. GL_SPECULAR - Luz especular (reflejos/brillos) 
    glLightfv(GL_LIGHT0, GL_SPECULAR, [R, G, B, A])     [1.0, 1.0, 1.0, 1.0] Reflejos blancos

    5. GL_SPOT_DIRECTION - Dirección del foco
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [dx, dy, dz])   Solo para luces tipo foco/reflector

    
    Y con glLightf() (versión para valores individuales):

    6. GL_SPOT_CUTOFF - Ángulo del foco
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, angulo)         0-90 grados, o 180 para desactivar foco

    7. GL_SPOT_EXPONENT - Intensidad del foco
    glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, valor)        0-128, mayor = foco más concentrado

    8. GL_CONSTANT_ATTENUATION - Atenuación constante

    9. GL_LINEAR_ATTENUATION - Atenuación lineal

    10. GL_QUADRATIC_ATTENUATION - Atenuación cuadrática

    Cómo disminuye la luz con la distancia
            glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
            glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)  
            glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.01)

    PODEMOS PROBAR LAS SIGUIENTES COMBINACIONES
    ===========================================

    LUZ DE SOL (direccional, blanca)
            glLightfv(GL_LIGHT0, GL_POSITION, [0, 1, 0, 0.0])
            glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 0.95, 0.9, 1.0])  # Blanco cálido

    LUZ DE LUNA (azulada, suave)  
            glLightfv(GL_LIGHT0, GL_POSITION, [0.2, 1, 0.3, 0.0])
            glLightfv(GL_LIGHT0, GL_AMBIENT, [0.1, 0.1, 0.3, 1.0])
            glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.2, 0.2, 0.5, 1.0])

    FOCO DE ESCENARIO (spotlight rojo)
            glLightfv(GL_LIGHT0, GL_POSITION, [0, 5, 0, 1.0])
            glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 0.2, 0.2, 1.0])
            glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0, -1, 0])
            glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 25.0)

    LINTERNA DEL JUGADOR (sigue al personaje)
            glLightfv(GL_LIGHT0, GL_POSITION, [jugador_x, jugador_y+1, jugador_z, 1.0])
            glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [jugador_mira_x, jugador_mira_y, jugador_mira_z])
            glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 45.0)

"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *           # PAra que funcione glut (recordar que tenemos que inicializar glutInit())
import math
import time

def mostrar_todas_las_propiedades():
    """Demuestra TODAS las propiedades que se pueden controlar con glLightfv()"""
    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    
    # 1. POSICIÓN (ya la conoces)
    glLightfv(GL_LIGHT0, GL_POSITION, [2, 3, 2, 1])  # Posición y tipo
    
    # 2. COLOR AMBIENTE - Iluminación general (como luz rebotada)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    # ↑ Color gris suave que ilumina TODO, incluso sombras
    
    # 3. COLOR DIFUSO - Color principal de la luz
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
    # ↑ Color blanco para la iluminación directa
    
    # 4. COLOR ESPECULAR - Color de los reflejos/brillos
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    # ↑ Blanco puro para reflejos brillantes
    
    # 5. ATENUACIÓN - Cómo disminuye la luz con la distancia
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)   # Constante
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)    # Lineal  
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.01) # Cuadrática
    
    # 6. FOCO DIRECCIONAL (SPOT) - Para luces tipo reflector
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0, -1, 0])  # Dirección del foco
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 30.0)            # Ángulo del cono (grados)
    glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 2.0)           # Intensidad dentro del cono

# Ejemplo Interactivo Completo
if not glfw.init():
    exit()

ventana = glfw.create_window(1000, 700, "TODAS las propiedades de glLightfv()", None, None)
glfw.make_context_current(ventana)

                        # ***********************************************************************
glutInit()              # Activamos GLUT                                                    *****
                        # recordar que el caso de windows tienen que crear una ventanita    *****
                        # glutCreateWindow(b"La ventanita")
                        # ***********************************************************************



glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)

# Variables para control interactivo
luz_color = [1.0, 1.0, 1.0, 1.0]  # Color blanco
luz_ambiente = [0.2, 0.2, 0.2, 1.0]
luz_difusa = [0.8, 0.8, 0.8, 1.0]
luz_especular = [1.0, 1.0, 1.0, 1.0]
es_foco = False
angulo_foco = 30.0

def dibujar_escena_demostracion():
    """Escena para demostrar efectos de diferentes propiedades"""
    
    # Configurar propiedades actuales
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 5, 3, 1])
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)
    
    # Configurar foco si está activado
    if es_foco:
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0, -1, 0])
        glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, angulo_foco)
        glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 2.0)
    else:
        glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 180.0)  # Desactivar foco
    
    # Piso con rejilla
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.4, 0.4, 0.4, 1.0])
    for x in range(-5, 6):
        for z in range(-5, 6):
            glPushMatrix()
            glTranslatef(x, -1, z)
            glutSolidCube(0.9)
            glPopMatrix()
    
    # Objetos con diferentes materiales
    # Esfera ROJA - Material mate
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 0.2, 0.2, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.3, 0.3, 0.3, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 30)
    glPushMatrix()
    glTranslatef(-2, 0, 0)
    glutSolidSphere(0.8, 32, 32)
    glPopMatrix()
    
    # Esfera VERDE - Material plástico brillante
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.2, 1.0, 0.2, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.8, 0.8, 0.8, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 60)
    glPushMatrix()
    glTranslatef(0, 0, -2)
    glutSolidSphere(0.8, 32, 32)
    glPopMatrix()
    
    # Esfera AZUL - Material metálico
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.2, 0.2, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100)
    glPushMatrix()
    glTranslatef(2, 0, 0)
    glutSolidSphere(0.8, 32, 32)
    glPopMatrix()
    
    # Cubo AMARILLO - Para ver efectos de foco
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 1.0, 0.2, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.5, 0.5, 0.5, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 40)
    glPushMatrix()
    glTranslatef(0, 0, 2)
    glutSolidCube(1.2)
    glPopMatrix()

# Bucle principal
tiempo = 0
while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar vista
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1000/700, 0.1, 100.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(8, 6, 8,  0, 0, 0,  0, 1, 0)
    
    # Rotar escena lentamente
    tiempo += 0.01
    glRotatef(math.sin(tiempo * 0.5) * 10, 0, 1, 0)
    
    dibujar_escena_demostracion()
    
    # Controles para cambiar propiedades
    if glfw.get_key(ventana, glfw.KEY_1) == glfw.PRESS:
        # Cambiar COLOR AMBIENTE
        luz_ambiente = [0.3, 0.1, 0.1, 1.0]  # Rojo ambiente
        print("Ambiente: Rojo suave")
    
    if glfw.get_key(ventana, glfw.KEY_2) == glfw.PRESS:
        # Cambiar COLOR DIFUSO  
        luz_difusa = [0.2, 0.8, 0.2, 1.0]  # Verde difuso
        print("Difuso: Verde")
    
    if glfw.get_key(ventana, glfw.KEY_3) == glfw.PRESS:
        # Cambiar COLOR ESPECULAR
        luz_especular = [0.8, 0.8, 0.1, 1.0]  # Amarillo especular
        print("Especular: Amarillo (reflejos amarillos)")
    
    if glfw.get_key(ventana, glfw.KEY_4) == glfw.PRESS:
        # Cambiar a LUZ AZULADA
        luz_ambiente = [0.1, 0.1, 0.3, 1.0]
        luz_difusa = [0.2, 0.2, 0.8, 1.0]
        luz_especular = [0.5, 0.5, 1.0, 1.0]
        print("Luz: Azul (como luz de luna)")
    
    if glfw.get_key(ventana, glfw.KEY_5) == glfw.PRESS:
        # Activar/desactivar FOCO
        es_foco = not es_foco
        print(f"Foco: {'ACTIVADO' if es_foco else 'DESACTIVADO'}")
    
    if glfw.get_key(ventana, glfw.KEY_6) == glfw.PRESS:
        # Cambiar ángulo del foco
        angulo_foco = 15.0 if angulo_foco == 30.0 else 30.0
        print(f"Ángulo foco: {angulo_foco}°")
    
    if glfw.get_key(ventana, glfw.KEY_R) == glfw.PRESS:
        # Reset a valores por defecto
        luz_ambiente = [0.2, 0.2, 0.2, 1.0]
        luz_difusa = [0.8, 0.8, 0.8, 1.0]
        luz_especular = [1.0, 1.0, 1.0, 1.0]
        es_foco = False
        print("Reset a valores por defecto")
    
    # Información en título
    estado_foco = f"Foco: {angulo_foco}°" if es_foco else "Sin foco"
    glfw.set_window_title(ventana, 
        f"glLightfv() Demo - {estado_foco} - 1:Ambiente 2:Difuso 3:Especular")
    
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()