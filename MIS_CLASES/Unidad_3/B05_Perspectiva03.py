""" gluLookAt()  Entendiendo la función.

    gluLookAt(): Colocar y Apuntar la Cámara (Matriz de Vista)
    gluLookAt() define dónde está la cámara, hacia dónde está mirando y cuál es su orientación vertical.
    Su Función: Mueve el mundo entero de forma que parezca que la cámara se ha movido o rotado.

    ¿Cómo funciona?
    Esta función toma 9 argumentos que se organizan en 3 grupos de coordenadas (X, Y, Z):

    gluLookAt(camara_x, camara_y, camara_z,         1. Posición de la Cámara (Eye)
              mirar_x,  mirar_y,  mirar_z,          2. El Punto al que Mira (Center)
              arriba_x, arriba_y, arriba_z)         3. La Orientación Vertical (Up)

    camara (Posición de la Cámara): ¿Dónde está el fotógrafo? Si pones (0, 0, 10), la cámara está en (0, 0, 10).
    mirar (Punto al que Mira): ¿Hacia dónde apunta el fotógrafo? Si pones (0, 0, 0), la cámara mira 
    directamente al origen del mundo 3D.
    arriba (Orientación Vertical): ¿Qué es "arriba" para la cámara? Casi siempre es (0, 1, 0). Esto significa que 
    el eje Y es la dirección vertical de tu cámara (el lado superior de la pantalla).

    Analogía:
    Usar gluLookAt(0, 2, 5, 0, 0, 0, 0, 1, 0)       es como decir: "Coloca al fotógrafo 5 metros delante del 
                                                    origen y 2 metros por encima, apuntando al centro, y mantén 
                                                    la cabeza derecha (el eje Y es arriba).


                                                    
    EXPLICACION VISUAL DE gluLookAt()
    ---------------------------------
    ANALOGÍA: gluLookAt() es como posicionar una CÁMARA FÍSICA

    gluLookAt(
        2, 3, 5,    <--- ¿DÓNDE ESTÁ EL FOTÓGRAFO?  Fotógrafo en posición (2, 3, 5)
        0, 0, 0,    <--- ¿HACIA DÓNDE APUNTA LA CÁMARA?  Enfoca al punto (0, 0, 0) - el origen
        0, 1, 0     <--- ¿QUÉ DIRECCIÓN ES "ARRIBA" EN LA CÁMARA?   El eje Y es "arriba" (normal)
        )

        
    EJEMPLO PRÁCTICOS COMUNES:
    --------------------------

    VISTA FRONTAL (como mirar un cuadro)
        gluLookAt(0, 0, 5,   0, 0, 0,   0, 1, 0)

    VISTA SUPERIOR (como mirar un mapa)
        gluLookAt(0, 5, 0,   0, 0, 0,   0, 0, -1)  # ¡Arriba es -Z!

    VISTA EN PICADO (como desde un edificio alto)
        gluLookAt(0, 10, 10,   0, 0, 0,   0, 1, 0)

    VISTA ORBITANTE (cámara que gira alrededor)
        angulo = tiempo * 0.5
        radio = 8
        cam_x = radio * math.cos(angulo)
        cam_z = radio * math.sin(angulo)
        gluLookAt(cam_x, 3, cam_z,   0, 0, 0,   0, 1, 0)

    CÁMARA EN PRIMERA PERSONA
        gluLookAt(
            jugador_x, jugador_y, jugador_z,             <--- Posición del jugador
            jugador_x + mirar_x, jugador_y, jugador_z,   <--- Mira hacia adelante
            0, 1, 0                                      <--- Arriba normal
        )

        
    EL VECTOR "ARRIBA" - CASOS ESPECIALES:
    --------------------------------------

    NORMAL (como cámara en trípode)
        gluLookAt(0, 0, 5,  0, 0, 0,  0, 1, 0)

    CÁMARA INVERTIDA (como cabeza hacia abajo)
        gluLookAt(0, 0, 5,  0, 0, 0,  0, -1, 0)

    CÁMARA LADEADA 45° (como inclinar la cabeza)
        gluLookAt(0, 0, 5,  0, 0, 0,  0.7, 0.7, 0)      <--- 45° diagonal

"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Variables de la cámara               gluLookAt(
camara_x, camara_y, camara_z = 0, 0, 5      # camara_x, camara_y, camara_z,     ¿DÓNDE ESTÁ LA CÁMARA?
mirar_x, mirar_y, mirar_z = 0, 0, 0         # mirar_x, mirar_y, mirar_z,        ¿HACIA DÓNDE MIRA?
arriba_x, arriba_y, arriba_z = 0, 1, 0      # arriba_x, arriba_y, arriba_z )    ¿QUÉ ES "ARRIBA"?


def dibujar_escena_simple():
    """Escena con objetos en posiciones conocidas"""
    
    glBegin(GL_LINES)                               # Dibujar los ejes de coordenadas
    glColor3f(1, 0, 0)                              # Eje "x" color ROJO
    glVertex3f(-10, 0, 0); glVertex3f(10, 0, 0)

    glColor3f(0, 1, 0)                              # Eje "y" color VERDE
    glVertex3f(0, -10, 0); glVertex3f(0, 10, 0)

    glColor3f(0, 0, 1)                              # Eje "z" color AZUL
    glVertex3f(0, 0, -10); glVertex3f(0, 0, 10)
    glEnd()
    
    glColor3f(1, 0, 0)                              # Cubo ROJO en el origen
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glutSolidCube(1)
    glPopMatrix()
    
    glColor3f(0, 1, 0)                              # Esfera VERDE en (3, 0, 0)
    glPushMatrix()
    glTranslatef(3, 0, 0)
    glutSolidSphere(0.5, 16, 16)
    glPopMatrix()
    
    glColor3f(0, 0, 1)                              # Toroide (la dona) AZUL en (0, 0, 3)
    glPushMatrix()
    glTranslatef(0, 0, 3)
    glutSolidTorus(0.3, 0.7, 12, 24)
    glPopMatrix()
    
    glColor3f(1, 1, 0)                              # Cono AMARILLO en (-3, 0, 0)
    glPushMatrix()
    glTranslatef(-3, 0, 0)
    glRotatef(-90, 1, 0, 0)  # Apuntar hacia arriba
    glutSolidCone(0.5, 1, 16, 8)
    glPopMatrix()



def mostrar_info_camara():
    """Muestra la configuración actual de la cámara"""
    print(f"gluLookAt(")
    print(f"  {camara_x}, {camara_y}, {camara_z},    # Posición cámara")
    print(f"  {mirar_x}, {mirar_y}, {mirar_z},       # Punto de mira")  
    print(f"  {arriba_x}, {arriba_y}, {arriba_z}     # Vector arriba")
    print(f")")


if not glfw.init():
    exit()

ventana = glfw.create_window(800, 600, "gluLookAt() - Prueba Interactiva", None, None)
glfw.make_context_current(ventana)
glutInit()                      # inicializa FreeGLUT

glEnable(GL_DEPTH_TEST)

print("=== CONTROLES ===")
print("WASD: Mover cámara")
print("Flechas: Mirar a diferentes puntos")  
print("Q/E: Acercar/Alejar")
print("R: Reset cámara")
print("1-6: Vistas predefinidas")
print("=================")

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar perspectiva
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 100.0)
    
    # CONFIGURAR CÁMARA con gluLookAt()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        camara_x, camara_y, camara_z,  # ¿DÓNDE ESTÁ LA CÁMARA?
        mirar_x, mirar_y, mirar_z,     # ¿HACIA DÓNDE MIRA?
        arriba_x, arriba_y, arriba_z   # ¿QUÉ ES "ARRIBA"?
    )
    
    dibujar_escena_simple()
    
    # Controles para modificar los valores de gluLookAt() (la cámara)
    velocidad = 0.1
    
    # MOVER CÁMARA
    if glfw.get_key(ventana, glfw.KEY_W) == glfw.PRESS:
        camara_z -= velocidad
    if glfw.get_key(ventana, glfw.KEY_S) == glfw.PRESS:
        camara_z += velocidad
    if glfw.get_key(ventana, glfw.KEY_A) == glfw.PRESS:
        camara_x -= velocidad
    if glfw.get_key(ventana, glfw.KEY_D) == glfw.PRESS:
        camara_x += velocidad
    if glfw.get_key(ventana, glfw.KEY_Q) == glfw.PRESS:
        camara_y -= velocidad
    if glfw.get_key(ventana, glfw.KEY_E) == glfw.PRESS:
        camara_y += velocidad
    
    # MOVER PUNTO DE MIRA
    if glfw.get_key(ventana, glfw.KEY_UP) == glfw.PRESS:
        mirar_y += velocidad
    if glfw.get_key(ventana, glfw.KEY_DOWN) == glfw.PRESS:
        mirar_y -= velocidad
    if glfw.get_key(ventana, glfw.KEY_LEFT) == glfw.PRESS:
        mirar_x -= velocidad
    if glfw.get_key(ventana, glfw.KEY_RIGHT) == glfw.PRESS:
        mirar_x += velocidad
    
    # VISTAS PREDEFINIDAS
    if glfw.get_key(ventana, glfw.KEY_1) == glfw.PRESS:  # Vista frontal
        camara_x, camara_y, camara_z = 0, 0, 5
        mirar_x, mirar_y, mirar_z = 0, 0, 0
        arriba_x, arriba_y, arriba_z = 0, 1, 0
        print("Vista FRONTAL")
        mostrar_info_camara()
    
    if glfw.get_key(ventana, glfw.KEY_2) == glfw.PRESS:  # Vista lateral
        camara_x, camara_y, camara_z = 5, 0, 0
        mirar_x, mirar_y, mirar_z = 0, 0, 0  
        arriba_x, arriba_y, arriba_z = 0, 1, 0
        print("Vista LATERAL")
        mostrar_info_camara()
    
    if glfw.get_key(ventana, glfw.KEY_3) == glfw.PRESS:  # Vista superior
        camara_x, camara_y, camara_z = 0, 5, 0
        mirar_x, mirar_y, mirar_z = 0, 0, 0
        arriba_x, arriba_y, arriba_z = 0, 0, -1  # ¡Importante!
        print("Vista SUPERIOR")
        mostrar_info_camara()
    
    if glfw.get_key(ventana, glfw.KEY_4) == glfw.PRESS:  # Vista isométrica
        camara_x, camara_y, camara_z = 4, 3, 4
        mirar_x, mirar_y, mirar_z = 0, 0, 0
        arriba_x, arriba_y, arriba_z = 0, 1, 0
        print("Vista ISOMÉTRICA")
        mostrar_info_camara()
    
    if glfw.get_key(ventana, glfw.KEY_5) == glfw.PRESS:  # Cámara invertida
        camara_x, camara_y, camara_z = 0, 0, 5
        mirar_x, mirar_y, mirar_z = 0, 0, 0
        arriba_x, arriba_y, arriba_z = 0, -1, 0  # ¡Arriba invertido!
        print("Cámara INVERTIDA")
        mostrar_info_camara()
    
    if glfw.get_key(ventana, glfw.KEY_6) == glfw.PRESS:  # Vista desde atrás
        camara_x, camara_y, camara_z = 0, 0, -5
        mirar_x, mirar_y, mirar_z = 0, 0, 0
        arriba_x, arriba_y, arriba_z = 0, 1, 0
        print("Vista TRASERA")
        mostrar_info_camara()
    
    # Reset
    if glfw.get_key(ventana, glfw.KEY_R) == glfw.PRESS:
        camara_x, camara_y, camara_z = 0, 0, 5
        mirar_x, mirar_y, mirar_z = 0, 0, 0
        arriba_x, arriba_y, arriba_z = 0, 1, 0
        print("Cámara RESETEADA")
        mostrar_info_camara()
    
    # Actualizar título en la ventana con la información de la cámara
    glfw.set_window_title(ventana, 
        f"gluLookAt() - Cam: ({camara_x:.1f},{camara_y:.1f},{camara_z:.1f}) "
        f"Mirar: ({mirar_x:.1f},{mirar_y:.1f},{mirar_z:.1f}) "
        f"Arriba:({arriba_x:.1f},{arriba_y:.1f},{arriba_z:.1f})")
    
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()