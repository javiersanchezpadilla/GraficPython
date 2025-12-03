""" Esta es la forma correcta (pero complicada) para cargar imagenes en poligonos
    quedando como la textura del mismo"""


import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
import os
import sys
import numpy as np


                                                    # Configuración de Ventana y Constantes
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
NOMBRE_ARCHIVO = "/home/javier/Documentos/Programas/Python/Texturas/PNGs/ejm_redim.jpg"
texture_id = None                                   # ID global para la textura de OpenGL


                                                    # Carga y Conversión de Textura (Pillow a OpenGL)

def cargar_textura(nombre_archivo):
    """
    Carga una imagen PNG/JPG con Pillow y la convierte en una textura de OpenGL.
    """
    try:
                                                    # PASO 1: Cargar y convertir la imagen a RGBA para consistencia
        img = Image.open(nombre_archivo).convert('RGBA')
    except Exception as e:
        print(f"ERROR: No se pudo cargar la imagen '{nombre_archivo}'. {e}")
        return 0 
    
                                                    # Obtener el tamaño y los datos de la imagen
    width, height = img.size
    img_data = np.array(list(img.getdata()), np.uint8) # Convertir a array de bytes
    
                                                    # PASO 2: Generar el ID de Textura de OpenGL
    texture_id = glGenTextures(1)
    
                                                    # PASO 3: Vincular y configurar la textura
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
                                                    # Configurar cómo se comporta la textura al ser más grande/pequeña 
                                                    # que el polígono
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) # Suavizado al reducir
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) # Suavizado al ampliar
    
                                                    # PASO 4: Cargar los datos de la imagen a la VRAM
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    
                                                    # Desvincular la textura
    glBindTexture(GL_TEXTURE_2D, 0)
    
    print(f"Textura cargada correctamente. ID de OpenGL: {texture_id}")
    return texture_id


                                                    # 3. Dibujo del Cuadrado Texturizado

def dibujar_cuadrado_texturizado(id_textura):
    """Dibuja un cuadrado y le aplica la textura cargada."""
    
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, id_textura)
    
    # Usamos GL_QUADS para dibujar un simple cuadrado (polígono)
    glBegin(GL_QUADS)
    
    # Vertices y Coordenadas de Textura (TexCoords)
    # Los TexCoords (0.0 a 1.0) mapean la imagen sobre el cuadrado (2x2)
    
    # Inferior Izquierdo
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.5, -1.5, 0.0) 
    
    # Inferior Derecho
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.5, -1.5, 0.0)
    
    # Superior Derecho
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.5,  1.5, 0.0)
    
    # Superior Izquierdo
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.5,  1.5, 0.0)
    
    glEnd()
    
    # Deshabilitar texturizado
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)


# --- 4. Bucle de Renderizado y Main ---

def dibujar_escena(window):
    """Función de renderizado principal."""
    global texture_id
    
    glClearColor(0.1, 0.1, 0.1, 1.0) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar Vista (Cámara)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # Movemos la cámara hacia atrás para poder ver el cuadrado
    glTranslatef(0.0, 0.0, -5.0) 
    
    # Dibujar el cuadrado si la textura se cargó con éxito
    if texture_id:
        dibujar_cuadrado_texturizado(texture_id)

    glfw.swap_buffers(window)
    

def window_resize(window, width, height):
    """Callback para manejar el cambio de tamaño de la ventana."""
    glViewport(0, 0, width, height) 
    
    # Configurar Proyección (Perspectiva) para el nuevo tamaño
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    ratio = width / height if height != 0 else 1
    gluPerspective(45, ratio, 0.1, 50.0)

def inicializar_glfw():
    """Inicializa GLFW y la ventana."""
    if not glfw.init():
        print("Error: No se pudo inicializar GLFW.")
        sys.exit(1)

    window = glfw.create_window(ANCHO_VENTANA, ALTO_VENTANA, "Imagen en Cuadrado (Pillow + OpenGL)", None, None)
    
    if not window:
        glfw.terminate()
        print("Error: No se pudo crear la ventana de GLFW.")
        sys.exit(1)

    glfw.make_context_current(window)
    glfw.set_window_size_callback(window, window_resize)
    
    # Llamar al resize una vez para configurar la proyección inicial
    window_resize(window, ANCHO_VENTANA, ALTO_VENTANA)
    
    # Habilitamos la mezcla de colores (solo por si cargamos PNG con transparencia)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    return window

def main():
    global texture_id
    
    # Paso 1: Asegurar que la imagen exista
    crear_archivo_de_prueba()
    
    # Paso 2: Inicializar el entorno gráfico
    window = inicializar_glfw()
    
    # Paso 3: Cargar la imagen y obtener el ID de Textura
    texture_id = cargar_textura(NOMBRE_ARCHIVO)

    # Paso 4: Bucle principal de la aplicación
    while not glfw.window_should_close(window):
        glfw.poll_events()
        dibujar_escena(window)

    glfw.terminate()

if __name__ == "__main__":
    main()