import urllib2
import json
import pygame, sys
from pygame.locals import *
import pprint
import time
#trying to get a change
try:
    import android
except ImportError:
    android = None

pygame.init()

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer

windowSurface = pygame.display.set_mode((1280, 770))

RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
LIGHT_BLUE = ((85, 190, 255))
LIGHT_GREEN = ((32, 255, 128))
PURPLE = ((236, 32, 255))
PINK = ((255, 32, 206))
WHITE = ((255, 255, 255))


city = "palo alto, ca"
pull = sys.argv

if len(pull) < 2:
    city = "palo alto"
else:
    city = (pull[1])

info = urllib2.urlopen('http://api.openweathermap.org/data/2.5/find?q={}&units=imperial'.format(city))
data = info.read()

j_data = json.loads(data)
count = (j_data["count"])

pprint.pprint(j_data)

if count > 1:
    print("Specify country")

pa_button = True
sc_button = True

palo_alto_pic = pygame.image.load("img/palo_alto.jpg")
weather_font = pygame.font.Font("fonts/animeace2_reg.ttf", 35)
weather_font_large = pygame.font.Font("fonts/animeace2_reg.ttf", 45)
wind_font = pygame.font.Font("fonts/animeace2_reg.ttf", 28)
title_font = pygame.font.Font("fonts/ASTONISH.TTF", 200)

pa_1 = pygame.Rect(90, 120, 40, 40)
pa_2 = pygame.Rect(90, 180, 40, 40)
sc_rect = pygame.Rect(70, 450, 40, 40)
pa_weather = pygame.draw.circle(windowSurface, RED, (150, 175), 100, 5)
sc_weather = pygame.draw.circle(windowSurface, LIGHT_BLUE, (150, 475), 100, 5)
menu = pygame.draw.circle(windowSurface, WHITE, (1100, 600), 100, 5)

picture_rect = pygame.Rect(100, 425, 900, 400)
title_rect = pygame.Rect(580, 10, 600, 100)
title_2_rect = pygame.Rect(640, 80, 600, 100)
description_rect = pygame.Rect(120, 10, 600, 100)
description2_rect = pygame.Rect(120, 60, 60, 100)
weather_rect = pygame.Rect(40, 110, 600, 100)
maximum_temp_rect = pygame.Rect(30, 160, 600, 100)
min_temp_rect = pygame.Rect(30, 210, 600, 100)
current_temperature_rect = pygame.Rect(60, 260, 600, 100)
wind_description_rect = pygame.Rect(2, 310, 600, 100)
day_rect = pygame.Rect(35, 360, 600, 100)
menu_rect = pygame.Rect(1040, 575, 40, 40)

max_temp = (j_data["list"][0]["main"]["temp_max"])
min_temp = (j_data["list"][0]["main"]["temp_min"])
current_temp = (j_data["list"][0]["main"]["temp"])
wind_speed = (j_data["list"][0]["wind"]["speed"])
gust = (j_data["list"][0]["wind"]["gust"])
date = (j_data["list"][0]["dt"])
time = time.ctime(date)

title = title_font.render("Weather", True, PURPLE)
title_2 = title_font.render("App", True, LIGHT_BLUE)
pa_1_text = weather_font.render("Palo", True, WHITE)
pa_2_text = weather_font.render("Alto", True, WHITE)
sc_text = wind_font.render("Capitola", True, LIGHT_GREEN)
menu_text = weather_font.render("Home", True, LIGHT_BLUE)
description = weather_font_large.render("The name of the city is " + j_data["list"][0]["name"], True, RED)
description_2 = weather_font_large.render("It is located in the country of " + j_data["list"][0]["sys"]["country"], True, RED)
weather = weather_font.render("The " + j_data["list"][0]["weather"][0]["description"], True, GREEN)
maximum_temp = weather_font.render("The maximum temperature today is {} degrees".format(max_temp), True, PURPLE)
minimum_temp = weather_font.render("The minimum temperature will be {} degrees".format(min_temp), True, PURPLE)
current_temperature = weather_font.render("The current temperature is {} degrees.".format(current_temp), True, LIGHT_BLUE)
wind_description = wind_font.render("There is a wind blowing at {} mph with gusts up to {} mph".format(gust, wind_speed), True, LIGHT_GREEN)
day = weather_font.render("The date is {}".format(time), True, PINK)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        mouse_pos = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            if pa_weather.collidepoint(mouse_pos):
                pa_button = False
                # pa_button_2 = False
            if sc_weather.collidepoint(mouse_pos):
                sc_button = False
            if menu.collidepoint(mouse_pos):
                pa_button = True
                sc_button = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


    if pa_button == True:
        windowSurface.fill((0,0,0))
        pa_weather = pygame.draw.circle(windowSurface, RED, (150, 175), 100, 5)
        windowSurface.blit(pa_1_text, pa_1)
        windowSurface.blit(pa_2_text, pa_2)
        sc_weather = pygame.draw.circle(windowSurface, LIGHT_BLUE, (150, 475), 100, 5)
        windowSurface.blit(sc_text, sc_rect)
        windowSurface.blit(title, title_rect)
        windowSurface.blit(title_2, title_2_rect)

    if pa_button == False:
        windowSurface.fill((0,0,0))
        windowSurface.blit(description, description_rect)
        windowSurface.blit(description_2, description2_rect)
        windowSurface.blit(weather, weather_rect)
        windowSurface.blit(maximum_temp, maximum_temp_rect)
        windowSurface.blit(minimum_temp, min_temp_rect)
        windowSurface.blit(current_temperature, current_temperature_rect)
        windowSurface.blit(wind_description, wind_description_rect)
        windowSurface.blit(day, day_rect)
        windowSurface.blit(palo_alto_pic, picture_rect)

        menu = pygame.draw.circle(windowSurface, WHITE, (1100, 600), 100, 5)
        windowSurface.blit(menu_text, menu_rect)

    if sc_button == False:
        windowSurface.fill((0,0,0))
        windowSurface.blit(title, title_rect)
        windowSurface.blit(title_2, title_2_rect)
        menu = pygame.draw.circle(windowSurface, WHITE, (1100, 600), 100, 5)
        windowSurface.blit(menu_text, menu_rect)




    pygame.display.update()



#print(pull[1])