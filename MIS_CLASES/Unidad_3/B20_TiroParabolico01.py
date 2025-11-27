""" El código es un tiro parabolico pero no funciona"""


import sys
import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5               

# Colores (RGBA)
WHITE = (1, 1, 1, 1)
RED   = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)
BLUE  = (0, 0, 1, 1)
BLACK = (0, 0, 0, 1)

class Projectile:
    
    def __init__(self, x, y, angle, power):
        self.x = x
        self.y = y
        self.angle = math.radians(angle)
        self.power = power
        self.vx = power * math.cos(self.angle)
        self.vy = -power * math.sin(self.angle)   # negativo porque OpenGL tiene y ↑ ↑
        self.active = True

    def update(self):
        if not self.active:
            return
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY
        # Colisión con suelo o bordes
        if self.y < -1 or self.x < -1 or self.x > 1:
            self.active = False

    def draw(self):
        if not self.active:
            return
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glColor4fv(RED)
        gluDisk(gluNewQuadric(), 0, 0.02, 16, 1)
        glPopMatrix()

class Enemy:
    """Enemigo estático con animación de 8 frames (cambio de color)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0  # 0‑7

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        # Cada frame tiene un color diferente (rojo → azul)
        r = 1 - self.frame / 7.0
        g = self.frame / 7.0
        b = self.frame / 7.0
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glColor4f(r, g, b, 1)
        gluDisk(gluNewQuadric(), 0, 0.05, 16, 1)
        glPopMatrix()

class Explosion:
    """Animación de explosión (8 frames)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.max_frames = 8

    def update(self):
        self.frame += 1

    def draw(self):
        if self.frame >= self.max_frames:
            return
        size = 0.02 + 0.08 * (self.frame / self.max_frames)
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glColor4f(1, 0.5, 0, 1)  # naranja
        gluDisk(gluNewQuadric(), 0, size, 16, 1)
        glPopMatrix()

    @property
    def finished(self):
        return self.frame >= self.max_frames

def draw_text(x, y, text):
    """Renderiza texto en la ventana OpenGL."""
    glWindow2d(WIDTH, HEIGHT)
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def draw_cannon(angle):
    """Dibuja el cañón en la esquina inferior izquierda."""
    glPushMatrix()
    glTranslatef(-0.9, -0.9, 0)
    glRotatef(angle, 0, 0, 1)
    glColor4fv(BLACK)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(0.1, 0)
    glEnd()
    glPopMatrix()

def reset_game():
    global cannon_angle, cannon_power, lives, projectiles, enemies, explosions
    cannon_angle = 45
    cannon_power = 50
    lives = 3
    projectiles = []
    enemies = [Enemy(random.uniform(-0.8, 0.8), random.uniform(0.2, 0.8)) for _ in range(5)]
    explosions = []

import random
pygame.init()
display = (WIDTH, HEIGHT)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
glClearColor(0.2, 0.3, 0.4, 1.0)

# Variables de juego
reset_game()

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cannon_angle = min(90, cannon_angle + 5)
            elif event.key == pygame.K_DOWN:
                cannon_angle = max(0, cannon_angle - 5)
            elif event.key == pygame.K_RIGHT:
                cannon_power = min(100, cannon_power + 5)
            elif event.key == pygame.K_LEFT:
                cannon_power = max(10, cannon_power - 5)
            elif event.key == pygame.K_SPACE:
                projectiles.append(Projectile(-0.9, -0.9, cannon_angle, cannon_power / 10))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Apuntar con ratón (convierte coordenadas de pantalla a OpenGL)
            mx, my = event.pos
            # Normaliza a [-1, 1]
            ox = (mx / WIDTH) * 2 - 1
            oy = -(my / HEIGHT) * 2 + 1
            dx, dy = ox - (-0.9), oy - (-0.9)
            cannon_angle = math.degrees(math.atan2(dy, dx))

    # Actualizar objetos
    for p in projectiles:
        p.update()
    for e in enemies:
        e.update()
    for ex in explosions:
        ex.update()
    explosions = [ex for ex in explosions if not ex.finished]

    # Colisiones
    for p in projectiles[:]:
        for e in enemies[:]:
            if (p.x - e.x) ** 2 + (p.y - e.y) ** 2 < 0.01:
                p.active = False
                e.x = random.uniform(-0.8, 0.8)
                e.y = random.uniform(0.2, 0.8)
                explosions.append(Explosion(e.x, e.y))
                break

    # Dibujar
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cannon(cannon_angle)
    for p in projectiles:
        p.draw()
    for e in enemies:
        e.draw()
    for ex in explosions:
        ex.draw()

    # Texto en consola (para cumplir con “visualización de texto en consola”)
    print(f"\rVidas: {lives} | Ángulo: {cannon_angle}° | Fuerza: {cannon_power} ", end='')

    # Texto en pantalla (OpenGL)
    glColor4fv(WHITE)
    draw_text(10, 580, f"Vidas: {lives}")
    draw_text(10, 560, f"Ángulo: {cannon_angle}°")
    draw_text(10, 540, f"Fuerza: {cannon_power}")
    draw_text(10, 520, "↑/↓ ángulo | ←/→ fuerza | Espacio disparar")

    pygame.display.flip()
