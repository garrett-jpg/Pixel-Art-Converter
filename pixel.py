import pygame
from pygame.locals import *


pygame.init()


pixel_image = "farmers-market.jpg"  # Replace with the path to your image
original_image = pygame.image.load(pixel_image)


pixel_size = 10


resized_image = pygame.transform.scale(original_image, (original_image.get_width() // pixel_size, original_image.get_height() // pixel_size))


pixel_art_surface = pygame.Surface(original_image.get_size())


for x in range(0, original_image.get_width(), pixel_size):
    for y in range(0, original_image.get_height(), pixel_size):
        color = original_image.get_at((x, y))
        pygame.draw.rect(pixel_art_surface, color, (x, y, pixel_size, pixel_size))


screen = pygame.display.set_mode(original_image.get_size())
pygame.display.set_caption("Pixel Art Converter")
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(pixel_art_surface, (0, 0))
    pygame.display.flip()

pygame.quit()