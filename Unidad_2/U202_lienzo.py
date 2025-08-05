""" Preparando el lienzo
    Antes de poder dibujar algo, necesitamos un lugar donde hacerlo, 
    En nuestro caso, ese "lugar" es una ventana en la pantalla de nuestro 
    ordenador. Piénsalo como si tuvieras que comprar un lienzo en blanco 
    antes de empezar a pintar.

    Para crear y gestionar esta ventana, la mayoría de la gente usa una biblioteca 
    de Python llamada Pygame o PyOpenGL. Vamos a usar Pygame, ya que es muy fácil de entender y usar.

    Aquí tienes un ejemplo de cómo se vería el código para crear nuestra ventana:"""

# Importamos la biblioteca que nos ayuda a crear la ventana
import pygame

# Inicializamos Pygame para que todo funcione, es como encender el interruptor de la luz
pygame.init()

# Creamos una ventana de 800 píxeles de ancho por 600 de alto
# y le damos un título
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi primera ventana de OpenGL")


# Este es el "bucle principal" del programa.
# Es como el motor que mantiene la ventana abierta y escuchando
# hasta que la cerremos
running = True
while running:
    # Este bucle revisa si hemos hecho clic en el botón de cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aquí es donde pintaríamos cosas en la ventana
    # (¡esto lo veremos más adelante!)
    
    # Esto actualiza la pantalla para que veamos los cambios
    # esta linea lanza los dibujos realizados a la pantalla
    pygame.display.flip()

# Cerramos Pygame al final
pygame.quit()
