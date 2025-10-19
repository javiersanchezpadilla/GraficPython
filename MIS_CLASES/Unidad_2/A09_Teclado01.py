""" En este ejercicio se dibujara un cuadro en el centro de la pantalla.
    Cuando el usuario oprima una tecla se identidicara en la pantalla de la consola.
    LA idea es entender como funciona el callback de teclado en GLFW.

    Dado que estamos utilizando la biblioteca GLFW, la forma de detectar e identificar 
    las teclas es a través de una función llamada callback de teclado.

    1. Implementación del Callback de Teclado en GLFW
       GLFW utiliza un sistema de "callbacks" (llamadas de retorno) para manejar la entrada. 
       En lugar de revisar en cada fotograma si una tecla está presionada, le dices a GLFW: 
       "Si ocurre un evento de teclado, llama a esta función que te voy a dar."

    Código de la Función Callback
    Necesitas definir una función que GLFW llamará automáticamente. Esta función recibe varios parámetros, 
    siendo los más importantes el código de la tecla y la acción (presionar o soltar).

    Tecla                   Constante       GLFWDescripción
    -----------------------------------------------------------------------
    Flecha Arriba       glfw.KEY_UP         Mueve la figura hacia arriba.
    Flecha Abajo        glfw.KEY_DOWN       Mueve la figura hacia abajo.
    Flecha Izquierda    glfw.KEY_LEFT       Mueve la figura a la izquierda.
    Flecha Derecha      glfw.KEY_RIGHT      Mueve la figura a la derecha.
    

    *** OTROS PARÁMETROS CLAVE SON:
    -------------------------------------------------------------------------------------------    
    action                  Indica lo que sucedió con la tecla:
        glfw.PRESS:     La tecla fue presionada por primera vez.
        glfw.RELEASE:   La tecla fue soltada.
        glfw.REPEAT:    La tecla se mantiene presionada (el sistema operativo repite la señal).

        
    *** CONSTANTES DE TECLAS COMUNES EN GLFW
    
    TIPO DE TECLA               CONSTANTE GLFW                              USO TÍPICO
    -------------------------------------------------------------------------------------------------------------------
    Teclas Alfanuméricas    glfw.KEY_A, glfw.KEY_B, glfw.KEY_Z, etc.    Entrada de texto o comandos específicos 
                                                                        (ej. 'W', 'A', 'S', 'D' para movimiento).
                                                                        
    Números (Arriba)        glfw.KEY_0 a glfw.KEY_9                     Selección de ítems o cambio de herramienta.
    
    Teclas de Función       glfw.KEY_F1 a glfw.KEY_F12                  Acciones rápidas o menús de ayuda.
    
    Teclas Especiales       glfw.KEY_SPACE                              Saltar o disparar.
                            glfw.KEY_ENTER                              Aceptar o confirmar.
                            glfw.KEY_ESCAPE                             Pausa, salir de un menú o terminar el programa.
                            glfw.KEY_LEFT_SHIFT,                        Correr o modificar una acción.
                            glfw.KEY_RIGHT_SHIFT
                            glfw.KEY_LEFT_CONTROL,                      Agacharse o disparar secundario.          
                            glfw.KEY_RIGHT_CONTROL
        
        """

import glfw
from OpenGL.GL import *


def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Mi primera ventana como funcion en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana



def key_callback(window, key, scancode, action, mods):
    
    # Solo procesamos eventos cuando la tecla es PRESIONADA o REPETIDA
    if action == glfw.PRESS or action == glfw.REPEAT:
        
        # 2. Identificación de Teclas
        if key == glfw.KEY_UP:
            print("Flecha Arriba presionada")
        elif key == glfw.KEY_DOWN:
            print("Flecha Abajo presionada")
        elif key == glfw.KEY_LEFT:
            print("Flecha Izquierda presionada")
        elif key == glfw.KEY_RIGHT:
            print("Flecha Derecha presionada")
        elif key == glfw.KEY_A:
            print("Tecla A presionada")
        elif key == glfw.KEY_B:
            print("Tecla B presionada")
        elif key == glfw.KEY_S:
            print("Tecla S presionada")
        elif key == glfw.KEY_W:
            print("Tecla W presionada")
        elif key == glfw.KEY_Z:
            print("Tecla Z presionada")
        elif key == glfw.KEY_SPACE:
            print("Espacio presionado")
        elif key == glfw.KEY_ENTER:
            print("Enter presionado")
        elif key == glfw.KEY_LEFT_SHIFT or key == glfw.KEY_RIGHT_SHIFT:
            print("Shift presionado")
        elif key == glfw.KEY_LEFT_CONTROL or key == glfw.KEY_RIGHT_CONTROL:
            print("Control presionado")
        elif key == glfw.KEY_F1:
            print("F1 presionado")
        elif key == glfw.KEY_F2:
            print("F2 presionado")
        elif key == glfw.KEY_F3:
            print("F3 presionado")
        elif key == glfw.KEY_F4:
            print("F4 presionado")
        elif key == glfw.KEY_F5:
            print("F5 presionado")
        elif key == glfw.KEY_F10:
            print("F10 presionado")
        elif key == glfw.KEY_F12:
            print("F12 presionado")
        elif key == glfw.KEY_0:
            print("Tecla 0 presionada")
        elif key == glfw.KEY_1:
            print("Tecla 1 presionada")
        elif key == glfw.KEY_2:
            print("Tecla 2 presionada")
        elif key == glfw.KEY_3:
            print("Tecla 3 presionada")
        elif key == glfw.KEY_4:
            print("Tecla 4 presionada")
        elif key == glfw.KEY_ESCAPE:
            print("Escape presionado - Cerrando ventana")
            glfw.set_window_should_close(window, True)
        


def dibujar_cuadro(x, tamanio):
    """
    La función `dibujar_cuadro` dibuja un cuadrado en la posición x con un tamaño específico.
    
    :param x: El parámetro `x` en la función `dibujar_cuadro` representa la coordenada x del
    Posición donde se dibujará el cuadrado. Determina la posición horizontal de la esquina superior izquierda.
    esquina del cuadrado en la pantalla o lienzo
    :param tamanio: El parámetro `tamanio` representa el tamaño del cuadrado que deseas dibujar. Es
    Se utiliza para determinar las dimensiones del cuadrado en relación con su posición `x`. el valor de
    `tamanio` determinará el ancho y alto del cuadrado

    """
    #Dibuja un cuadrado en la posición x.
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x, tamanio)
    glVertex2f(x + tamanio, tamanio)
    glVertex2f(x + tamanio, -tamanio)
    glVertex2f(x, -tamanio)
    glEnd()



def programa_principal():
    
    ventana = iniciar_ventana()
    # **********************************************
    # * ESTA LÍNEA ES CLAVE: Registro del Callback *
    # **********************************************
    glfw.set_key_callback(ventana, key_callback)
    
    while not glfw.window_should_close(ventana):
        # 1. Limpiar la pantalla con el color de fondo
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Dibujar el cuadro
        dibujar_cuadro(-0.5, 0.2)
        
        # Intercambiar búferes para mostrar el resultado
        glfw.swap_buffers(ventana)
        
        # Procesar eventos (clics, etc.)
        glfw.poll_events()
    
    glfw.terminate()


# LLamado al programa principal de control
if __name__ == "__main__":
    programa_principal()
