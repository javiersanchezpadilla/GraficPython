"""
    glLightfv(GL_LIGHT0, GL_POSITION, [x, y, z, w])
                     ↑     ↑           ↑  ↑  ↑  ↑
                     |     |           |  |  |  |
                     |     |           |  |  |  ╰── TIPO de luz (1.0 = posicional, 0.0 = direccional)
                     |     |           |  |  ╰───── Coordenada Z (profundidad)
                     |     |           |  ╰──────── Coordenada Y (altura)  
                     |     |           ╰─────────── Coordenada X (ancho)
                     |     ╰───────────────── Establecer posición de la luz
                     ╰─────────────────────── Luz número 0
    
    Diferencia Visual Clave
    Con w=1.0 (Posicional):
        Los objetos CERCANOS a la luz se ven más brillantes
        Los objetos LEJANOS se ven más oscuros
        Como una bombilla real

    Con w=0.0 (Direccional):
        Todos los objetos se iluminan IGUAL sin importar distancia
        Como un día muy nublado o luz artificial uniforme, o la luna o el sol

    [x, y, z, w] = [2, 2, 2, 1]
                    x=2, y=2, z=2 → POSICIÓN en el espacio 3D


    # La luz está en el punto (2, 2, 2) del mundo
    # Es como colocar un foco en esa posición exacta

    [0, 0, 0, 1]   # Luz EN el objeto (mala iluminación)
    [2, 2, 2, 1]   # Luz a 2 unidades en cada eje (buena)
    [0, 5, 0, 1]   # Luz directamente arriba
    [-3, 2, 4, 1]  # Luz en posición asimétrica

    
    w=1 → TIPO DE LUZ (¡ES EL MÁS IMPORTANTE!)

    w = 1.0 → LUZ POSICIONAL (como un foco/bombilla)  
    [2, 2, 2, 1.0]  Foco en posición (2,2,2)

        Los rayos salen de un punto específico
        La dirección de la luz cambia según la posición del objeto
        Como una bombilla en una habitación

        
    w = 0.0 → LUZ DIRECCIONAL (como el sol)
    [0, 0, 1, 0.0]  Luz que viene en dirección Z
        Todos los rayos son paralelos
        La dirección es constante, no importa dónde esté el objeto  
        Como la luz del sol (viene de muy lejos)

    
    Luces Posicionales (w=1.0):
    ---------------------------
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 5, 0, 1.0])                                       Foco en el techo
    glLightfv(GL_LIGHT0, GL_POSITION, [2, 1, 3, 1.0])                                       Lámpara en una mesa
    glLightfv(GL_LIGHT0, GL_POSITION, [personaje_x, personaje_y+1, personaje_z, 1.0])       Linterna en mano del personaje

    
    Luces Direccionales (w=0.0):
    ---------------------------
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 1, 0, 0.0])                                       Sol de mediodía (ilumina desde arriba)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 0.5, 0, 0.0])                                     Sol de tarde (ilumina lateralmente)  
    glLightfv(GL_LIGHT0, GL_POSITION, [0.2, 1, 0.3, 0.0])                                   Luz de luna (iluminación suave)

    Diferencia Visual Clave
    Con w=1.0 (Posicional):
        Los objetos CERCANOS a la luz se ven más brillantes
        Los objetos LEJANOS se ven más oscuros
        Como una bombilla real

    Con w=0.0 (Direccional):
        Todos los objetos se iluminan IGUAL sin importar distancia
        Como un día muy nublado o luz artificial uniforme
"""


import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Variables para ajustar la posición de la luz
# desempaquetamos los valores en cada variable
luz_x, luz_y, luz_z, luz_w = 2.0, 2.0, 2.0, 1.0

def dibujar_escena_con_luz():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    
    # CONFIGURAR LA LUZ CON LOS 4 PARÁMETROS
    luz_posicion = [luz_x, luz_y, luz_z, luz_w]
    glLightfv(GL_LIGHT0, GL_POSITION, luz_posicion)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
    
    # Dibujar esfera en el origen
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.2, 0.2, 1.0])
    glutSolidSphere(1, 32, 32)
    
    # Dibujar ejes para referencia
    # desabilitamos la luz para que los ejes no sean afectados por la luz
    glDisable(GL_LIGHTING)
    glBegin(GL_LINES)
    # Eje X (Rojo)
    glColor3f(1, 0, 0); glVertex3f(0, 0, 0); glVertex3f(3, 0, 0)
    # Eje Y (Verde)
    glColor3f(0, 1, 0); glVertex3f(0, 0, 0); glVertex3f(0, 3, 0)
    # Eje Z (Azul)  
    glColor3f(0, 0, 1); glVertex3f(0, 0, 0); glVertex3f(0, 0, 3)
    glEnd()
    glEnable(GL_LIGHTING)
    
    # Dibujar la posición de la luz como esfera amarilla
    glDisable(GL_LIGHTING)
    glColor3f(1, 1, 0)
    glPushMatrix()
    glTranslatef(luz_x, luz_y, luz_z)
    glutSolidSphere(0.1, 8, 8)
    glPopMatrix()
    glEnable(GL_LIGHTING)

if not glfw.init():
    exit()

ventana = glfw.create_window(800, 600, "Entendiendo Luz: [2, 2, 2, 1]", None, None)
glfw.make_context_current(ventana)


                        # ***********************************************************************
glutInit()              # Activamos GLUT                                                    *****
                        # recordar que el caso de windows tienen que crear una ventanita    *****
                        # glutCreateWindow(b"La ventanita")
                        # ***********************************************************************




print("=== CONTROLES ===")
print("Tecla 1 o 2: Cambiar X de la luz")
print("Tecla 3 o 4: Cambiar Y de la luz") 
print("Tecla 5 o 6: Cambiar Z de la luz")
print("W: Cambiar tipo (1.0=Posicional, 0.0=Direccional)")
print("   Posicional(como lampara), Direccional(como el sol)")
print("=================")

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar vista
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 50.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3, 3, 3,  0, 0, 0,  0, 1, 0)
    
    dibujar_escena_con_luz()
    
    # Controles para modificar la luz
    if glfw.get_key(ventana, glfw.KEY_1) == glfw.PRESS:
        luz_x = max(-5, luz_x - 0.1)
    if glfw.get_key(ventana, glfw.KEY_2) == glfw.PRESS:
        luz_x = min(5, luz_x + 0.1)
    if glfw.get_key(ventana, glfw.KEY_3) == glfw.PRESS:
        luz_y = max(-5, luz_y - 0.1)
    if glfw.get_key(ventana, glfw.KEY_4) == glfw.PRESS:
        luz_y = min(5, luz_y + 0.1)
    if glfw.get_key(ventana, glfw.KEY_5) == glfw.PRESS:
        luz_z = max(-5, luz_z - 0.1)
    if glfw.get_key(ventana, glfw.KEY_6) == glfw.PRESS:
        luz_z = min(5, luz_z + 0.1)
    if glfw.get_key(ventana, glfw.KEY_W) == glfw.PRESS:
        luz_w = 0.0 if luz_w == 1.0 else 1.0  # Alternar
    
    # Actualizar título
    tipo_luz = "POSICIONAL" if luz_w == 1.0 else "DIRECCIONAL"
    glfw.set_window_title(ventana, 
        f"Luz: [{luz_x:.1f}, {luz_y:.1f}, {luz_z:.1f}, {luz_w}] - {tipo_luz}")
    
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()