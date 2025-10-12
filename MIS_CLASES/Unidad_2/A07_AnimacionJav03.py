""" Animación de cuadros que rebotan y colisionan entre sí
    Esta version del programa solo cambio el sentido de movimiento de los cuadros
    cuando colisionan entre sí, y cuando chocan en los bordes de la ventana.
    Esta version trata de respetar los sentidos de rebote entre los cuadros."""

import glfw
from OpenGL.GL import *
import random

# --- Constantes y Resolución ---
MAX_TAMANIO = 50
MAX_VELOCIDAD = 4
RES_X = 800
RES_Y = 600
TOTAL_CUADROS = 10

# --- Estructura de Datos (Clase en Python) ---
class Cuadro:
    vertice = [(0, 0)] * 4  # Lista de 4 tuplas para vértices [(0,0)]*4 = [(0,0)],(0,0),(0,0),(0,0)]
    tamanio = 0             # Tamaño del cuadro (ancho y alto, ya que es cuadrado)
    factorX = 0             # Velocidad en X
    factorY = 0             # Velocidad en Y
    rojo = 0.0              # Componente roja del color
    verde = 0.0             # Componente verde del color
    azul = 0.0              # Componente azul del color

# Inicializa la lista de objetos inicializa de 0 a TOTAL_CUADROS-1 
cuadrito = [Cuadro() for _ in range(TOTAL_CUADROS)]


