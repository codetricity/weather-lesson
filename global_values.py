import pygame

pygame.init()

SCREENSIZE = (1280, 770)
windowSurface = pygame.display.set_mode(SCREENSIZE)

RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
LIGHT_BLUE = ((85, 190, 255))
LIGHT_GREEN = ((32, 255, 128))
PURPLE = ((236, 32, 255))
PINK = ((255, 32, 206))
WHITE = ((255, 255, 255))

sorry_font = pygame.font.Font("fonts/ASTONISH.TTF", 150)

palo_alto_pic = pygame.image.load("img/palo_alto.jpg")
weather_font = pygame.font.Font("fonts/animeace2_reg.ttf", 35)
weather_font_large = pygame.font.Font("fonts/animeace2_reg.ttf", 45)
wind_font = pygame.font.Font("fonts/animeace2_reg.ttf", 28)
title_font = pygame.font.Font("fonts/ASTONISH.TTF", 200)

