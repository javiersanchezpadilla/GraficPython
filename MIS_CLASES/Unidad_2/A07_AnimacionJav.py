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
import sys # Para sys.exit

# --- Constantes y Resolución ---
MAX_TAMANIO = 50
MAX_VELOCIDAD = 4
RES_X = 800
RES_Y = 600
TOTAL_CUADROS = 15

# --- Estructura de Datos (Clase en Python) ---
class Cuadro:
    # Usaremos una lista de 4 tuplas para los vértices
    vertice = [(0, 0)] * 4
    tamanio = 0
    factorX = 0
    factorY = 0
    rojo = 0.0
    verde = 0.0
    azul = 0.0

# Inicializa la lista de objetos inicializa de 0 a TOTAL_CUADROS-1 (15-1 = 14)
objeto = [Cuadro() for _ in range(TOTAL_CUADROS)]


def Inicializa():
    # Establece el color de la ventana de fondo
    glClearColor(0.1, 0.3, 0.4, 0.0)


# Función de redimensionamiento (similar a lo que haría gluOrtho2D en Init)
def framebuffer_size_callback(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Define la proyección ortogonal para que las coordenadas (0,0) a (800,600) se vean bien.
    # Nota: glOrtho es el equivalente directo en OpenGL de gluOrtho2D
    glOrtho(0.0, RES_X, 0.0, RES_Y, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW) # Siempre volvemos al modo de modelo


def CreaCuadros():
    random.seed() # Reinicializa el generador de números aleatorios

    for b in range(TOTAL_CUADROS):
        # Genera tamaño aleatorio
        objeto[b].tamanio = random.randint(1, MAX_TAMANIO)

        # Calcula la posición inicial del vértice superior izquierdo (PosIni)
        tam = objeto[b].tamanio
        # Asegura que el cuadro inicie dentro de la pantalla
        pos_x = random.randint(1, RES_X - tam - 2)
        pos_y = random.randint(tam + 1, RES_Y - 1) # Arriba de 0 + tamaño y abajo de RES_Y

        # Define los 4 vértices del cuadro
        # Nota: En C++ usaste un sistema donde el y positivo es ARRIBA. Mantendremos eso.
        objeto[b].vertice = [
            (pos_x, pos_y),              # Vértice 0: Esq. Sup. Izq. (x, y)
            (pos_x + tam, pos_y),        # Vértice 1: Esq. Sup. Der. (x+t, y)
            (pos_x + tam, pos_y - tam),  # Vértice 2: Esq. Inf. Der. (x+t, y-t)
            (pos_x, pos_y - tam)         # Vértice 3: Esq. Inf. Izq. (x, y-t)
        ]

        # Factores de velocidad
        objeto[b].factorX = random.randint(1, MAX_VELOCIDAD)
        objeto[b].factorY = random.randint(1, MAX_VELOCIDAD)

        # Colores aleatorios
        objeto[b].rojo = random.uniform(0.0, 1.0)
        objeto[b].verde = random.uniform(0.0, 1.0)
        objeto[b].azul = random.uniform(0.0, 1.0)

def ChecaColisiones():
    for b in range(TOTAL_CUADROS):
        # Calcula el centro del cuadro actual
        # Vértice[0] es (x, y_max), Vértice[3] es (x, y_min)
        x0, y0 = objeto[b].vertice[0]
        x3, y3 = objeto[b].vertice[3]
        
        centro_cuadro_x = x0 + objeto[b].tamanio / 2
        centro_cuadro_y = y3 + objeto[b].tamanio / 2

        for c in range(TOTAL_CUADROS):
            if c != b:
                # Calcula el centro del otro cuadro
                xc, yc = objeto[c].vertice[0]
                xz, yz = objeto[c].vertice[3]
                
                centro_otro_x = xc + objeto[c].tamanio / 2
                centro_otro_y = yz + objeto[c].tamanio / 2
                
                # Cálculo de distancias
                distX = abs(centro_cuadro_x - centro_otro_x)
                distY = abs(centro_cuadro_y - centro_otro_y)
                
                distancia_zero = (objeto[b].tamanio + objeto[c].tamanio) / 2
                
                # El criterio de colisión es: si la distancia entre centros
                # es menor o igual a la suma de la mitad de sus tamaños.
                if distX <= distancia_zero and distY <= distancia_zero:
                    # Invierte la dirección de AMBOS cuadros
                    objeto[b].factorX *= -1
                    objeto[b].factorY *= -1
                    objeto[c].factorX *= -1
                    objeto[c].factorY *= -1

# La función de dibujo principal (antes Animacion en C++)
def dibujar_y_animar():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW) # Asegura estar en el modo de modelo
    glLoadIdentity() # No necesitamos transformaciones de matriz complejas aquí, solo dibujamos en coordenadas absolutas

    # 1. Dibuja los cuadros
    for b in range(TOTAL_CUADROS):
        glColor3f(objeto[b].rojo, objeto[b].verde, objeto[b].azul)
        glBegin(GL_POLYGON)
        for x, y in objeto[b].vertice:
            # Usamos glVertex2i como en C++
            glVertex2i(int(x), int(y))
        glEnd()

    # 2. Actualiza los límites (rebote en las paredes)
    for b in range(TOTAL_CUADROS):
        # Vértices del cuadro:
        x_min = objeto[b].vertice[3][0] # x de la esq. inf. izq.
        x_max = objeto[b].vertice[1][0] # x de la esq. sup. der.
        y_min = objeto[b].vertice[3][1] # y de la esq. inf. izq.
        y_max = objeto[b].vertice[0][1] # y de la esq. sup. izq.

        if x_min <= 0 or x_max >= RES_X:
            objeto[b].factorX *= -1
        if y_min <= 0 or y_max >= RES_Y:
            objeto[b].factorY *= -1

    # 3. Mueve todos los cuadros
    for b in range(TOTAL_CUADROS):
        nuevos_vertices = []
        for x, y in objeto[b].vertice:
            nueva_x = x + objeto[b].factorX
            nueva_y = y + objeto[b].factorY
            nuevos_vertices.append((nueva_x, nueva_y))
        objeto[b].vertice = nuevos_vertices

    # 4. Chequea colisiones entre cuadros
    ChecaColisiones()
    
    # En GLFW, el swap_buffers va en el bucle principal (ver abajo)


def main():
    # --- Inicialización de GLFW ---
    if not glfw.init():
        sys.exit()

    # --- Creación de la Ventana ---
    window = glfw.create_window(RES_X, RES_Y, "Cuadros Rebotantes (Python/GLFW)", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    # Asigna la función de redimensionamiento para manejar la proyección
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)

    # --- Inicialización del programa ---
    CreaCuadros() # Crea los datos de los cuadros
    Inicializa()  # Configura el color de fondo

    # Asegura que el viewport y la proyección se configuren al inicio
    # Llama manualmente a la función de redimensionamiento
    framebuffer_size_callback(window, RES_X, RES_Y) 
    
    # --- Bucle de Renderizado Principal (Reemplaza glutMainLoop) ---
    while not glfw.window_should_close(window):
        # Llama a la función de dibujo y animación
        dibujar_y_animar()

        # Intercambia los buffers (Reemplaza glutSwapBuffers)
        glfw.swap_buffers(window)
        
        # Procesa eventos (Reemplaza la necesidad de glutPostRedisplay para la animación)
        glfw.poll_events()

    # --- Terminación ---
    glfw.terminate()

if __name__ == "__main__":
    main()


