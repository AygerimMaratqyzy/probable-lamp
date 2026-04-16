import pygame
import sys
from clock import MickeyClock

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

# Create clock logic
mickey_clock = MickeyClock(WIDTH, HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    # Draw everything
    mickey_clock.update()
    mickey_clock.draw(screen)

    pygame.display.flip()
    clock.tick(60)