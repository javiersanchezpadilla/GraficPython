import glfw
from OpenGL.GL import *
from math import cos, sin, pi


radio = 0.6
puntos_a_dibujar = 5
punto_circulo = 1

def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Mi primera ventana como funcion en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


# def rotar_punto():
#     """
#     La funcion `rotar_punto` rota un punto alrededor de un circulo y lo dibuja usando OpenGL.
#     """
    
#     global punto_circulo
#     punto_circulo += 1

#     angulo = (punto_circulo / puntos_a_dibujar) * 2 * 3.141592653589793
#     # Ecuación paramétrica
#     x = radio * cos(angulo)
#     y = radio * sin(angulo)
#     glPointSize(3)          # Tamaño del punto

#     # Dibuja un punto en las coordenadas (x, y)
#     glBegin(GL_POINTS)
#     glVertex2f(x, y)
#     glEnd()

def rotar_punto(x, y, p_x, p_y, angulo_grados):
    """
    Rota un punto (x, y) alrededor de un pivote (p_x, p_y) por un ángulo.
    """
    # 1. Convertir el ángulo a radianes
    angulo_rad = math.radians(angulo_grados)
    
    # 2. Trasladar al origen
    x_t = x - p_x
    y_t = y - p_y
    
    # 3. Rotar
    x_rot = x_t * math.cos(angulo_rad) - y_t * math.sin(angulo_rad)
    y_rot = x_t * math.sin(angulo_rad) + y_t * math.cos(angulo_rad)
    
    # 4. Trasladar de vuelta
    x_final = x_rot + p_x
    y_final = y_rot + p_y
    
    return (x_final, y_final)


def dibujar_punto(x, y):
    """
    Dibuja un punto en las coordenadas (x, y) usando OpenGL.
    """
    # Ejemplo con tus valores
    punto_original = (0.5, 0.5)
    pivote = (0.3, 0.3)
    angulo = 90

    nuevo_punto = rotar_punto(punto_original[0], punto_original[1], pivote[0], pivote[1], angulo)

    print(f"Punto original: {punto_original}")
    print(f"Pivote: {pivote}")
    # El resultado será (1.0, 5.0) con posibles decimales por la precisión de float
    print(f"Punto rotado {angulo} grados: {nuevo_punto}")

    glPointSize(3)          # Tamaño del punto
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()



if __name__ == "__main__":
    ventana = iniciar_ventana()
    glClearColor(0.0, 0.0, 0.0, 1.0)    # Limpia la pantalla
    glClear(GL_COLOR_BUFFER_BIT)    
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)    # Limpia la pantalla
        glClear(GL_COLOR_BUFFER_BIT)    
        rotar_punto()         
        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()
