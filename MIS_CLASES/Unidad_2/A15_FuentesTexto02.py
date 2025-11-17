import glfw
from OpenGL.GL import *
from PIL import Image, ImageDraw, ImageFont # Usaremos PIL para crear la textura
import numpy as np

# --- CONFIGURACIÓN DE LA VENTANA ---
VENTANA_ANCHO = 800
VENTANA_ALTO = 600

# --- FUNCIÓN CLAVE 1: Crear la Textura de la Letra ---
def create_text_texture(text, font_path, font_size):
    """Genera una textura de OpenGL a partir de un texto."""
    
    # Intenta cargar la fuente. Si falla, usa una fuente por defecto
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Advertencia: No se encontró la fuente. Usando fuente predeterminada de PIL.")
        font = ImageFont.load_default()
        
    # Obtener el tamaño que ocupará el texto
    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Crear una imagen transparente
    img = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Dibujar el texto en la imagen (Blanco opaco)
    draw.text((-bbox[0], -bbox[1]), text, font=font, fill=(255, 255, 255, 255))
    
    # Convertir la imagen a datos de textura
    img_data = np.array(list(img.getdata()), np.uint8)

    # 1. Generar ID de Textura en OpenGL
    texture_id = glGenTextures(1)
    
    # 2. Enlazar (Bind) la Textura
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # 3. Parámetros de la Textura
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) # Filtro para calidad al reducir
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) # Filtro para calidad al ampliar
    
    # 4. Cargar los datos de la imagen a la GPU
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_width, text_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    
    # Desenlazar la Textura
    glBindTexture(GL_TEXTURE_2D, 0)
    
    return texture_id, text_width, text_height

# --- FUNCIÓN CLAVE 2: Dibujar un Cuadrilátero con la Textura ---
def draw_textured_quad(texture_id, x, y, width, height):
    """Dibuja un cuadrilátero (rectángulo) con la textura aplicada."""
    
    # 1. Habilitar el uso de texturas 2D y el canal alfa (transparencia)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # 2. Enlazar la textura a dibujar
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # 3. Dibujar el cuadrilátero (dos triángulos)
    glBegin(GL_QUADS)
    
    glColor3f(1.0, 1.0, 1.0) # Establece el color (el color de la textura se multiplicará por este)
    
    # Esquina Superior Izquierda
    glTexCoord2f(0.0, 0.0); glVertex2f(x, y + height) 
    # Esquina Superior Derecha
    glTexCoord2f(1.0, 0.0); glVertex2f(x + width, y + height)
    # Esquina Inferior Derecha
    glTexCoord2f(1.0, 1.0); glVertex2f(x + width, y)
    # Esquina Inferior Izquierda
    glTexCoord2f(0.0, 1.0); glVertex2f(x, y)
    
    glEnd()
    
    # 4. Limpiar el estado
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_BLEND)


# --- FUNCIONES DE INICIALIZACIÓN ---
def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(VENTANA_ANCHO, VENTANA_ALTO, "Texto con Texturas", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana

def configurar_coordenadas_ventana(ancho, alto):
    # Usaremos coordenadas de píxeles (ventana) para facilitar el posicionamiento del texto
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, ancho, 0.0, alto, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# --- BUCLE PRINCIPAL ---
def main():
    ventana = iniciar_ventana()
    configurar_coordenadas_ventana(VENTANA_ANCHO, VENTANA_ALTO)
    
    # --- PREPARACIÓN DE LA TEXTURA ---
    # Nota: Debes indicar la ruta a un archivo .ttf real en tu sistema si quieres otra fuente.
    # Aquí se usa una fuente de sistema (ej. Arial) para maximizar la compatibilidad del ejemplo.
    try:
        font_path = "arial.ttf" # Reemplaza si no encuentras 'arial.ttf'
        texture_id, t_width, t_height = create_text_texture("Clase de Graficación", font_path, 72) 
    except Exception as e:
        print(f"Error al cargar la textura de texto: {e}")
        glfw.terminate()
        return

    glClearColor(0.1, 0.1, 0.2, 1.0)
    
    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Dibujar el texto texturizado
        # Posición de inicio: (100, 300) píxeles
        draw_textured_quad(texture_id, 100, 300, t_width, t_height)
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    # Limpiar recursos de OpenGL
    glDeleteTextures([texture_id])
    glfw.terminate()

if __name__ == "__main__":
    main()