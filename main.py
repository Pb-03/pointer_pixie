import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Pointer Pixie Dust")

# Colors
BG_COLOR = (10, 10, 30)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Particle class (Pixie Dust)
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(2, 5)
        self.color = (255, random.randint(180, 255), 255)
        self.life = random.randint(40, 80)
        self.vel = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]

    def update(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
        self.life -= 1
        if self.radius > 0:
            self.radius -= 0.05

    def draw(self, surface):
        if self.life > 0 and self.radius > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))


# Particle system
particles = []

# Main loop
running = True
while running:
    screen.fill(BG_COLOR)
    dt = clock.tick(FPS) / 1000  # Delta time (not critical here)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Spawn new particles at mouse
    for _ in range(3):  # Number of particles per frame (adjust for denser trail)
        particles.append(Particle(mouse_pos[0], mouse_pos[1]))

    # Update and draw particles
    for particle in particles:
        particle.update()
        particle.draw(screen)

    # Remove dead particles
    particles = [p for p in particles if p.life > 0 and p.radius > 0]

    # Update display
    pygame.display.flip()

pygame.quit()
