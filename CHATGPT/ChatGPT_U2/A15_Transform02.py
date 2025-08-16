""" Ejemplo: Una casa con chimenea y humo animado

    Queremos dibujar una casa fija, con un techo girando lentamente 
    (como si fuera un molino), y una chimenea que suelta humo en movimiento.
    Esto nos permitirá ver cómo cada parte de la escena tiene su sistema 
    de referencia independiente, pero todo se integra en la misma escena.

    Qué aprendemos aquí

    Casa fija: La base de la casa no depende de nada, se dibuja sin 
    transformaciones acumuladas.

    Techo giratorio: Se aplica glTranslatef para colocarlo encima de la casa, 
    luego glRotatef para girarlo.
    Si hubiéramos rotado antes de trasladar, el techo giraría en el centro 
    de la ventana, no en la casa.

    Chimenea + humo: La chimenea se traslada a un costado.
    El humo se genera en un bucle, cada círculo se anima con sin(tiempo) para oscilar como si el viento lo moviera.
    Cada humo se dibuja dentro de un glPushMatrix para que se aplique su propio desplazamiento sin afectar a los demás.

    Este ejemplo muestra cómo puedes armar objetos compuestos:

    La casa es una base estática.
    El techo depende de la casa.
    La chimenea depende del techo.
    El humo depende de la chimenea.

    Todo se combina gracias a las transformaciones jerárquicas (glPushMatrix y glPopMatrix).
"""

import glfw
from OpenGL.GL import *
import math

# Inicializar GLFW
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(700, 700, "Casa con humo animado", None, None)
glfw.make_context_current(window)

def dibujar_cuadrado(lado, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(-lado/2, -lado/2)
    glVertex2f(lado/2, -lado/2)
    glVertex2f(lado/2, lado/2)
    glVertex2f(-lado/2, lado/2)
    glEnd()

def dibujar_triangulo(base, altura, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    glVertex2f(-base/2, 0)
    glVertex2f(base/2, 0)
    glVertex2f(0, altura)
    glEnd()

def dibujar_circulo(radio, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for ang in range(361):
        rad = math.radians(ang)
        glVertex2f(math.cos(rad) * radio, math.sin(rad) * radio)
    glEnd()

# Bucle principal
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    tiempo = glfw.get_time()

    # --- Casa (base) ---
    glPushMatrix()
    glTranslatef(0, -0.3, 0)  # bajar la casa un poco
    dibujar_cuadrado(0.6, (0.8, 0.5, 0.2))  # pared café
    glPopMatrix()

    # --- Techo girando ---
    glPushMatrix()
    glTranslatef(0, 0.0, 0)   # encima de la casa
    glRotatef(tiempo * 20, 0, 0, 1)  # gira lentamente
    dibujar_triangulo(0.8, 0.4, (1, 0, 0))  # rojo
    glPopMatrix()

    # --- Chimenea ---
    glPushMatrix()
    glTranslatef(0.2, 0.2, 0)  # lado derecho del techo
    dibujar_cuadrado(0.1, (0.4, 0.4, 0.4))  # gris oscuro

    # --- Humo animado ---
    for i in range(3):
        glPushMatrix()
        glTranslatef(0, 0.15 + i*0.15 + 0.05*math.sin(tiempo*2+i), 0)
        dibujar_circulo(0.05, (0.9, 0.9, 0.9))  # humo gris claro
        glPopMatrix()

    glPopMatrix()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()


