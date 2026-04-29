""" RELLENO DE POLIGONOS.

    Para lograr que los colores cambien o brillen con el tiempo, vamos a 
    utilizar la función 
    
            glfw.get_time().

    Esta función nos devuelve el tiempo que ha pasado desde que inició el 
    programa. Si metemos ese número dentro de una función matemática como 
    el Seno (math.sin), obtendremos un valor que sube y baja suavemente 
    entre -1 y 1, ideal para crear un efecto de 'pulsación' o brillo.

    ¿Qué es lo que hace que brille?
    glfw.get_time(): Actúa como nuestro reloj. Cada vez que el bucle se repite, 
                     este número es un poco más grande.

    math.sin(tiempo):Esta función crea una onda. Imagina una montaña rusa que 
                     sube y baja. Eso hace que el color no cambie de golpe, 
                     sino de forma fluida.

    Ajuste del brillo:Como sin (seno) nos da valores negativos y los colores 
                     en OpenGL van de 0 a 1, le sumamos 1 y dividimos entre 2 
                     para que el resultado siempre esté en el rango correcto.
"""
import glfw
from OpenGL.GL import *
import math # Necesario para usar la función seno

def dibujar_cuadrado_animado():
    # Obtenemos el tiempo actual
    tiempo = glfw.get_time()
    
    # Calculamos un valor que oscila entre 0 y 1 para el brillo
    # math.sin devuelve valores entre -1 y 1, por eso lo ajustamos
    brillo = (math.sin(tiempo) + 1) / 2
    
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
    
    # Esquina 4: Amarillo (Mezcla de rojo y verde) que brilla
    glColor3f(brillo, brillo, 0) 
    glVertex2f(-0.5, 0.5)
    
    glEnd()

def main():
    if not glfw.init(): return
    ventana = glfw.create_window(600, 600, "Cuadrado con Brillo Animado", None, None)
    glfw.make_context_current(ventana)

    while not glfw.window_should_close(ventana):
        # Fondo oscuro para que el brillo se note más
        glClearColor(0.05, 0.05, 0.05, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        dibujar_cuadrado_animado()
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()