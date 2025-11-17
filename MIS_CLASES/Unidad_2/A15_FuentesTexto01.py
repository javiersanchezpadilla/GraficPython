import glfw
from OpenGL.GL import *
import numpy as np

# --- 1. Definición de la Fuente (Mapas de Bits para Caracteres) ---

# Cada byte (0x) representa 8 píxeles horizontalmente. 
# La fuente es de 8 píxeles de ancho y 8 de alto.
# Los datos deben ser numpy.ubyte para glBitmap.

# H (8x8)
# Se lee de abajo hacia arriba en el array, pero de izquierda a derecha en cada byte.
char_H = np.array([
    0x00, 0x00, 
    0x88, 0x88, 
    0x88, 0x88, 
    0xFF, 0x88, 
    0x88, 0x88, 
    0x88, 0x88, 
    0x00, 0x00
], dtype=np.ubyte)

# E (8x8)
char_E = np.array([
    0x00, 0x00, 
    0xFF, 0x80, 
    0x80, 0x80, 
    0xF8, 0x80, 
    0x80, 0x80, 
    0xFF, 0x80, 
    0x00, 0x00
], dtype=np.ubyte)

# L (8x8)
char_L = np.array([
    0x00, 0x00, 
    0x80, 0x80, 
    0x80, 0x80, 
    0x80, 0x80, 
    0x80, 0x80, 
    0xFF, 0x80, 
    0x00, 0x00
], dtype=np.ubyte)

# O (8x8)
char_O = np.array([
    0x00, 0x00, 
    0x70, 0x88, 
    0x88, 0x88, 
    0x88, 0x88, 
    0x88, 0x88, 
    0x70, 0x00, 
    0x00, 0x00
], dtype=np.ubyte)

# Espacio (no dibuja nada, pero avanza la posición)
char_space = np.array([0x00], dtype=np.ubyte) 


# Diccionario para mapear caracteres a sus datos y dimensiones
font_map = {
    'H': (char_H, 8),
    'E': (char_E, 8),
    'L': (char_L, 8),
    'O': (char_O, 8),
    ' ': (char_space, 8) # El ancho de la letra L se usa como avance
}


def draw_text_bitmap(text, start_x, start_y, char_width=8, char_height=8):
    """
    Dibuja una cadena de texto usando glBitmap en la posición de píxel (start_x, start_y).
    """
    glColor3f(1.0, 1.0, 1.0) # Color del texto: Blanco
    
    # 1. Establecer la posición inicial de trama
    glRasterPos2i(start_x, start_y)
    
    # Parámetros de movimiento: 
    # x_advance (avanza al siguiente carácter)
    # y_advance (generalmente 0 para texto horizontal)
    x_advance = char_width + 2 # Ancho de la letra + 2 píxeles de espacio

    for char in text.upper():
        if char in font_map:
            bitmap_data, width = font_map[char]
            
            # El movimiento del cursor (raster position) es clave:
            # - Dibuja el carácter
            # - Mueve la posición de trama para el siguiente glBitmap
            glBitmap(
                width,              # Ancho del carácter (8 píxeles)
                char_height,        # Alto del carácter (8 píxeles)
                0.0, 0.0,           # Origen (usamos la esquina inferior izquierda del bitmap)
                x_advance, 0.0,     # Mover la posición X para el siguiente carácter
                bitmap_data         # Los datos binarios
            )
        else:
            # Si el carácter no está mapeado, solo avanza la posición para no romper el texto
            glBitmap(0, 0, 0.0, 0.0, x_advance, 0.0, None)


def iniciar_ventana():
    # ... (Inicialización y creación de ventana - Código omitido para brevedad) ...
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Texto con glBitmap", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana

def configurar_coordenadas_ventana(ancho, alto):
    """Configura la proyección para usar coordenadas de píxeles (ventana)."""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, ancho, 0.0, alto, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    ventana_ancho = 800
    ventana_alto = 600
    ventana = iniciar_ventana()

    configurar_coordenadas_ventana(ventana_ancho, ventana_alto)
    
    # Activamos la fusión (blending) para manejar la transparencia (aunque en bitmap es binario, es buena práctica)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glClearColor(0.1, 0.1, 0.2, 1.0)
    
    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # --- Llama a la función de dibujo de texto ---
        # Posicionamos el texto en las coordenadas de píxel (50, 500)
        draw_text_bitmap("HOLA", 50, 500)
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()