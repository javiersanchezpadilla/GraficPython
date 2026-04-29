""" RELLENO DE POLIGONOS (inundación).

    Algoritmo de inundación (Flood fill)
    ------------------------------------
    ¿Cómo funciona el Algoritmo de Inundación?
    Imagina que tienes un dibujo de cualquier cosa (un poligono) en una hoja 
    Para rellenarlo, pones la punta del lápiz en un punto blanco dentro del
    dibujo y empiezas a pintar hacia afuera hasta chocar con el borde negro.

    Paso a paso:

    1)  Eliges un punto inicial (semilla) dentro del polígono.
    2)  Miras el color de ese punto.
    3)  Si el color es el 'color de fondo' (blanco), lo pintas con el 'color 
        nuevo' (rojo).
    4)  Repites el proceso para los vecinos (arriba, abajo, izquierda, derecha).

    Si chocas con un color que no es el de fondo (un borde), te detienes.

    Implementación de Flood Fill
    ----------------------------
    Como este es un algoritmo que trabaja a nivel de píxeles, usaremos una 
    matriz simple para representar nuestra pantalla. En aplicaciones reales con 
    OpenGL, esto es más complejo, pero este ejemplo te permitirá entender la 
    lógica perfectamente.

    Puntos clave para entender este código:
    ---------------------------------------
    1)  La Recursión: La función se llama a sí misma. Es como decirle a cada 
        píxel: 'Píntate y luego dile a tus vecinos que hagan lo mismo'.
    2)  El Límite (Borde): El algoritmo se detiene solo porque cuando llega a 
        una 'X' (el borde), la condición if pantalla[x][y] != color_fondo se 
        vuelve verdadera y deja de expandirse.
    3)  La 'Semilla': Es el punto (3, 3). Si pones la semilla fuera del 
        polígono, ¡se llenará toda la pantalla excepto el polígono!

    Limitación importante:
    -----------------------
    Este algoritmo es excelente para entender la lógica, pero en polígonos muy 
    grandes (como una pantalla 4K), la recursión puede ser tan profunda que la 
    computadora se quede sin memoria (error de Stack Overflow). Por eso, en 
    gráficos avanzados se usan versiones más complejas llamadas Scanline Fill, 
    que llenan el polígono línea por línea, como si fuera una persiana bajando.

"""
import time

def imprimir_pantalla(pantalla):
    """Muestra la matriz en la consola para ver el progreso."""
    for fila in pantalla:
        print(" ".join(fila))
    print("-" * 20)

def flood_fill(pantalla, x, y, color_fondo, color_nuevo):
    """
    Algoritmo de Inundación (Recursivo).
    x, y: coordenadas actuales.
    color_fondo: el color que queremos reemplazar (ej. '.').
    color_nuevo: el color que queremos poner (ej. '#').
    """
    # 1. Caso Base: Si estamos fuera de los límites de la pantalla
    if x < 0 or x >= len(pantalla) or y < 0 or y >= len(pantalla[0]):
        return

    # 2. Caso Base: Si el color no es el de fondo o ya está pintado
    if pantalla[x][y] != color_fondo:
        return

    # 3. Pintar el punto actual
    pantalla[x][y] = color_nuevo
    
    # (Opcional) Ver como se va llenando poco a poco
    imprimir_pantalla(pantalla) 
    time.sleep(0.5)

    # 4. Magia: Llamar a la función para los 4 vecinos (Recursión)
    flood_fill(pantalla, x + 1, y, color_fondo, color_nuevo) # Abajo
    flood_fill(pantalla, x - 1, y, color_fondo, color_nuevo) # Arriba
    flood_fill(pantalla, x, y + 1, color_fondo, color_nuevo) # Derecha
    flood_fill(pantalla, x, y - 1, color_fondo, color_nuevo) # Izquierda

# --- PRUEBA DEL ALGORITMO ---

# Creamos una 'pantalla' de 7x7 con un borde de 'X' y fondo de '.'
mi_pantalla = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', '.', '.', '.', '.', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
]

print("Pantalla inicial (vacía):")
imprimir_pantalla(mi_pantalla)

# Iniciamos el relleno en el centro (3, 3)
print("Iniciando relleno...")
flood_fill(mi_pantalla, 3, 3, '.', '#')

print("Resultado final:")
imprimir_pantalla(mi_pantalla)
