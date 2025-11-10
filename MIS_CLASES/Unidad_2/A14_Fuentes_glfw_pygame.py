import glfw
from OpenGL.GL import *
import pygame
import sys
import numpy as np

# --- 1. Configuración de Variables Globales ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TEXTO_ACTUAL = "¡Hola OpenGL con Pygame!"
TEXTO_X = 50
TEXTO_Y = 50

# Almacenará el ID de la textura que crearemos a partir del texto de Pygame
textura_texto_id = 0
ancho_texto = 0
alto_texto = 0

# --- 2. Funciones de Ayuda ---

def crear_textura_desde_texto(texto, color=(255, 255, 255), tamano=48):
    """
    Usa Pygame para renderizar texto en una superficie y lo convierte
    en una textura de OpenGL (la 'Goma del Sello').
    Retorna (textureID, ancho, alto) de la textura creada.
    """
    global textura_texto_id, ancho_texto, alto_texto

    # 1. Preparar Pygame Font y Surface
    # Intentamos cargar una fuente de sistema común
    try:
        fuente = pygame.font.SysFont('arial', tamano, bold=True)
    except:
        fuente = pygame.font.Font(None, tamano)
        
    # Renderizamos el texto. El True es para antialiasing.
    superficie_texto = fuente.render(texto, True, color) 
    # Convertir con Alpha (transparencia) es crucial para que el fondo sea transparente
    superficie_texto = superficie_texto.convert_alpha()

    ancho_texto = superficie_texto.get_width()
    alto_texto = superficie_texto.get_height()
    
    # 2. Obtener los datos de la imagen
    # 'RGBA': decimos a Pygame que nos dé los datos en el formato que OpenGL necesita
    datos_texto = pygame.image.tostring(superficie_texto, "RGBA", True)

    # 3. Crear Textura de OpenGL (La Textura del Chef)
    # Si ya existe una textura, la reutilizamos
    if textura_texto_id == 0:
        textura_texto_id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, textura_texto_id)
    
    # Configuramos filtros para que se vea bien al estirar o encoger
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    # Enviar los datos de Pygame a OpenGL
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ancho_texto, alto_texto, 
                 0, GL_RGBA, GL_UNSIGNED_BYTE, datos_texto)

    glBindTexture(GL_TEXTURE_2D, 0) # Desvincular la textura

    return textura_texto_id, ancho_texto, alto_texto


def dibujar_textura_2D(texture_id, x, y, w, h):
    """
    Dibuja un Quad 2D con la textura del texto aplicado (El 'Constructor').
    """
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    # Configuración de mezcla para la transparencia (crucial para que el texto se vea bien)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    # Vinculamos nuestra textura de texto
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # Empezar a dibujar el cuadrado (Quad)
    glBegin(GL_QUADS)
    
    # Coordenadas de texturizado (UVs) para que la imagen cubra todo el Quad.
    # Coordenadas de la pantalla (x, y)
    
    # Esquina inferior izquierda
    glTexCoord2f(0.0, 1.0) 
    glVertex2f(x, y)
    
    # Esquina inferior derecha
    glTexCoord2f(1.0, 1.0) 
    glVertex2f(x + w, y)
    
    # Esquina superior derecha
    glTexCoord2f(1.0, 0.0)
    glVertex2f(x + w, y + h)
    
    # Esquina superior izquierda
    glTexCoord2f(0.0, 0.0) 
    glVertex2f(x, y + h)
    
    glEnd()
    
    # Limpieza
    glDisable(GL_BLEND)
    glDisable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, 0)


def configurar_vista_2D(ancho, alto):
    """
    Configura la matriz de proyección para dibujar en 2D (ortográfico).
    Establece (0, 0) en la esquina inferior izquierda.
    """
    glViewport(0, 0, ancho, alto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Definir una proyección 2D: (izquierda, derecha, abajo, arriba, cerca, lejos)
    glOrtho(0.0, ancho, 0.0, alto, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# --- 3. Inicialización de Librerías ---

def inicializar_pygame():
    """Inicializa Pygame, solo la parte de fuentes."""
    try:
        pygame.init()
        # Solo necesitamos el módulo de fuentes
        pygame.font.init()
        print("Pygame Fonts inicializado correctamente.")
    except Exception as e:
        print(f"Error al inicializar Pygame: {e}")
        sys.exit(1)


def inicializar_glfw():
    """Inicializa GLFW y crea la ventana."""
    if not glfw.init():
        print("Error: No se pudo inicializar GLFW.")
        sys.exit(1)

    window = glfw.create_window(ANCHO_VENTANA, ALTO_VENTANA, "Texto Sencillo en GLFW con Pygame", None, None)
    
    if not window:
        glfw.terminate()
        print("Error: No se pudo crear la ventana de GLFW.")
        sys.exit(1)

    glfw.make_context_current(window)
    return window

# --- 4. Bucle Principal ---

def main():
    
    # 1. Inicializar
    inicializar_pygame()
    window = inicializar_glfw()
    
    # 2. Generar la textura del texto una sola vez (si no cambia)
    global textura_texto_id, ancho_texto, alto_texto
    textura_texto_id, ancho_texto, alto_texto = crear_textura_desde_texto(
        TEXTO_ACTUAL, 
        color=(0, 255, 0), # Color verde brillante
        tamano=50
    )

    # 3. Bucle de Renderizado
    while not glfw.window_should_close(window):
        
        # Procesar eventos de entrada (movimientos del mouse, teclado)
        glfw.poll_events()
        
        # Limpiar la pantalla
        glClearColor(0.2, 0.3, 0.3, 1.0) # Fondo oscuro
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Cambiar a modo 2D (Ortográfico) para dibujar el texto
        configurar_vista_2D(ANCHO_VENTANA, ALTO_VENTANA)
        
        # --- Dibujar Texto (El paso más importante) ---
        # La posición Y se ajusta para que el (TEXTO_Y) sea el borde inferior,
        # ya que la vista 2D comienza en la parte inferior izquierda.
        dibujar_textura_2D(
            textura_texto_id, 
            TEXTO_X, 
            ALTO_VENTANA - TEXTO_Y - alto_texto, # Ajuste a la esquina superior (Pygame usa arriba/izquierda)
            ancho_texto, 
            alto_texto
        )
        
        # ----------------------------------------------
        
        # Intercambiar buffers (mostrar lo que se dibujó)
        glfw.swap_buffers(window)

    # 4. Limpieza
    glfw.terminate()
    pygame.quit()

if __name__ == "__main__":
    main()