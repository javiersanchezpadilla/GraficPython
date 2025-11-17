import glfw
from OpenGL.GL import *
from PIL import Image, ImageDraw, ImageFont # Importamos las herramientas de Pillow
import numpy as np
import os # Para la ruta de la fuente

# --- 1. CONFIGURACIÓN ---
VENTANA_ANCHO = 800
VENTANA_ALTO = 600
TEXTO = "HOLA a todos en el Grupo"

# --- 2. FUNCIÓN CLAVE: CREAR Y CARGAR LA TEXTURA (Usando Pillow) ---
def cargar_textura_texto(text, font_size=40):
    """Crea una imagen del texto en la CPU y la carga a la GPU como textura."""
    
    # 2.1 Cargar una fuente: Intenta usar una fuente común del sistema
    # NOTA: En sistemas distintos, podrías necesitar cambiar 'arial.ttf' por otra ruta válida.
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        # Si la fuente no se encuentra, usa una por defecto de PIL
        font = ImageFont.load_default()
        
    # 2.2 Obtener el tamaño que ocupará el texto
    # (El método .getbbox() es el estándar para obtener dimensiones en PIL)
    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 2.3 Crear una imagen transparente (RGBA)
    img = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 2.4 Dibujar el texto en la imagen (Blanco opaco: 255, 255, 255, 255)
    draw.text((-bbox[0], -bbox[1]), text, font=font, fill=(255, 255, 255, 255))
    
    # 2.5 Convertir la imagen de PIL a un arreglo de bytes de NumPy
    img_data = np.array(list(img.getdata()), np.uint8)

    # 2.6 Proceso de Carga en OpenGL
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # Parámetros básicos para que la textura se vea bien
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    # Cargar los datos a la GPU
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_width, text_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    
    glBindTexture(GL_TEXTURE_2D, 0)
    
    return texture_id, text_width, text_height

# --- 3. FUNCIÓN DE DIBUJO ---
def dibujar_textura_quad(texture_info, x, y):
    """Dibuja un cuadrilátero con la textura aplicada en coordenadas de píxeles."""
    texture_id, width, height = texture_info
    
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0) # Color de la textura
    
    # Los 4 vértices del cuadrilátero, mapeados a las coordenadas de la textura (0.0 a 1.0)
    # Coordenadas de la Textura (T), Coordenadas de Pantalla (V)
    
    # Superior Izquierda
    glTexCoord2f(0.0, 0.0); glVertex2f(x, y + height) 
    # Superior Derecha
    glTexCoord2f(1.0, 0.0); glVertex2f(x + width, y + height)
    # Inferior Derecha
    glTexCoord2f(1.0, 1.0); glVertex2f(x + width, y)
    # Inferior Izquierda
    glTexCoord2f(0.0, 1.0); glVertex2f(x, y)
    
    glEnd()
    
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_BLEND)

# --- 4. FUNCIONES DE INICIALIZACIÓN DE OPENGL ---
def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(VENTANA_ANCHO, VENTANA_ALTO, "Pillow Textura Demo", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana

def configurar_coordenadas_ventana(ancho, alto):
    """Configura la proyección para usar coordenadas de píxeles (ventana)."""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(left, right, bottom, top, near, far)
    glOrtho(0.0, ancho, 0.0, alto, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# --- 5. BUCLE PRINCIPAL ---
def main():
    ventana = iniciar_ventana()
    configurar_coordenadas_ventana(VENTANA_ANCHO, VENTANA_ALTO)
    
    # Cargamos la textura UNA VEZ al inicio
    texture_info = cargar_textura_texto(TEXTO)
    t_id, t_width, t_height = texture_info
    
    # Posición central para el texto
    start_x = (VENTANA_ANCHO - t_width) / 2
    start_y = (VENTANA_ALTO - t_height) / 2
    
    glClearColor(0.1, 0.1, 0.2, 1.0)
    
    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Dibujamos el texto
        dibujar_textura_quad(texture_info, start_x, start_y)
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glDeleteTextures([t_id]) # Liberar la memoria de la GPU
    glfw.terminate()

if __name__ == "__main__":
    main()