""" COMPONENTES BÁSICOS DE LA ILUMINACIÓN. 

    CONFIGURACIÓN MÍNIMA PARA TENER ILUINACIÓN
    ------------------------------------------

    def configurar_iluminacion_basica():
        
        # 1. ACTIVAR la iluminación (como encender la luz eléctrica)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)  # Usar luz número 0
        
        # 2. Configurar la LUZ (foco)
        luz_posicion = [2.0, 2.0, 2.0, 1.0]  # Posición (x,y,z, 1.0=posicional)
        luz_color = [1.0, 1.0, 1.0, 1.0]     # Color (R,G,B,A) - blanco
        
        glLightfv(GL_LIGHT0, GL_POSITION, luz_posicion)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_color)
        
        # 3. Configurar el MATERIAL (pintura del objeto)
        material_color = [0.8, 0.2, 0.2, 1.0]  # Rojo
        glMaterialfv(GL_FRONT, GL_DIFFUSE, material_color)
        
        # 4. ACTIVAR depth test para cálculos correctos
        glEnable(GL_DEPTH_TEST)
        
        # 5. Configurar modelo de iluminación
        glEnable(GL_COLOR_MATERIAL)  # Usar colores de glColor3f (glColor**)
        glShadeModel(GL_SMOOTH)      # Suavizado de superficies
         
          
    LOS PARAMETROS BÁSICOS 
    ----------------------

    PARÁMETROS DE LA LUZ:

        # POSICIÓN: ¿Dónde está la luz?
        luz_posicion = [x, y, z, tipo]
        # tipo=1.0 → Luz posicional (como foco)
        # tipo=0.0 → Luz direccional (como sol)

        # COLOR AMBIENTE: Iluminación general suave
        luz_ambiente = [0.2, 0.2, 0.2, 1.0]  # Gris suave

        # COLOR DIFUSO: Color principal de la luz  
        luz_difusa = [1.0, 1.0, 1.0, 1.0]    # Blanco

        # COLOR ESPECULAR: Color de los brillos
        luz_especular = [1.0, 1.0, 1.0, 1.0] # Blanco


    PARÁMETROS DEL MATERIAL:
    ------------------------

        # MATERIAL DIFUSO: Color base del objeto
        material_difuso = [R, G, B, A]  # Ej: [1.0, 0.0, 0.0, 1.0] = Rojo

        # MATERIAL ESPECULAR: Color de los reflejos
        material_especular = [R, G, B, A]  # Blanco para reflejos naturales

        # BRILLANTEZ: Qué tan concentrado es el brillo
        material_brillantez = [valor]  # 0-128, mayor = brillo más concentrado  


    CONFIGURACIÓN MÍNIMA PARA COMENZAR
    ----------------------------------
        def iluminacion_minima()
            # La configuración ABSOLUTAMENTE MÍNIMA para que funcione
            glEnable(GL_LIGHTING)
            glEnable(GL_LIGHT0)
            glEnable(GL_DEPTH_TEST)
            
            # Solo estos dos parámetros son esenciales:
            glLightfv(GL_LIGHT0, GL_POSITION, [2, 2, 2, 1])  # Posición luz
            glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])   # Color luz
            
            # Opcional: para usar colores normales con glColor*
            glEnable(GL_COLOR_MATERIAL)

            
    COMO SOLUCIONAR LOS ERRORES MAS COMUNES
    ---------------------------------------
    Problema: "No se ve la iluminación"
    Solución:

        glEnable(GL_LIGHTING)    # Verificar que activamos esto
        glEnable(GL_LIGHT0)      # tambien se debe activar esto
        glEnable(GL_DEPTH_TEST)  # Con esto le estamos diciendo que tenga mayor exactitud en los calculos

    Problema: "Los objetos se ven todos negros"
    Solución:

        # Verificar que la luz tenga posición correcta
        glLightfv(GL_LIGHT0, GL_POSITION, [2, 2, 2, 1])  # No [0,0,0,1]

        # Y que los materiales tengan color
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [1, 0, 0, 1])  # Rojo         
"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time

def inicializar_iluminacion():
    """Inicializa todo el sistema de iluminación"""
    
    # ACTIVAR SISTEMA DE ILUMINACIÓN
    glEnable(GL_LIGHTING)                           # activa la iluminacion
    glEnable(GL_LIGHT0)                             # Enciende el foco cero
    glEnable(GL_DEPTH_TEST)                         # habilita las pruebas de profundidad
    glEnable(GL_COLOR_MATERIAL)                     # habilita el uso de colores en los materiales
    glShadeModel(GL_SMOOTH)
    
    glClearColor(0.3, 0.3, 0.3, 1.0)                # COLOR DE FONDO (gris claro para mejor contraste)

    # Configuramos los componentes de la luz (luz ambiente, luz difusa y luz especular)    
    # Configurar LUZ AMBIENTE (iluminación general)
    luz_ambiente = [0.2, 0.2, 0.2, 1.0]             # Gris suave
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)
    
    # Configurar LUZ DIFUSA (color principal de la luz)
    luz_difusa = [0.8, 0.8, 0.8, 1.0]               # Blanco brillante
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    
    # Configurar LUZ ESPECULAR (brillos) (es ese pequeño punto en la esfera, el del maximo brillo)
    luz_especular = [1.0, 1.0, 1.0, 1.0]            # Blanco puro para brillos
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)

def actualizar_luz(tiempo):
    """Mueve la luz en círculo para ver efectos"""
    radio = 3.0
    x = math.cos(tiempo) * radio
    z = math.sin(tiempo) * radio
    y = 2.0  # Altura fija
    
    luz_posicion = [x, y, z, 1.0]  # 1.0 = luz posicional
    glLightfv(GL_LIGHT0, GL_POSITION, luz_posicion) # Ubicacion del foco, realmente esta girando
    
    return x, y, z                                  # NO se espanten, no esta retornando tres valores
                                                    # esta retornando uno solo valor (que es una TUPLA)



def dibujar_esfera_con_material(x, y, z, radio, color, brillo=0.0):
    """ Dibuja una esfera con propiedades de material específicas
        Representa la esfera con caracteristicas de materiales"""
    glPushMatrix()
    glTranslatef(x, y, z)
    
    # Configurar MATERIAL
    material_difuso = [color[0], color[1], color[2], 1.0]
    material_especular = [brillo, brillo, brillo, 1.0]
    material_brillantez = [50.0]                    # Qué tan concentrado es el brillo
    
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_difuso)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_especular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_brillantez)
    
    glutSolidSphere(radio, 32, 32)
    glPopMatrix()



# CONFIGURACIÓN PRINCIPAL
if not glfw.init():
    exit()

ventana = glfw.create_window(800, 600, "Iluminación OpenGL - Básica", None, None)
glfw.make_context_current(ventana)

                        # ***********************************************************************
glutInit()              # Activamos GLUT                                                    *****
                        # recordar que el caso de windows tienen que crear una ventanita    *****
                        # glutCreateWindow(b"La ventanita")
                        # ***********************************************************************

inicializar_iluminacion()
tiempo_inicio = time.time()

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar perspectiva
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 50.0)          # Esta parte ya la entienden
    
    # Configurar cámara
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 3, 8,  0, 0, 0,  0, 1, 0)          # Esta otra parte tambien ya la entienden
    
    # Actualizar posición de la luz (se mueve en círculo)
    tiempo_actual = time.time() - tiempo_inicio
    luz_x, luz_y, luz_z = actualizar_luz(tiempo_actual * 0.5)
    
    # DIBUJAR OBJETOS CON DIFERENTES MATERIALES
    
    # Esfera ROJA - Material mate (sin brillo)
    dibujar_esfera_con_material(-2, 0, 0, 0.8, [1.0, 0.2, 0.2], brillo=0.0)
    
    # Esfera VERDE - Material plástico (poco brillo)
    dibujar_esfera_con_material(0, 0, 0, 0.8, [0.2, 1.0, 0.2], brillo=0.3)
    
    # Esfera AZUL - Material metálico (mucho brillo)
    dibujar_esfera_con_material(2, 0, 0, 0.8, [0.2, 0.2, 1.0], brillo=0.8)
    
    # Piso para referencia (El piso es un cubo escalado en 5 unidades en "x", 0.1 en "y" 
    # y una profundidad de 5 para "z"
    glPushMatrix()
    glTranslatef(0, -1.5, 0)
    glScalef(5, 0.1, 5)     # glScalef(5, 0.1, 5)
    material_piso = [0.7, 0.7, 0.7, 1.0]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_piso)
    glutSolidCube(1)
    glPopMatrix()
    
    # Dibujar posición de la luz (esfera pequeña amarilla)
    glDisable(GL_LIGHTING)  # Temporalmente desactivar iluminación para que no se vea solo como sombra 
    glColor3f(1, 1, 0)      # y brille sin necesidad de otra fuente de luz, el color es Amarillo
    glPushMatrix()
    glTranslatef(luz_x, luz_y, luz_z)
    glutSolidSphere(0.1, 8, 8)
    glPopMatrix()
    glEnable(GL_LIGHTING)   # Reactivar iluminación para que la escena se vea iluminada
    
    # Información en título
    glfw.set_window_title(ventana, 
        f"Iluminación OpenGL - Luz en: ({luz_x:.1f}, {luz_y:.1f}, {luz_z:.1f})")
    
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
