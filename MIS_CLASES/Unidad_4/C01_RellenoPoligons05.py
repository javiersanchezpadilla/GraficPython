""" RELLENO DE POLIGONOS.

    para que el cuadrado no solo brille, sino que también rote sobre su propio
    eje.
    Para lograr esto, usaremos la función glRotatef(). Esta función toma tres 
    valores: el ángulo de rotación y el eje sobre el cual queremos girar 
    (X, Y o Z). Al usar el tiempo como ángulo, crearemos un movimiento fluido 
    y constante.

    Ya sabemos el manejo de las transformaciones mediante el usos de 
    glPushMatrix y glPopMatrix, que son como 'puntos de control' para que la 
    rotación solo afecte al cuadrado y no a todo lo que dibujes después. 
"""

import glfw
from OpenGL.GL import *
import math # Necesario para usar la función seno

def dibujar_cuadrado_animado():
    # Obtenemos el tiempo actual para las animaciones
    tiempo = glfw.get_time()
    
    # Calculamos un valor que oscila entre 0 y 1 para el brillo
    brillo = (math.sin(tiempo) + 1) / 2
    
    # --- EFECTO DE ROTACIÓN ---
    # glRotatef(ángulo, x, y, z)
    # Multiplicamos el tiempo por 50 para que la velocidad sea agradable
    glPushMatrix() # Guarda el estado actual de la matriz
    glRotatef(tiempo * 50, 0, 0, 1) # Rota sobre el eje Z (plano de la pantalla)
    
    glBegin(GL_QUADS)
    
    # Esquina 1: Rojo que brilla
    glColor3f(brillo, 0, 0) 
    glVertex2f(-0.5, -0.5)
    
    # Esquina 2: Verde que brilla
    glColor3f(0, brillo, 0) 
    glVertex2f(0.5, -0.5)
    
    # Esquina 3: Azul que brilla
    glColor3f(0, 0, brillo) 
    glVertex2f(0.5, 0.5)
    
    # Esquina 4: Amarillo que brilla
    glColor3f(brillo, brillo, 0) 
    glVertex2f(-0.5, 0.5)
    
    glEnd()
    glPopMatrix() # Restaura el estado de la matriz

def main():
    if not glfw.init(): return
    ventana = glfw.create_window(600, 600, "Cuadrado con Brillo y Rotación", None, None)
    glfw.make_context_current(ventana)

    while not glfw.window_should_close(ventana):
        # Fondo oscuro
        glClearColor(0.05, 0.05, 0.05, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Reiniciar la matriz de dibujo para que la rotación no se acumule infinitamente
        glLoadIdentity()
        
        dibujar_cuadrado_animado()
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
