""" En este ejercicio se dibujaran varios cuadros que se moveran en direcciones aleatorias.
    Cuando los cuadros colisionen entre si, rebotaran y cambiaran de direccion.
    Cada cuadro estara formado por cuatro vertices y tendra un color diferente.
    La implementacion utiliza Programación Orientada a Objetos (OOP) para manejar múltiples cuadros.
    Se define una clase `Cuadro` que encapsula los atributos y métodos relacionados con cada cuadro.
    Esto hace que el código sea más modular, reutilizable y fácil de entender.
    Pero ademas se utiliza una lista para almacenar multiples cuadros y se itera sobre ella para 
    actualizar y dibujar cada cuadro.
    De esta manera, se pueden manejar facilmente muchos cuadros sin necesidad de definir variables
    individuales para cada uno.
"""

import glfw
from OpenGL.GL import *
import random

class Cuadro:
    def __init__(self, pos, velocidad, tamanio, color):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.vel_x = velocidad[0]
        self.vel_y = velocidad[1]
        self.tamanio = tamanio
        self.color = color

    def dibujar(self):
        glBegin(GL_QUADS)
        glColor3f(self.color[0], self.color[1], self.color[2])
        
        x = self.pos_x
        y = self.pos_y
        tam = self.tamanio
        
        glVertex2f(x, y)
        glVertex2f(x + tam, y)
        glVertex2f(x + tam, y + tam)
        glVertex2f(x, y + tam)
        glEnd()

    def actualizar(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        
        # Rebotar en los bordes de la pantalla (eje x)
        if self.pos_x + self.tamanio >= 1.0 or self.pos_x <= -1.0:
            self.vel_x *= -1

        # Rebotar en los bordes de la pantalla (eje y)
        if self.pos_y + self.tamanio >= 1.0 or self.pos_y <= -1.0:
            self.vel_y *= -1

    def detectar_colision(self, otro_cuadro):
        # Bbox del cuadro 1
        x1_min, x1_max = self.pos_x, self.pos_x + self.tamanio
        y1_min, y1_max = self.pos_y, self.pos_y + self.tamanio

        # Bbox del cuadro 2
        x2_min, x2_max = otro_cuadro.pos_x, otro_cuadro.pos_x + otro_cuadro.tamanio
        y2_min, y2_max = otro_cuadro.pos_y, otro_cuadro.pos_y + otro_cuadro.tamanio

        # Detección de colisión entre rectángulos
        colisiona_x = (x1_min < x2_max and x1_max > x2_min)
        colisiona_y = (y1_min < y2_max and y1_max > y2_min)

        return colisiona_x and colisiona_y

def iniciar_ventana():
    # ... (código de inicialización de ventana, sin cambios) ...
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Lista de cuadros rebotando", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana

def programa_principal():
    ventana = iniciar_ventana()
    
    # Creamos una lista para almacenar los cuadros
    cuadros = []
    num_cuadros = 10
    
    for _ in range(num_cuadros):
        # Valores aleatorios para cada cuadro
        pos = (random.uniform(-0.9, 0.7), random.uniform(-0.9, 0.7))
        vel = (random.uniform(-0.005, 0.005), random.uniform(-0.005, 0.005))
        tam = random.uniform(0.1, 0.2)
        color = (random.random(), random.random(), random.random())
        
        nuevo_cuadro = Cuadro(pos, vel, tam, color)
        cuadros.append(nuevo_cuadro)
    
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        # 1. Actualizar la posición de todos los cuadros
        for cuadro in cuadros:
            cuadro.actualizar()
        
        # 2. Detectar y manejar colisiones entre todos los cuadros
        for i in range(len(cuadros)):
            for j in range(i + 1, len(cuadros)):
                cuadro1 = cuadros[i]
                cuadro2 = cuadros[j]
                
                if cuadro1.detectar_colision(cuadro2):
                    cuadro1.vel_x *= -1
                    cuadro1.vel_y *= -1
                    cuadro2.vel_x *= -1
                    cuadro2.vel_y *= -1
        
        # 3. Dibujar todos los cuadros
        for cuadro in cuadros:
            cuadro.dibujar()
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    programa_principal()