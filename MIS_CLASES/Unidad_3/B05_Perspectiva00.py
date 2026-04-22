""" USO DE PERSPECTIVA Y LOOKAT

     imaginar que estás en un set de filmación de una película. 
     En OpenGL, tú eres el director de cámara.
     
     1. gluPerspective: La Lente de la Cámara
     Esta función define qué tipo de lente tiene tu cámara. ¿Es un gran angular 
     que ve mucho espacio o un zoom que ve solo un detalle?
     
     ¿Qué hace?: Crea la sensación de profundidad. Las cosas lejos se ven 
     pequeñas y las cerca se ven grandes.
     Parámetros clave:
     fovy: El ángulo de visión (qué tan abierta es la toma). 
     45 grados es lo estándar.
     aspect: La relación entre ancho y alto (para que no se vea "estirada" la imagen).
     zNear y zFar: Qué tan cerca y qué tan lejos puede ver la cámara (el rango de visión).
     
     2. gluLookAt: La Posición de la CámaraEsta función define dónde está la 
     cámara y a dónde apunta.
     ¿Qué hace?: Mueve físicamente la cámara por el espacio 3D.
     Parámetros clave (se agrupan de 3 en 3):
     eye (x, y, z): ¿Dónde estás parado tú con la cámara?
     center (x, y, z): ¿A qué punto exacto estás mirando?
     up (x, y, z): ¿Hacia dónde está el 'cielo' (donde es arriba)? (Normalmente es 0, 1, 0).
     
     Imagina que hay un cubo en el centro del mundo (0, 0, 0) y nosotros nos 
     alejamos para verlo desde una esquina.

     Resumen de la analogía:
     gluPerspective: Es cuando decides si vas a usar un lente de 18mm (mucha visión) o 
     uno de 200mm (telescopio). Solo lo haces una vez o cuando cambias el tamaño de la 
     ventana.
     gluLookAt: Es cuando mueves el trípode de la cámara por la habitación. Se 
     suele llamar en cada vuelta del bucle si quieres que la cámara se mueva 
     (por ejemplo, si sigues a un personaje).
    
"""
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

def configurar_proyeccion(ancho, alto):
    """Define la lente de la camara (Perspectiva)"""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # gluPerspective(angulo_vision, relacion_aspecto, cerca, lejos)
    aspecto = ancho / alto
    gluPerspective(45, aspecto, 0.1, 12.0)
    # gluPerspective(45, aspecto, 0.1, 100.0)
    
    glMatrixMode(GL_MODELVIEW)

def configurar_camara():
    """Define la posicion y direccion de la camara"""
    glLoadIdentity()
    
    # gluLookAt(
    #   ojo_x, ojo_y, ojo_z,     <- Donde esta la camara
    #   centro_x, centro_y, centro_z, <- A donde mira
    #   arriba_x, arriba_y, arriba_z  <- Direccion del 'cielo'
    # )
    gluLookAt(3, 3, 5,  # Estamos arriba a la derecha y lejos
              0, 0, 0,  # Miramos al centro del mundo (donde estara el cubo)
              0, 1, 0)  # El eje Y es hacia arriba

def dibujar_cubo_basico():
    """Dibuja un cubo simple para tener algo que ver"""
    glBegin(GL_LINES)
    # Eje X (Rojo)
    glColor3f(1, 0, 0); glVertex3f(0, 0, 0); glVertex3f(1, 0, 0)
    # Eje Y (Verde)
    glColor3f(0, 1, 0); glVertex3f(0, 0, 0); glVertex3f(0, 1, 0)
    # Eje Z (Azul)
    glColor3f(0, 0, 1); glVertex3f(0, 0, 0); glVertex3f(0, 0, 1)
    glEnd()

    # Un cuadrado blanco para representar una cara
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex3f(-0.5, -0.5, 0); glVertex3f(0.5, -0.5, 0)
    glVertex3f(0.5, 0.5, 0); glVertex3f(-0.5, 0.5, 0)
    glEnd()

def main():
    if not glfw.init(): return
    
    ancho, alto = 800, 600
    ventana = glfw.create_window(ancho, alto, "Camara con gluLookAt", None, None)
    glfw.make_context_current(ventana)
    
    # Habilitar prueba de profundidad para que el 3D se vea bien
    glEnable(GL_DEPTH_TEST)

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # 1. Configuramos la lente
        configurar_proyeccion(ancho, alto)
        
        # 2. Posicionamos la camara
        configurar_camara()
        
        # 3. Dibujamos el objeto
        dibujar_cubo_basico()

        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()


