""" Vamos a darle vida a nuestro paisaje
    🌞 Sol moviéndose en trayectoria curva con sin y cos
    ☁️ Nubes desplazándose horizontalmente
    🪟 Parpadeo de luz en ventanas
    🌬 Molino de viento con aspas giratorias usando transformaciones
    📜 Explicación antes del código

    Para animar en OpenGL con Python:

    Variables de estado → guardan posición, ángulo o cualquier valor que 
    cambia con el tiempo.
    Tiempo → usamos time.time() para medir el tiempo y controlar velocidad.
    Delta time → asegura animaciones suaves sin importar la potencia del PC.
    Transformaciones (glTranslatef, glRotatef) → permiten mover o rotar 
    objetos sin cambiar sus coordenadas originales.

    Lo que logramos aquí
    Movimiento del sol → math.cos y math.sin generan un recorrido circular/curvo.
    Nubes flotando → pos_nube aumenta poco a poco y se reinicia.
    Ventanas vivas → math.sin alterna el brillo para simular luz.
    Molino girando → usamos glPushMatrix y glRotatef para girar todas las aspas 
    alrededor de un punto central.
"""

import glfw
from OpenGL.GL import *
import math
import time

# Función para iniciar ventana
def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Reto 4 - Escena Animada", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana

# Función para dibujar círculo
def dibujar_circulo(x, y, radio, r, g, b, segmentos=50):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(r, g, b)
    glVertex2f(x, y)  # centro
    for i in range(segmentos + 1):
        angulo = 2 * math.pi * i / segmentos
        glVertex2f(x + math.cos(angulo) * radio, y + math.sin(angulo) * radio)
    glEnd()

# Variables iniciales
ventana = iniciar_ventana()
tiempo_inicial = time.time()
angulo_aspas = 0
pos_nube = -1.0

while not glfw.window_should_close(ventana):
    tiempo_actual = time.time()
    delta_time = tiempo_actual - tiempo_inicial
    tiempo_inicial = tiempo_actual

    # ---- Actualizar animaciones ----
    # Movimiento circular del sol
    x_sol = math.cos(glfw.get_time() * 0.2) * 0.6
    y_sol = math.sin(glfw.get_time() * 0.2) * 0.4 + 0.3

    # Movimiento horizontal de la nube
    pos_nube += 0.05 * delta_time
    if pos_nube > 1.5:
        pos_nube = -1.5  # reinicia

    # Rotación de aspas
    angulo_aspas += 90 * delta_time  # grados por segundo

    # ---- Dibujar escena ----
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.8, 0.9, 1.0, 1)  # cielo

    # Pasto
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.7, 0.3)
    glVertex2f(-1.0, -0.5)
    glVertex2f(1.0, -0.5)
    glVertex2f(1.0, -1.0)
    glVertex2f(-1.0, -1.0)
    glEnd()

    # Sol
    dibujar_circulo(x_sol, y_sol, 0.15, 1.0, 1.0, 0.0)

    # Nube (varios círculos blancos)
    dibujar_circulo(pos_nube, 0.6, 0.12, 1, 1, 1)
    dibujar_circulo(pos_nube + 0.1, 0.62, 0.12, 1, 1, 1)
    dibujar_circulo(pos_nube - 0.1, 0.62, 0.12, 1, 1, 1)

    # Casa
    glBegin(GL_QUADS)  # pared
    glColor3f(0.9, 0.7, 0.5)
    glVertex2f(-0.4, -0.5)
    glVertex2f(0.4, -0.5)
    glVertex2f(0.4, 0.0)
    glVertex2f(-0.4, 0.0)
    glEnd()

    glBegin(GL_TRIANGLES)  # techo
    glColor3f(0.7, 0.2, 0.2)
    glVertex2f(-0.45, 0.0)
    glVertex2f(0.45, 0.0)
    glVertex2f(0.0, 0.4)
    glEnd()

    glBegin(GL_QUADS)  # puerta
    glColor3f(0.5, 0.3, 0.1)
    glVertex2f(-0.1, -0.5)
    glVertex2f(0.1, -0.5)
    glVertex2f(0.1, -0.2)
    glVertex2f(-0.1, -0.2)
    glEnd()

    # Ventanas con parpadeo
    brillo = abs(math.sin(glfw.get_time() * 3))  # 0 a 1
    glBegin(GL_QUADS)
    glColor3f(0.6 + brillo * 0.4, 0.8, 1.0)  # ventana izquierda
    glVertex2f(-0.35, -0.1)
    glVertex2f(-0.15, -0.1)
    glVertex2f(-0.15, 0.1)
    glVertex2f(-0.35, 0.1)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.6 + brillo * 0.4, 0.8, 1.0)  # ventana derecha
    glVertex2f(0.15, -0.1)
    glVertex2f(0.35, -0.1)
    glVertex2f(0.35, 0.1)
    glVertex2f(0.15, 0.1)
    glEnd()

    # Molino base
    glBegin(GL_QUADS)
    glColor3f(0.7, 0.7, 0.7)
    glVertex2f(-0.75, -0.5)
    glVertex2f(-0.65, -0.5)
    glVertex2f(-0.65, 0.0)
    glVertex2f(-0.75, 0.0)
    glEnd()

    # Aspas del molino
    glPushMatrix()
    glTranslatef(-0.7, 0.0, 0)  # centro de rotación
    glRotatef(angulo_aspas, 0, 0, 1)
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex2f(-0.02, 0)
    glVertex2f(0.02, 0)
    glVertex2f(0.02, 0.4)
    glVertex2f(-0.02, 0.4)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-0.02, 0)
    glVertex2f(0.02, 0)
    glVertex2f(0.02, -0.4)
    glVertex2f(-0.02, -0.4)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(0, -0.02)
    glVertex2f(0.4, -0.02)
    glVertex2f(0.4, 0.02)
    glVertex2f(0, 0.02)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(0, -0.02)
    glVertex2f(-0.4, -0.02)
    glVertex2f(-0.4, 0.02)
    glVertex2f(0, 0.02)
    glEnd()
    glPopMatrix()

    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()

