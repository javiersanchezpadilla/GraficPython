""" PARAMETRO FVY (Field of View "Y")

    Guía de Valores FOV
    FOV BAJO (10° - 40°) - "Efecto Telefoto"

    10° - Telefoto extremo (como telescopio)    gluPerspective(10, aspecto, near, far)

    EFECTO: Objetos lejanos se ven grandes, poca profundidad

# 30° - Teleobjetivo (como binoculares)  
gluPerspective(30, aspecto, near, far)
# EFECTO: Vista enfocada, perspectiva aplanada
📷 FOV NORMAL (45° - 60°) - "Vista Natural"
python
# 45° - Estándar (vista humana normal)
gluPerspective(45, aspecto, near, far)
# EFECTO: Perspectiva natural, buen balance

# 60° - Ligeramente ampliado
gluPerspective(60, aspecto, near, far)  
# EFECTO: Más campo de visión, algo de distorsión
🎥 FOV ALTO (70° - 120°) - "Gran Angular"
python
# 75° - Videojuegos (FPS típico)
gluPerspective(75, aspecto, near, far)
# EFECTO: Mucho campo visual, objetos cercanos grandes

# 90° - Gran angular (como cámara GoPro)
gluPerspective(90, aspecto, near, far)
# EFECTO: Distorsión perceptible, gran sensación de velocidad

# 120° - Ojo de pez extremo
gluPerspective(120, aspecto, near, far)
# EFECTO: Distorsión severa, bordes curvados
Ejemplo Visual de Efectos
python
# ESCENA: Objeto a 2 unidades vs objeto a 10 unidades

# Con FOV 30° (telefoto):
# - Objeto cercano: ocupa 15% de pantalla
# - Objeto lejano: ocupa 3% de pantalla
# - Diferencia de tamaño: 5x

# Con FOV 90° (gran angular):
# - Objeto cercano: ocupa 40% de pantalla  
# - Objeto lejano: ocupa 8% de pantalla
# - Diferencia de tamaño: 5x (igual proporción pero MÁS EXAGERADO)
Reglas Prácticas:
🎯 Para simulación/realismo: 45°-60°

🎮 Para videojuegos: 60°-90° (más campo visual)

🏙️ Para arquitectura: 30°-45° (menos distorsión)

🚗 Para carreras: 75°-100° (sensación de velocidad)

🔬 Para visualización científica: 20°-40° (enfoque preciso)

Consejo Final:
Empieza con 45° y ajusta según necesites:

Si no ves suficiente escena → aumenta FOV

Si hay mucha distorsión → disminuye FOV



    VALORES DE REFERENCIA PARA FOV (Field o View)
"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL import GLUT
import math

# Ejemplo interactivo para probar diferentes FOV
fov_actual = 45.0

def cambiar_fov(fov):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fov, 800/600, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def dibujar_escena_referencia():
    """Escena con objetos a diferentes distancias para ver el efecto FOV"""
    
    # Objeto MUY cercano (para ver distorsión)
    glColor3f(1, 0, 0)  # Rojo
    glPushMatrix()
    glTranslatef(0, 0, 2)  # Muy cerca!
    GLUT.glutSolidCube(1)
    glPopMatrix()
    
    # Objeto a distancia media  
    glColor3f(0, 1, 0)  # Verde
    glPushMatrix()
    glTranslatef(-3, 1, 8)  # Distancia media
    GLUT.glutSolidCube(1.5)
    glPopMatrix()
    
    # Objeto lejano
    glColor3f(0, 0, 1)  # Azul
    glPushMatrix()
    glTranslatef(4, -1, 15)  # Lejos
    GLUT.glutSolidCube(2)
    glPopMatrix()
    
    # Rejilla para referencia de profundidad
    glColor3f(0.5, 0.5, 0.5)
    for i in range(-10, 11, 2):
        glBegin(GL_LINES)
        glVertex3f(i, 0, -10)
        glVertex3f(i, 0, 20)
        glVertex3f(-10, 0, i)
        glVertex3f(10, 0, i)
        glEnd()

if not glfw.init():
    exit()

ventana = glfw.create_window(800, 600, "Prueba FOV - Actual: 45°", None, None)
glfw.make_context_current(ventana)
GLUT.glutInit()             # Inicializamos glut

glEnable(GL_DEPTH_TEST)

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar con FOV actual
    cambiar_fov(fov_actual)
    
    # Configurar cámara
    glLoadIdentity()
    gluLookAt(0, 5, 10,  0, 0, 0,  0, 1, 0)
    
    dibujar_escena_referencia()
    
    # Cambiar FOV con teclas
    if glfw.get_key(ventana, glfw.KEY_UP) == glfw.PRESS:
        fov_actual = min(120, fov_actual + 1)
        glfw.set_window_title(ventana, f"FOV: {fov_actual}° (Gran angular)")
    
    if glfw.get_key(ventana, glfw.KEY_DOWN) == glfw.PRESS:
        fov_actual = max(10, fov_actual - 1) 
        glfw.set_window_title(ventana, f"FOV: {fov_actual}° (Telefoto)")
    
    # Valores predefinidos
    if glfw.get_key(ventana, glfw.KEY_1) == glfw.PRESS:
        fov_actual = 10
        glfw.set_window_title(ventana, "FOV: 10° (Telefoto extremo)")
    
    if glfw.get_key(ventana, glfw.KEY_2) == glfw.PRESS:
        fov_actual = 30
        glfw.set_window_title(ventana, "FOV: 30° (Teleobjetivo)")
    
    if glfw.get_key(ventana, glfw.KEY_3) == glfw.PRESS:
        fov_actual = 45
        glfw.set_window_title(ventana, "FOV: 45° (Normal)")
    
    if glfw.get_key(ventana, glfw.KEY_4) == glfw.PRESS:
        fov_actual = 60  
        glfw.set_window_title(ventana, "FOV: 60° (Gran angular suave)")
    
    if glfw.get_key(ventana, glfw.KEY_5) == glfw.PRESS:
        fov_actual = 90
        glfw.set_window_title(ventana, "FOV: 90° (Gran angular)")
    
    if glfw.get_key(ventana, glfw.KEY_6) == glfw.PRESS:
        fov_actual = 120
        glfw.set_window_title(ventana, "FOV: 120° (Ojo de pez)")
    
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()