def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(RES_X, RES_Y, "Mi primera ventana como funcion en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


def proyeccion():
    """ Esta función configura la matriz de proyección para definir el espacio de coordenadas
        que vamos a utilizar para dibujar en la ventana.
        No retorna ningún valor, solo configura el estado de OpenGL.
        La función establece un sistema de coordenadas 2D donde el origen (0,0) está en la esquina
        inferior izquierda, el eje X va de 0 a 200 y el eje Y va de 0 a 150.
        Esto significa que cualquier cosa que dibujemos usando estas coordenadas se ajustará a este
        rango dentro de la ventana.
    """
    # Indicamos que vamos a trabajar en la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    # Limpiamos cualquier configuración anterior
    glLoadIdentity()
    # Establecemos el espacio de coordenadas de 0 a 200 en X y 0 a 150 en Y
    glOrtho(0.0, float(RES_X), 0.0, float(RES_Y), -1.0, 1.0) 
    # Volvemos a la matriz de modelo-vista para dibujar
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



def CreaCuadros():
    """ Esta función inicializa los atributos de cada cuadro en la lista `cuadrito`.
        No retorna ningún valor, solo modifica los objetos en la lista `cuadrito`.
        Cada cuadro recibe un tamaño, posición inicial, velocidad y color aleatorios.
    """
    # random.seed() # Reinicializa el generador de números aleatorios
    for b in range(TOTAL_CUADROS):
        # Genera tamaño aleatorio
        cuadrito[b].tamanio = random.randint(1, MAX_TAMANIO)
        # Calcula la posición inicial del vértice superior izquierdo (PosIni)
        tam = cuadrito[b].tamanio
        # Asegura que el cuadro inicie dentro de la pantalla
        pos_x = random.randint(1, RES_X - tam - 2)
        pos_y = random.randint(tam + 1, RES_Y - 1) # Arriba de 0 + tamaño y abajo de RES_Y
        # Define los 4 vértices del cuadro
        cuadrito[b].vertice = [
            (pos_x, pos_y),              # Vértice 0: Esq. Sup. Izq. (x, y)      v0  +---+  v1
            (pos_x + tam, pos_y),        # Vértice 1: Esq. Sup. Der. (x+t, y)        |   |
            (pos_x + tam, pos_y - tam),  # Vértice 2: Esq. Inf. Der. (x+t, y-t)      |   |
            (pos_x, pos_y - tam)         # Vértice 3: Esq. Inf. Izq. (x, y-t)    v3  +---+  v2
        ]
        # Factores de velocidad
        cuadrito[b].factorX = random.randint(1, MAX_VELOCIDAD)
        cuadrito[b].factorY = random.randint(1, MAX_VELOCIDAD)
        # Colores aleatorios
        cuadrito[b].rojo = random.uniform(0.0, 1.0)
        cuadrito[b].verde = random.uniform(0.0, 1.0)
        cuadrito[b].azul = random.uniform(0.0, 1.0)


def dibuja_cuadros():
    """ Esta función dibuja todos los cuadros en sus posiciones actuales.
        No retorna ningún valor, solo realiza operaciones de dibujo en OpenGL."""
    for b in range(TOTAL_CUADROS):
        glColor3f(cuadrito[b].rojo, cuadrito[b].verde, cuadrito[b].azul)
        glBegin(GL_POLYGON)
        # por cada vértice (x,y) en la lista de vértices del cuadro
        for x, y in cuadrito[b].vertice:    
            glVertex2i(int(x), int(y))
        glEnd()



   # 3. Mueve todos los cuadros
def mueve_cuadros(que_cuadrito):
    """ Esta función actualiza las posiciones de todos los cuadros según sus factores de velocidad.
        No retorna ningún valor, solo modifica los atributos de los cuadros en la lista `cuadrito`.
    """
    nuevos_vertices = []
    for x, y in cuadrito[que_cuadrito].vertice:
        nueva_x = x + cuadrito[que_cuadrito].factorX
        nueva_y = y + cuadrito[que_cuadrito].factorY
        nuevos_vertices.append((nueva_x, nueva_y))
    cuadrito[que_cuadrito].vertice = nuevos_vertices



def ChecaColisiones():
    """ Esta función verifica y maneja las colisiones entre los cuadros.
        No retorna ningún valor, solo modifica los atributos de los cuadros en la lista `cuadrito`.
        Si dos cuadros colisionan, invierte sus direcciones de movimiento.
    """
    for b in range(TOTAL_CUADROS):
        # Calcula el centro del cuadro actual
        # Vértice[0] es (x, y_max), Vértice[3] es (x, y_min)
        x0, y0 = cuadrito[b].vertice[0]
        x3, y3 = cuadrito[b].vertice[3]
        centro_cuadro_x = x0 + cuadrito[b].tamanio / 2
        centro_cuadro_y = y3 + cuadrito[b].tamanio / 2
        for c in range(TOTAL_CUADROS):
            # quiere decir que no se compare consigo mismo
            if c != b:
                # Calcula el centro del otro cuadro
                xc, yc = cuadrito[c].vertice[0]
                xz, yz = cuadrito[c].vertice[3]
                centro_otro_x = xc + cuadrito[c].tamanio / 2
                centro_otro_y = yz + cuadrito[c].tamanio / 2
                # Cálculo de distancias
                distX = abs(centro_cuadro_x - centro_otro_x)
                distY = abs(centro_cuadro_y - centro_otro_y)
                distancia_zero = (cuadrito[b].tamanio + cuadrito[c].tamanio) / 2
                # El criterio de colisión es: si la distancia entre centros
                # es menor o igual a la suma de la mitad de sus tamaños.
                if distX <= distancia_zero and distY <= distancia_zero:
                    fx_b = cuadrito[b].factorX
                    fy_b = cuadrito[b].factorY
                    fx_c = cuadrito[c].factorX
                    fy_c = cuadrito[c].factorY
                    if (fx_b + fy_b + fx_c + fy_c) == 0:    # Van en direcciones opuestas
                        cuadrito[b].factorX *= -1
                        cuadrito[b].factorY *= -1
                        cuadrito[c].factorX *= -1
                        cuadrito[c].factorY *= -1
                    elif fy_b == fy_c:
                        cuadrito[b].factorX *= -1
                        cuadrito[c].factorX *= -1
                    else: #fx_b == fx_c:
                        cuadrito[b].factorY *= -1
                        cuadrito[c].factorY *= -1

                    mueve_cuadros(b)
                    mueve_cuadros(c)



def dibujar_y_animar():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW) # Asegura estar en el modo de modelo
    glLoadIdentity() # No necesitamos transformaciones de matriz complejas aquí, solo dibujamos en coordenadas absolutas

    # 1. Actualiza los límites (rebote en las paredes)
    for b in range(TOTAL_CUADROS):
        # Vértices del cuadro:
        x_min = cuadrito[b].vertice[3][0] # x de la esq. inf. izq.
        x_max = cuadrito[b].vertice[1][0] # x de la esq. sup. der.
        y_min = cuadrito[b].vertice[3][1] # y de la esq. inf. izq.
        y_max = cuadrito[b].vertice[0][1] # y de la esq. sup. izq.

        if x_min <= 0 or x_max >= RES_X:
            cuadrito[b].factorX *= -1
        if y_min <= 0 or y_max >= RES_Y:
            cuadrito[b].factorY *= -1

    # 2. Chequea colisiones entre cuadros
    ChecaColisiones()   

    # 3. Mueve todos los cuadros
    for b in range(TOTAL_CUADROS):
        mueve_cuadros(b)
        
    # 4. Dibuja los cuadros
    dibuja_cuadros()    
    # En GLFW, el swap_buffers va en el bucle principal (ver abajo)



# El bucle principal de trabajo
# Asignamos a la variable ventana el valor retornado por la función iniciar_ventana
ventana = iniciar_ventana()
proyeccion()
CreaCuadros()
while not glfw.window_should_close(ventana):
    # Limpiamos la pantalla
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    dibujar_y_animar()
    # Refresca la pantalla
    # Intercambia las dos caras del lienzo para mostrar lo que hemos dibujado
    glfw.swap_buffers(ventana)
    glfw.poll_events()

# Terminamos el programa y cerramos todo
glfw.terminate()
