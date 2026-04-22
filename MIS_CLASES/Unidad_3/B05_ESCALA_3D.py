""" ESTE EJEMPLO PERMITE ENTENDER EL USO DE PERSPECTIVA gluPerspective() Y gluLookAt()
    ===================================================================================

    si quiero el uso de perspectiva, pero ademas quiero definir los valores de los ejes de coordenadas
    en los siguientes rangos, para "x" de (-15 a 15), en "y" de (-15 a 15) para "z" de (-15 a 15)
    ¿en que momento definimos los valores de los ejes de coordenadas para todos lo ejes de -15 a 15? 

    Las Coordenadas las DEFINE el usuario al momento de Dibujar. 
    Cuando creamos una escena pero no definimos coordenadas, se asume que el rango son coordenadas normalizadas
    (desde -1 a 1 en todos los ejes), sin embargo la realidad es que OpenGL no tiene un "mundo" predefinido. 
    Uno crea el rango de coordenadas según cómo se dibujan los objetos:

    Cuando dibujas un cubo, TÚ defines sus coordenadas: por ejemplo aquí nos basamos en coordenadas normalizadas

        glBegin(GL_QUADS)
        glVertex3f(-1, -1, 1)   # TÚ defines que va en x=-1, y=-1, z=1
        glVertex3f( 1, -1, 1)   # TÚ defines que va en x=1, y=-1, z=1  
        glVertex3f( 1,  1, 1)   # TÚ defines que va en x=1, y=1, z=1
        glVertex3f(-1,  1, 1)   # TÚ defines que va en x=-1, y=1, z=1
        glEnd()

    CREANDO UN MUNDO DE -15 A 15 EN TODOS LOS EJES DE COORDENADAS. Pero ¿qué sucede si queremos crear una escena 
    donde los valores los pueda usar desde -15 a 15 en todos los ejes?, facil, simplemente dibujo las figuras
    basandome en este sistema de coordenadas que requiero, realmente la magia ocurre cuando le indico a OpenGL
    los valores necesarios para que pueda manejar la perspectiva y la posicion de la camara o punto de vision del
    espectador

        gluPerspective(45, 800/600, 1.0, 100.0)  # Near=1, Far=100
    
        gluPerspective(fovy, aspect, zNear, zFar)

    fovy (Field of View Y)          Es el ángulo vertical de visión.
    Angulo PEQUEÑO (ej: 30°)        Es como usar un teleobjetivo. Verás el mundo "acercado" o 
                                    con zoom. La perspectiva es más plana.
    Ángulo GRANDE (ej: 90°)         Es como usar un gran angular. Verás más del mundo, pero con 
                                    una distorsión de perspectiva más pronunciada (los objetos 
                                    cercanos se verán muy grandes).
                                    <<<Sugerencia: Un valor común es 45 o 60.>>>
    aspect (Aspect Ratio)           Es la relación de aspecto de la ventana (ANCHO / ALTO).
                                    Esto es crucial para que los objetos no se vean estirados. 
                                    Si tu ventana es 800x600, el aspect es 800 / 600 = 1.33.
    zNear y zFar                    Son los planos de corte cercano y lejano.
    zNear                           Es la distancia mínima que la cámara ve. Los objetos más cerca 
                                    de este plano se cortan. Debe ser un valor pequeño (ej: 0.1).
    zFar                            Es la distancia máxima que la cámara ve. Los objetos más allá 
                                    de este plano no se dibujan, lo que ayuda a ahorrar recursos. 
                                    Debe ser un valor grande (ej: 50.0).

    Configurar cámara para VER mi mundo de -15 a 15

        gluLookAt(
            25, 20, 25,    # Cámara fuera del rango -15 a 15
            0, 0, 0,       # Mira al centro de mi mundo
            0, 1, 0        # Arriba (eje "y")
        )

        gluLookAt(): Colocar y Apuntar la Cámara (Matriz de Vista)

    gluLookAt() define dónde está la cámara, hacia dónde está mirando y cuál es su orientación vertical.
    Su Función: Mueve el mundo entero de forma que parezca que la cámara se ha movido o rotado.

    ¿Cómo funciona?
    Esta función toma 9 argumentos que se organizan en 3 grupos de coordenadas (X, Y, Z):

    gluLookAt(eyeX, eyeY, eyeZ,               1. Posición de la Cámara (Eye)
              centerX, centerY, centerZ,      2. El Punto al que Mira (Center)
              upX, upY, upZ)                  3. La Orientación Vertical (Up)

    eye (Posición de la Cámara): ¿Dónde está el fotógrafo? Si pones (0, 0, 10), la cámara está en (0, 0, 10).
    center (Punto al que Mira): ¿Hacia dónde apunta el fotógrafo? Si pones (0, 0, 0), la cámara mira 
    directamente al origen del mundo 3D.
    up (Orientación Vertical): ¿Qué es "arriba" para la cámara? Casi siempre es (0, 1, 0). Esto significa que 
    el eje Y es la dirección vertical de tu cámara (el lado superior de la pantalla).

    Analogía:
    Usar gluLookAt(0, 2, 5, 0, 0, 0, 0, 1, 0)       es como decir: "Coloca al fotógrafo 5 metros delante del 
                                                    origen y 2 metros por encima, apuntando al centro, y mantén 
                                                    la cabeza derecha (el eje Y es arriba)."
    gluLookAt(25, 20, 25, 0, 0, 0, 0, 1, 0)         (25, 20, 25  Coloca al fotografo 25 metros a la derecha, del origen 
                                                    (fuera del rango de -15 a 15), 20 metros por encima y 25 metros 
                                                    adelante del origen apuntando al centro
                                                    0, 0, 0,    Apuntano al centro del origen 
                                                    1, 1, 0)    MAnten 1 unidad por encima

                                                    
    OpenGL NO TIENE coordenadas predefinidas
    ----------------------------------------

    * TÚ CREAS las coordenadas cuando dibujas vértices
    * El "rango de -15 a 15" lo decides tú al:
    * Posicionar objetos entre -15 y 15
    * Dibujar ejes de -15 a 15

    Usar tamaños que quepan en ese rango
    ¡Tú eres el arquitecto de tu mundo 3D! Las coordenadas existen solo donde tú las defines.


    ¿COMO SABER EL RANGO DEL MUNDO? Tú decides el rango basado en:
    --------------------------------------------------------------
    * Posiciones de los objetos en la escena
    * Tamaños de los objetos
    * Dónde son colocados los límites visuales


    PARA EL USO DE LAS FIGURAS DE ALAMBRE DE GLUT:
    ---------------------------------------------
    Cuando importamos:

    import glfw
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *       <-- Aquí es donde se accede a las funciones de GLUT/FreeGLUT

    ya para llamar a las funciones y usarlas debemos referenciar de la siguiente forma:

        glutInit()                     <-- Inicializar para poder hacer uso de las funciones
        glutWireSphere(2, 25, 25)      <-- Llamar a la funcion glutWireSphere()
        glutWireCube(2)                <-- Llamar a la funcion glutWireCube()
        glutWireTorus(1, 3, 16, 32)    <-- Llamar a la funcion glutWireTorus()


    EN CASO DE IMPORTAR Freeglut DE ESTA MANERA:

    from OpenGL import GLUT  
    
    entonces tenemos que referencias a las funciones de esta forma:

        GLUT.glutInit()                     <-- Inicializar para poder hacer uso de las funciones
        GLUT.glutWireSphere(2, 25, 25)      <-- Llamar a la funcion glutWireSphere()
        GLUT.glutWireCube(2)                <-- Llamar a la funcion glutWireCube()
        GLUT.glutWireTorus(1, 3, 16, 32)    <-- Llamar a la funcion glutWireTorus()
"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL import GLUT


def dibujar_mi_mundo():
    """ YO DECIDO que mi mundo va de -15 a 15 en todos los ejes, sin necesidad
        de definir una escala fija """
    
    # Dibujar una esfera en el CENTRO (0,0,0) con radio 2
    # Ocupa aproximadamente de -2 a 2 en cada eje, (si el radio es 2
    # entonces el diametro total será de 2 + 2 = 4)

    glColor3f(1, 1, 0)
    # como quiero que la esfera sea representada en el origen, no es necesario
    # redefinir un nuevo origen, por eso no se requiere glTranslatef(0, 0, 0)
    GLUT.glutWireSphere(2, 25, 25)
    
    # Dibujar un cubo en posición (10, 5, -8)
    # Ocupa aproximadamente de 9 a 11 en X, 4 a 6 en Y, -9 a -7 en Z
    glPushMatrix()
    glTranslatef(10, 5, -8)
    GLUT.glutWireCube(2)
    glPopMatrix()
    
    # Dibujar un toro en posición (-12, -10, 12)  
    # Ocupa aproximadamente de -14 a -10 en X, -12 a -8 en Y, 10 a 14 en Z
    glPushMatrix()
    glTranslatef(-12, -10, 12)
    GLUT.glutWireTorus(1, 3, 16, 32)
    glPopMatrix()
    
    # Dibujar los ejes de coordenadas desde -15 hasta 15 para todos los ejes
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)  # Eje X de -15 a 15 en rojo
    glVertex3f(-15, 0, 0)
    glVertex3f(15, 0, 0)
    
    glColor3f(0, 1, 0)  # Eje Y de -15 a 15  en verde
    glVertex3f(0, -15, 0)
    glVertex3f(0, 15, 0)
    
    glColor3f(0, 0, 1)  # Eje Z de -15 a 15 en azul
    glVertex3f(0, 0, -15)
    glVertex3f(0, 0, 15)
    glEnd()


# Configuración principal
if not glfw.init():
    exit()

ventana = glfw.create_window(800, 600, "Mi Mundo -15 a 15", None, None)
glfw.make_context_current(ventana)

GLUT.glutInit()     # Inicializamos GLUT
glEnable(GL_DEPTH_TEST)

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar perspectiva
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 1.0, 100.0)  # Near=1, Far=100
    
    # Configurar cámara para VER mi mundo de -15 a 15
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        25, 20, 25,    # Cámara fuera del rango -15 a 15 (25, 20, 25)
        0, 0, 0,       # Mira al centro de mi mundo
        0, 1, 0        # Arriba
    )
    
    # Dibujar MI mundo con rango -15 a 15
    dibujar_mi_mundo()
    
    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
