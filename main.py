import pygame
import sys
import random

pygame.init()

WIDTH = 1024
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tibran Simulator")

SPACE_BLACK = (5, 5, 12)
STAR_WHITE = (240, 240, 255)

star_list =[]
for i in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    star_list.append((x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(SPACE_BLACK)




    for star in star_list:
        pygame.draw.circle(screen, STAR_WHITE, star, 2)


    pygame.display.flip()
