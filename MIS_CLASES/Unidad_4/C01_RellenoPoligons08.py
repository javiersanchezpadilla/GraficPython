""" RELLENO DE POLIGONOS (METODO DE INUNDACIÓN).

    ¿CÓMO FUNCIONA?

    1)  Punto de partida: Se selecciona un punto inicial dentro del polígono 
        que se desea rellenar.
    2)  Comprobación de vecinos: Se examinan los píxeles adyacentes al punto 
        inicial (arriba, abajo, izquierda, derecha).
    3)  Relleno: Si un píxel adyacente está dentro del polígono y aún no ha sido 
        coloreado, se le asigna el color de relleno y se añade a una lista de 
        píxeles a procesar.
    4)  Iteración: Se repite el paso 3 para cada píxel de la lista hasta que no 
        queden más píxeles por procesar.

defd rellena (int x, int y, int color)
    # Si el pixel es negro hay que pintar y seguir la ruta
    if (glReadPixels (x,y) == 0):
        rellena( x, y+1, color)   # Rellena al norte
        rellena( x+1, y, color)   # Rellena al este
        rellena( x, y-1, color)   # Rellena al sur
        rellena( x-1, y, color)   # Rellena al oeste


    1)  Dibujaremos un polígono irregular (usando líneas blancas).
    2)  Detectaremos un clic del ratón.
    3)  Ese clic será la 'semilla' que iniciará el algoritmo de Inundación 
        (Flood Fill).
    4)  Usaremos glReadPixels para saber si el píxel es negro (fondo) o blanco 
        (borde).

"""
import glfw
from OpenGL.GL import *
import sys

# Aumentamos el límite de recursión de Python para que el algoritmo
# no se detenga en polígonos un poco más grandes.
sys.setrecursionlimit(20000)

ANCHO, ALTO = 400, 400

def dibujar_poligono_irregular():
    """Dibuja un polígono irregular con líneas blancas."""
    glColor3f(1.0, 1.0, 1.0) # Blanco
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 100)
    glVertex2f(250, 80)
    glVertex2f(300, 200)
    glVertex2f(220, 320)
    glVertex2f(120, 250)
    glVertex2f(80, 180)
    glEnd()

def flood_fill(x, y, color_objetivo, color_nuevo):
    """
    Algoritmo de inundación que lee los píxeles de la pantalla.
    color_objetivo: El color que queremos rellenar (Negro [0,0,0]).
    color_nuevo: El color con el que pintamos (Rojo [255,0,0]).
    """
    # 1. Leer el color del píxel actual (x, y)
    pixel = glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE)
    r, g, b = list(pixel)

    # 2. Si el color es el de fondo (objetivo) y no es el color nuevo
    if (r, g, b) == color_objetivo:
        # 3. Pintar el píxel de color nuevo
        # Usamos coordenadas de dibujo (la ventana es de 400x400)
        # Convertimos coordenadas de píxel a coordenadas de dibujo
        glColor3ub(color_nuevo[0], color_nuevo[1], color_nuevo[2])
        glBegin(GL_POINTS)
        glVertex2i(x, y)
        glEnd()
        
        # Forzar a OpenGL a dibujar el punto inmediatamente para ver el progreso
        # (Aunque esto lo hace más lento, ayuda a entender el proceso)
        # glFlush() 

        # 4. Recursión en 4 direcciones (Vecinos)
        flood_fill(x + 1, y, color_objetivo, color_nuevo)
        flood_fill(x - 1, y, color_objetivo, color_nuevo)
        flood_fill(x, y + 1, color_objetivo, color_nuevo)
        flood_fill(x, y - 1, color_objetivo, color_nuevo)

def mouse_button_callback(window, button, action, mods):
    """Detecta el clic para iniciar el relleno."""
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        x, y = glfw.get_cursor_pos(window)
        
        # IMPORTANTE: Invertir el eje Y (GLFW usa 0 arriba, OpenGL usa 0 abajo)
        y_real = ALTO - int(y)
        x_real = int(x)
        
        print(f"Iniciando relleno en: {x_real}, {y_real}")
        
        # Llamamos al algoritmo: 
        # Objetivo: Negro (0,0,0), Nuevo: Rojo (255,0,0)
        flood_fill(x_real, y_real, (0, 0, 0), (255, 0, 0))
        
        # Mostramos el resultado final
        glfw.swap_buffers(window)

def main():
    if not glfw.init(): return

    window = glfw.create_window(ANCHO, ALTO, "Clic dentro para Rellenar", None, None)
    glfw.make_context_current(window)
    
    # Configurar proyección ortográfica (para trabajar con píxeles 1 a 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, ANCHO, 0, ALTO, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    
    # Configurar el evento del ratón
    glfw.set_mouse_button_callback(window, mouse_button_callback)

    while not glfw.window_should_close(window):
        # No limpiamos la pantalla cada vez (glClear) porque borraríamos el relleno
        # Dibujamos el polígono solo una vez o lo mantenemos
        dibujar_poligono_irregular()
        
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
