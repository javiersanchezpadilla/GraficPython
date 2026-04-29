# Algoritmo de Relleno por Barrido de Líneas (Scanline) en Software

import math

# --- 1. Configuración del Lienzo (Canvas) ---
# Tamaño de la matriz de píxeles
ANCHO = 80
ALTO = 40
PIXEL_VACIO = ' ' # Píxel que representa el fondo
PIXEL_RELLENO = '#' # Píxel que representa el color del polígono

# El lienzo es una matriz bidimensional (lista de listas)
CANVAS = [[PIXEL_VACIO for _ in range(ANCHO)] for _ in range(ALTO)]

# --- 2. Definición del Polígono ---

# Definimos un polígono de 4 vértices (una forma irregular)
# Los vértices son tuplas (x, y)
POLIGONO = [
    (10, 5),   # A
    (70, 15),  # B
    (50, 35),  # C
    (30, 25)   # D
]

# --- 3. Funciones del Algoritmo Scanline ---

def obtener_intersecciones(poligono, y_actual):
    """
    Paso 1: Encuentra las coordenadas X donde la línea de barrido (y_actual)
    cruza los bordes del polígono.
    """
    intersecciones_x = []
    num_vertices = len(poligono)

    # Recorrer todos los bordes (aristas) del polígono
    for i in range(num_vertices):
        # Vértice inicial del borde
        p1 = poligono[i]
        # Vértice final del borde (el último se conecta con el primero)
        p2 = poligono[(i + 1) % num_vertices]

        y1, y2 = p1[1], p2[1]
        x1, x2 = p1[0], p2[0]
        
        # Nos aseguramos de que el borde cruce la línea y_actual.
        # Debe estar entre el Y más pequeño y el Y más grande del borde.
        if (y_actual >= min(y1, y2) and y_actual < max(y1, y2)):
            # Cálculo de la intersección X (Interpolación lineal):
            # x_interseccion = x1 + (x2 - x1) * (y_actual - y1) / (y2 - y1)
            
            # Evitar división por cero si el borde es horizontal (y1 == y2)
            if (y2 - y1) != 0:
                x_inter = x1 + (x2 - x1) * (y_actual - y1) / (y2 - y1)
                intersecciones_x.append(int(round(x_inter)))
    
    # Ordenar las intersecciones de menor a mayor X
    intersecciones_x.sort()
    return intersecciones_x

def rellenar_scanline(intersecciones_x, y):
    """
    Paso 2: Rellena los píxeles en el lienzo entre pares de intersecciones.
    """
    # Recorrer la lista en pasos de 2 (pares: entrada y salida)
    for i in range(0, len(intersecciones_x), 2):
        x_inicio = intersecciones_x[i]
        
        # Manejar el caso de un polígono degenerado o impar (debe ser siempre par)
        if i + 1 >= len(intersecciones_x):
            continue 
            
        x_fin = intersecciones_x[i+1]

        # Rellenar desde el punto de entrada hasta el punto de salida
        for x in range(x_inicio, x_fin):
            # Asegurarse de no dibujar fuera de los límites del lienzo
            if 0 <= x < ANCHO and 0 <= y < ALTO:
                CANVAS[y][x] = PIXEL_RELLENO


def ejecutar_scanline_fill():
    """Bucle principal que aplica el algoritmo línea por línea."""
    
    # 1. Encontrar los límites Y del polígono
    min_y = min(p[1] for p in POLIGONO)
    max_y = max(p[1] for p in POLIGONO)
    
    # Asegurarse de que los límites estén dentro del lienzo
    min_y = max(0, min_y)
    max_y = min(ALTO - 1, max_y)

    print(f"Iniciando relleno desde Y={min_y} hasta Y={max_y}")

    # 2. Bucle principal: Recorrer de arriba a abajo
    for y_actual in range(min_y, max_y + 1):
        # A. Obtener puntos de intersección X para la línea Y_actual
        intersecciones = obtener_intersecciones(POLIGONO, y_actual)
        
        # B. Rellenar los segmentos horizontales
        rellenar_scanline(intersecciones, y_actual)

# --- 4. Ejecución y Visualización ---

if __name__ == "__main__":
    ejecutar_scanline_fill()

    # Imprimir el lienzo resultante en la consola
    print("\n--- Resultado del Relleno Scanline (Canvas) ---")
    for fila in reversed(CANVAS): # Invertir el eje Y para que (0,0) esté abajo (como en OpenGL)
        print("".join(fila))
    print("---------------------------------------------")

    print(f"\nPolígono Usado: {POLIGONO}")