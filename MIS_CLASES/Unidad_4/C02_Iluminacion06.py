""" Para consultar el numero maximo de luces que soporta la tarjeta grafica de nuestra
    computadora.

    Costo de Rendimiento:
    Cada luz adicional tiene costo computacional. Orden aproximado de costo:

    Luces direccionales (w=0.0): Más baratas
    Luces posicionales (w=1.0): Intermedio
    Luces con foco (spot): Más caras
    Luces con atenuación: Aún más caras (mayor procesamiento).
"""

# OpenGL garantiza mínimo 8 luces, pero algunas tarjetas soportan más
import OpenGL
from OpenGL.GL import *

# Puedes consultar el límite máximo
max_luces = glGetIntegerv(GL_MAX_LIGHTS)
print(f"Esta tarjeta soporta hasta {max_luces} luces")  # Típicamente 8