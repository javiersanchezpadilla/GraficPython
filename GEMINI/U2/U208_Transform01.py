""" Ejemplo de Traslación, Rotación y Escalamiento  NO FUNCIONA ADECUADAMENTE!!!!

    Vamos a modificar el código de nuestro triángulo para que haga una animación 
    muy sencilla. En cada fotograma, el triángulo se moverá a la derecha, rotará 
    y se hará un poco más grande.

    Añadiremos al código las siguientes funciones:

    glTranslatef(x, y, z): Mueve el sistema de coordenadas. Los valores x e y 
    controlan el movimiento en 2D.
    glRotatef(angle, x, y, z): Rota el sistema de coordenadas. El angle es el 
    ángulo de rotación, y (x, y, z) define el eje de rotación. Para 2D, rotamos 
    en el eje z (como si una flecha perforara la pantalla en el centro del triángulo).
    glScalef(x, y, z): Escala el sistema de coordenadas. Los valores x e y 
    controlan el escalamiento en 2D.

    El orden de estas funciones es clave. En este ejemplo, primero rotaremos, luego 
    escalaremos y finalmente trasladaremos.
    
    Puntos clave del código

    Variables de animación: Hemos creado variables (translation_x, rotation_angle, scale) 
    que se actualizan en cada fotograma. Esto es lo que crea el efecto de movimiento, 
    rotación y crecimiento.
    glPushMatrix() y glPopMatrix(): Estas funciones son como el "botón de deshacer" de 
    las transformaciones. glPushMatrix() guarda el estado actual de la matriz de transformación, 
    y glPopMatrix() lo restaura. Esto es muy útil cuando quieres aplicar una transformación 
    a un objeto, pero no quieres que afecte a otros objetos que dibujes después.
    Orden de las transformaciones: En este caso, el orden es rotar, escalar y trasladar. 
    Si cambias el orden, el resultado será diferente. 
    """

import glfw
from OpenGL.GL import *
import math

# (Código de configuración de la ventana... es el mismo que antes)
if not glfw.init():
    raise Exception("glfw can't be initialized!")
window = glfw.create_window(800, 600, "Animación 2D", None, None)
if not window:
    glfw.terminate()
    raise Exception("glfw window can't be created!")
glfw.make_context_current(window)

# Variables para la animación
translation_x = 0.0
rotation_angle = 0.0
scale = 1.0
factor = 0.005

# El bucle principal
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.2, 0.3, 0.3, 1.0)

    # --- ¡Aquí es donde aplicamos las transformaciones! ---
    glPushMatrix() # Guarda el estado actual de la matriz de transformación

    # 1. Rotación
    glRotatef(rotation_angle, 0.0, 0.0, 1.0)
    
    # 2. Escalamiento
    glScalef(scale, scale, 1.0)
    
    # 3. Traslación
    glTranslatef(translation_x, 0.0, 0.0)

    # Dibuja el triángulo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(-0.2, -0.2)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.2, -0.2)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.2)
    glEnd()

    glPopMatrix() # Restaura el estado de la matriz

    # Actualiza las variables para la próxima iteración
    rotation_angle += 1.0
    if factor > 1 or factor < -1:
        factor = -factor  # Cambia la dirección de la traslación
    # translation_x += 0.005
    translation_x += factor
    if scale > 1.5 or scale < 0.5:
        factor = -factor  # Cambia la dirección del escalamiento
    # scale += 0.001
    scale += factor
    
    print(f"Rotación: {rotation_angle:.2f}, Traslación: {translation_x:.2f}, Escala: {scale:.2f}")
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()