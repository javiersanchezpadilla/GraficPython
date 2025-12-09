""" En este codigo se muestra como cargar texturas de acuerdo a una matriz
    En esta primera parte solo se dibuja la escena cargando los mapas de bits.
    En la definición de la matrizs para cargar la escena son primero filas (EjeY) y después  columnas (EjeX)
        0 piso normal (puede pasar).
        1 muro destruible.
        2 muro no destruible.
        3 premio.
        4 caja

    Cada elemento de la matriz se considera a 50 pixeles de tamaño.
    12 x 50 = 600 pixeles de ancho
    9  x 50 = 450 pixeles de alto
    Por lo tanto la ventana se define enuna escala de 600 x 450, la resolucion que se manejo es de 850 x 480 pixeles




    En esta parte del código se obliga a que se represente la matriz de arriba hacia abajo con su equivalente en pixeles 
    por cada posición de la matriz numérica.
        razon_matriz = 50  # Tamaño de cada cuadro en píxeles
        pos_pixel_x = (pos_mat_x) * razon_matriz
        pos_pixel_y = 450 - ((pos_mat_y + 1) * razon_matriz)


"""


import glfw
from OpenGL.GL import *
from PIL import Image
import time
import os


def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(850, 480, "Mundo en matrix numérica en", None, None)
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
    glOrtho(0.0, 600.0, 0.0, 450.0, -1.0, 1.0) 

    # Volvemos a la matriz de modelo-vista para dibujar
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


                                                            # Función para cargar texturas usando Pillow (PIL)
                                            # Función para cargar textura
def cargar_textura(ruta):
    imagen = Image.open(ruta).transpose(Image.FLIP_TOP_BOTTOM)
    img_data = imagen.convert("RGBA").tobytes()
    width, height = imagen.size

    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return tex_id



def dibuja_cuadro_con_bmp(pos_mat_x, pos_mat_y, textura_id):
    razon_matriz = 50  # Tamaño de cada cuadro en píxeles
    pos_pixel_x = (pos_mat_x) * razon_matriz
    pos_pixel_y = 450 - ((pos_mat_y + 1) * razon_matriz)

    glBindTexture(GL_TEXTURE_2D, textura_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex2i(pos_pixel_x, pos_pixel_y)
    glTexCoord2f(1.0, 0.0); glVertex2i(pos_pixel_x + razon_matriz, pos_pixel_y)
    glTexCoord2f(1.0, 1.0); glVertex2i(pos_pixel_x + razon_matriz, pos_pixel_y + razon_matriz)
    glTexCoord2f(0.0, 1.0); glVertex2i(pos_pixel_x, pos_pixel_y + razon_matriz)
    glEnd()



def muestra_mundo(mundo_matriz, texturas):
    # glColor3f(1.0, 1.0, 1.0)
    for y, fila in enumerate(mundo_matriz):
        for x, que_textura in enumerate(fila):
            textura_id = texturas[que_textura]
            dibuja_cuadro_con_bmp(x, y, textura_id)


                                                            # Cargar carpeta de sprites
def carga_sprites_de_carpeta(folder):
    texturas = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            texturas.append(cargar_textura(os.path.join(folder, file))) 
    return texturas



# El bucle principal de trabajo
def programa_principal():
    # Asignamos a la variable ventana el valor retornado por la función iniciar_ventana
    ventana = iniciar_ventana()
    proyeccion()

                                                             
    glEnable(GL_TEXTURE_2D)                                 # Activar texturas  
    glEnable(GL_BLEND)                                      # Activar transparencia en PNGs
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glfw.make_context_current(ventana)
                                                            # Genermamos la matriz del mundo
    mundo_matriz=[[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [2, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2],
                  [2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 2],
                  [2, 0, 1, 0, 1, 0, 1, 4, 4, 0, 0, 2],
                  [2, 0, 1, 0, 0, 0, 0, 0, 3, 0, 1, 2],
                  [2, 2, 0, 2, 1, 0, 1, 0, 1, 0, 0, 2],
                  [2, 0, 3, 0, 1, 0, 1, 0, 1, 0, 0, 2],
                  [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
                                                            
    texturas = { 
        0: cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/BMPs/PisoMundo.bmp"),
        1: cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/BMPs/MuroDestruible.bmp"),
        2: cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/BMPs/MuroFijo.bmp"),
        3: cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/BMPs/PremioUNO.bmp"),
        4: cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/BMPs/Caja.bmp")
    }

                                                            # **********  CARGAR LAS LISTAS DE LOS SPRITES PARA CADA DIRECCION
    sprites = {
    "left":  carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sprites/izquierda"),
    "right": carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sprites/derecha")
    }

    direccion = "right"
    indice_del_frame = 0
    pos_jugador_x, pos_jugador_y = 50.0, 50.0




    while not glfw.window_should_close(ventana):
        glfw.poll_events()


                                                                    # Movimiento del jugador y control de dirección         
        if glfw.get_key(ventana, glfw.KEY_RIGHT) == glfw.PRESS:
            pos_jugador_x += 0.01
            direccion = "right"
            se_esta_moviendo = True
            indice_del_frame = (indice_del_frame + 1) % len(sprites[direccion])
        elif glfw.get_key(ventana, glfw.KEY_LEFT) == glfw.PRESS:
            pos_jugador_x += 0.01
            direccion = "left"
            se_esta_moviendo = True
            indice_del_frame = (indice_del_frame + 1) % len(sprites[direccion])
        elif glfw.get_key(ventana, glfw.KEY_UP) == glfw.PRESS:
            pos_jugador_y += 0.01
            direccion = "right"
            se_esta_moviendo = True
            indice_del_frame = (indice_del_frame + 1) % len(sprites[direccion])
        elif glfw.get_key(ventana, glfw.KEY_DOWN) == glfw.PRESS:
            pos_jugador_y -= 0.01
            direccion = "left"
            se_esta_moviendo = True
            indice_del_frame = (indice_del_frame + 1) % len(sprites[direccion])






        glClear(GL_COLOR_BUFFER_BIT)                        # Dibujar la escena


        muestra_mundo(mundo_matriz, texturas)

         # En este caso el sprite se dibuja en la posición (pos_jugador_x, pos_jugador_y)
        # voy a considerar los cuatro sentidos de movimiento, por lo que la posición Y también puede cambiar
        # en caso de solo usar izquierda y derecha, solo la posición X cambiará
        # pero queda preparado para que puedan agregar arriba y abajo si lo desean
        textura_actual_personaje = sprites[direccion][indice_del_frame]          # Sprite animado
        glBindTexture(GL_TEXTURE_2D, textura_actual_personaje)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(pos_jugador_x, pos_jugador_y)
        glTexCoord2f(1, 0); glVertex2f(pos_jugador_x + 50, pos_jugador_y)
        glTexCoord2f(1, 1); glVertex2f(pos_jugador_x + 50, pos_jugador_y + 50)
        glTexCoord2f(0, 1); glVertex2f(pos_jugador_x, pos_jugador_y + 50)
        glEnd()


        glfw.swap_buffers(ventana)
        #glfw.poll_events()
    # Terminamos el programa y cerramos todo
    glfw.terminate()


programa_principal()