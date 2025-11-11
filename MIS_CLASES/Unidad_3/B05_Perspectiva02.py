""" El siguiente código permite hacer uso del concepto de perspectiva en una escena 3D. 
    Usando OpenGL y GLFW, se dibujan tres cubos a distintas distancias en el eje Z.
    Se utiliza gluPerspective para definir una proyección en perspectiva y gluLookAt para posicionar la cámara.
    La cámara puede ser movida hacia adelante y hacia atrás con las teclas UP y DOWN,
    y el campo de visión (FOV) puede ser ajustado con las teclas LEFT y RIGHT.
    Esto permite observar cómo la perspectiva afecta la apariencia de los objetos en función de su distancia a la cámara.

    Qué podrás observar:
    --------------------------------------------------------------------------------------
    (flecha arriba) → te acercas al centro (los cubos se agrandan)
    (flecha abajo) → te alejas (los cubos se reducen)
    (izquierda) → haces zoom in (FOV más pequeño)
    (derecha) → haces zoom out (FOV más grande)

    Conclusión visual:
    --------------------------------------------------------------------------------------
    gluLookAt() define dónde está la cámara y hacia dónde mira.
    gluPerspective() controla cómo la cámara proyecta el mundo, es decir, el tipo de lente.
    """

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *       # <-- Aqui estamos importando la biblioteca GLUT FreeGLUT para las figuras precargadas.

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(800, 600, "Cámara interactiva - gluPerspective y gluLookAt", None, None)
glfw.make_context_current(window)
glEnable(GL_DEPTH_TEST)
glutInit()  # Inicializar GLUT para usar cubos

# Variables de cámara
fov = 60       # campo de visión (zoom)
eye_z = 5.0    # distancia de la cámara al origen

# --- FUNCIONES AUXILIARES ---
def cubo(x, y, z, color):
    """Dibuja un cubo sencillo"""
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3fv(color)
    glutWireCube(1.0)
    glPopMatrix()

def dibujar_escena():
    """Dibuja tres cubos en distintas profundidades"""
    cubo(0, 0, 0, (1, 0, 0))     # rojo (cercano)
    cubo(0, 0, -3, (0, 1, 0))    # verde (medio)
    cubo(0, 0, -6, (0, 0, 1))    # azul (lejano)

def display():
    global fov, eye_z
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # --- PROYECCIÓN ---
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fov, 800/600, 0.1, 50)

    # --- CÁMARA ---
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, eye_z, 0, 0, 0, 0, 1, 0)

    # --- ESCENA ---
    dibujar_escena()

    # Mostrar valores actuales
    glWindowPos2f(10, 570)
    text = f"Distancia cámara: {eye_z:.1f} | FOV: {fov}"
    for c in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))

# --- CONTROL DE TECLAS ---
def key_callback(window, key, scancode, action, mods):
    global eye_z, fov
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:      # acercar cámara
            eye_z -= 0.5
        elif key == glfw.KEY_DOWN:  # alejar cámara
            eye_z += 0.5
        elif key == glfw.KEY_LEFT:  # reducir FOV (zoom in)
            fov = max(20, fov - 5)
        elif key == glfw.KEY_RIGHT: # aumentar FOV (zoom out)
            fov = min(100, fov + 5)
        print(f"Cámara Z: {eye_z}, FOV: {fov}")

glfw.set_key_callback(window, key_callback)

# --- BUCLE PRINCIPAL ---
while not glfw.window_should_close(window):
    display()
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
