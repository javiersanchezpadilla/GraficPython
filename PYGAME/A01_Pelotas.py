""" Simulación de pelotas callendo"""

import pygame
import random

# Inicializamos Pygame
pygame.init()

# Definimos las propiedades de la ventana
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Cremos las pelotas
num_balls = 10
balls = [
    {
        'x': random.uniform(20, width - 20),
        'y': 20,
        'vx': random.uniform(-5, 5),
        'vy': random.uniform(-5, 5),
        'color': (random.randint(0, 255), 
                  random.randint(0, 255), 
                  random.randint(0, 255)),
        'radius': 10,
        'active': True
    } for _ in range(num_balls)
]

# Definicion de los valores de la gravedad y el rebote
gravedad = 0.5
factor_rebote = 0.8
limite_velocidad = 0.1
friccion = 0.99

ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # Actualizamos la posición de las pelotas
    for ball in balls:
        if not ball['active']:
            continue

        ball['vy'] += gravedad
        ball['x'] += ball['vx']
        ball['y'] += ball['vy']

        if (ball['x'] <= ball['radius']
            or ball['x'] >= width - ball['radius']):
            ball['vx'] *= -factor_rebote
            ball['x'] = max(ball['radius'], 
                        min(width - ball['radius'],
                        ball['x']))

        if ball['y'] >= height - ball['radius']:
            ball['y'] = height - ball['radius']
            ball['vy'] *= -factor_rebote
            ball['vx'] *= friccion
            if (abs(ball['vy']) < limite_velocidad
            and abs(ball['vx']) < limite_velocidad):
                ball['vy'] = 0
                ball['vx'] = 0
                ball['active'] = False
        

    # Dibujamos todo
    screen.fill((0, 0, 0))
    for ball in balls:
        pygame.draw.circle(screen, ball['color'], 
                    (int(ball['x']), int(ball['y'])), ball['radius'])
    
    pygame.display.flip()
    clock.tick(60)



# cerramos la ventana
pygame.quit()