""" Sistema Solar en 2D usando transformaciones independientes con glPushMatrix() y glPopMatrix().

    Conceptos clave

    Jerarquía de transformaciones:
    Usamos glPushMatrix() y glPopMatrix() para aislar movimientos.

    Rotación para órbita:
    glRotatef(tiempo * velocidad_orbita, 0, 0, 1)

    Traslación para distancia:
    glTranslatef(distancia, 0, 0)

    Rotación propia:
    glRotatef(tiempo * velocidad_rotacion, 0, 0, 1)

    TIEMPO ************
    tiempo = glfw.get_time()

    ¿Qué es?  Es el número de segundos (en float) desde que se abrió la ventana.
    Ejemplo:
    En el instante de inicio → tiempo = 0.0
    Después de 3 segundos → tiempo = 3.0
    Después de 10 segundos → tiempo = 10.0

    ¿Por qué lo usamos?
    Si multiplicamos este tiempo por un factor (velocidad), obtenemos un ángulo que crece 
    con el tiempo, lo que nos permite hacer animaciones sin tener que incrementar manualmente 
    variables.

    
    DISTANCIA
    glTranslatef(0.6, 0, 0)  # Distancia al sol

    Es un valor fijo que indica cuántas unidades OpenGL queremos que el planeta esté separado del Sol.
    No cambia con el tiempo (a menos que quieras simular una órbita elíptica).
    Unidad OpenGL ≠ píxeles → es relativo al sistema de coordenadas normalizadas.

    VELOCIDAD DE ORBITA
    glRotatef(tiempo * 30, 0, 0, 1)  # Órbita

    Aquí 30 significa 30 grados por segundo.
    tiempo * 30 produce un ángulo creciente:

    Si tiempo = 1s → 30°
    Si tiempo = 2s → 60°
    Si tiempo = 3s → 90°

    Como glRotatef rota el sistema de coordenadas, el planeta parece dar vueltas alrededor del Sol.


    VELOCIDAD DE ROTACIÓN (PROPIA)
    glRotatef(tiempo * 100, 0, 0, 1)  # Rotación sobre sí mismo

    Aquí 100 significa 100 grados por segundo.
    Sirve para que el planeta gire sobre su propio eje.
    Es independiente de la órbita, porque se aplica después de mover el planeta a su posición.

    RESUMEN VISUAL DEL CÁLCULO
    Imagina el planeta:
    Rotamos todo el sistema (órbita) → esto mueve la posición alrededor del Sol.
    Trasladamos al planeta a su distancia del Sol.
    Rotamos otra vez (rotación propia) → el planeta gira en su lugar.
"""

import glfw
from OpenGL.GL import *
import math


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Primitivas en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana

def dibujar_circulo(radio, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for ang in range(0, 361, 10):
        ang_rad = math.radians(ang)
        glVertex2f(math.cos(ang_rad) * radio, math.sin(ang_rad) * radio)
    glEnd()


# Aquí pondremos el código para dibujar primitivas
ventana = iniciar_ventana()

while not glfw.window_should_close(ventana):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    tiempo = glfw.get_time()
    print(f"Tiempo: {tiempo:.2f} segundos. POR 30 = {tiempo * 30:.2f} grados de órbita. POR 100 = {tiempo * 100:.2f} grados de rotación propia.")

    # ☀️ Sol en el centro
    glPushMatrix()
    dibujar_circulo(0.2, 1.0, 0.8, 0.0)  # Amarillo
    glPopMatrix()

    # 🌍 Planeta que orbita
    glPushMatrix()
    glRotatef(tiempo * 30, 0, 0, 1)  # Órbita
    glTranslatef(0.6, 0, 0)  # Distancia al sol
    glRotatef(tiempo * 100, 0, 0, 1)  # Rotación sobre sí mismo
    dibujar_circulo(0.08, 0.0, 0.5, 1.0)  # Azul
    glPopMatrix()

    # 🪐 Planeta con luna
    glPushMatrix()
    glRotatef(tiempo * 20, 0, 0, 1)  # Órbita
    glTranslatef(1.0, 0, 0)  # Distancia al sol
    glRotatef(tiempo * 60, 0, 0, 1)  # Rotación propia
    dibujar_circulo(0.1, 0.8, 0.3, 0.0)  # Marrón

    # 🌙 Luna
    glPushMatrix()
    glRotatef(tiempo * 200, 0, 0, 1)  # Órbita de la luna
    glTranslatef(0.2, 0, 0)
    dibujar_circulo(0.03, 0.8, 0.8, 0.8)  # Gris
    glPopMatrix()

    glPopMatrix()

    glfw.swap_buffers(ventana)

glfw.terminate()
