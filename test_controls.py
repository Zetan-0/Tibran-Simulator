import pygame
import sys
import random
import math

pygame.init()

WIDTH = 1024
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tibran Simulator")
clock = pygame.time.Clock()

SPACE_BLACK = (5, 5, 12)
STAR_WHITE = (240, 240, 255)

img1 = pygame.image.load("Visual Assets/galaxy.png").convert_alpha()
img2 = pygame.image.load("Visual Assets/galaxy2.png").convert_alpha()
img3 = pygame.image.load("Visual Assets/galaxy3.png").convert_alpha()

bg_number = random.randint(1,6)
bg_filename = f"Visual Assets/cosmic_background{bg_number}.jpg"

bg_image = pygame.image.load(bg_filename).convert()
bg_surface = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

galaxy_sprites = [
    pygame.transform.scale(img1, (24, 24)),
    pygame.transform.scale(img2, (24, 24)),
    pygame.transform.scale(img3, (24, 24))
]

star_list =[]
while len(star_list) < 100:
    x = random.randint(20, WIDTH - 20)
    y = random.randint(20, HEIGHT - 20)
    

    too_close = False
    for star in star_list:
        distance = math.hypot(x - star[0], y -star[1])
        if distance < 45:
            too_close = True
            break


    if not too_close:

        chosen_sprite = random.choice(galaxy_sprites)
        star_list.append((x, y, chosen_sprite))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                
                new_sprite = random.choice(galaxy_sprites)

                
                star_list.append((mouse_x, mouse_y, new_sprite))


    screen.fill(SPACE_BLACK)
   
    screen.blit(bg_surface, (0, 0))


    for star in star_list:
        x_pos = star[0]
        y_pos = star[1]
        sprite = star[2]
        screen.blit(sprite, (x_pos - 12, y_pos - 12))


    pygame.display.flip()




    clock.tick(60)
