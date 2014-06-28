import urllib2
import json
import pygame
import datetime
from global_values import windowSurface


class Weather():
    def __init__(self, city):
        import time
        self.city = city
        self.open_network()
        weather_font_large = pygame.font.Font("fonts/animeace2_reg.ttf", 45)
        weather_font = pygame.font.Font("fonts/animeace2_reg.ttf", 35)

        wind_font = pygame.font.Font("fonts/animeace2_reg.ttf", 28)

        RED = ((255, 0, 0))
        GREEN = ((0, 255, 0))
        LIGHT_BLUE = ((85, 190, 255))
        LIGHT_GREEN = ((32, 255, 128))
        PURPLE = ((236, 32, 255))
        PINK = ((255, 32, 206))

        if self.connected:
            data = self.info.read()
            j_data = json.loads(data)
            max_temp = (j_data["main"]["temp_max"])
            min_temp = (j_data["main"]["temp_min"])
            current_temp = (j_data["main"]["temp"])
            wind_speed = (j_data["wind"]["speed"])
            date = (j_data["dt"])
            current_time = time.ctime(date)
            s_time = int(j_data["sys"]["sunrise"])
            sunset_time = int(j_data["sys"]["sunset"])
            sunrise_time = datetime.datetime.fromtimestamp(s_time).strftime('%H:%M')
            sunset_time = datetime.datetime.fromtimestamp(sunset_time).strftime('%H:%M')

            self.description = weather_font_large.render("The name of the city is " + j_data["name"], True, RED)
            self.description_2 = wind_font.render("It is located in the country of " + j_data["sys"]["country"], True, RED)
            self.weather = weather_font.render(j_data["weather"][0]["description"], True, GREEN)
            self.maximum_temp = weather_font.render("The maximum temperature today is {} degrees".format(max_temp), True, PURPLE)
            self.minimum_temp = weather_font.render("The minimum temperature will be {} degrees".format(min_temp), True, PURPLE)
            self.current_temperature = weather_font.render("The current temperature is {} degrees.".format(current_temp), True, LIGHT_BLUE)
            self.wind_description = wind_font.render("There is a wind blowing at {} mph ".format(wind_speed), True, LIGHT_GREEN)
            self.day = weather_font.render("The date is {}".format(current_time), True, PINK)
            self.sunrise_text = weather_font.render("The sun rises at {} and sets at {}".format(sunrise_time, sunset_time), True, LIGHT_BLUE)

            self.description_rect = pygame.Rect(120, 10, 600, 100)
            self.description2_rect = pygame.Rect(60, 60, 60, 100)
            self.weather_rect = pygame.Rect(300, 110, 600, 100)
            self.maximum_temp_rect = pygame.Rect(30, 160, 600, 100)
            self.min_temp_rect = pygame.Rect(30, 210, 600, 100)
            self.current_temperature_rect = pygame.Rect(60, 260, 600, 100)
            self.wind_description_rect = pygame.Rect(2, 310, 600, 100)
            self.day_rect = pygame.Rect(35, 360, 600, 100)
            self.menu_rect = pygame.Rect(1040, 575, 40, 40)
            self.sunrise_rect = pygame.Rect(50, 410, 600, 100)

    def draw(self):
        # main_surface = pygame.Surface((1280, 770))

        windowSurface.blit(self.description, self.description_rect)
        windowSurface.blit(self.description_2, self.description2_rect)
        windowSurface.blit(self.weather, self.weather_rect)
        windowSurface.blit(self.maximum_temp, self.maximum_temp_rect)
        windowSurface.blit(self.minimum_temp, self.min_temp_rect)
        windowSurface.blit(self.current_temperature, self.current_temperature_rect)
        windowSurface.blit(self.wind_description, self.wind_description_rect)
        windowSurface.blit(self.day, self.day_rect)
        windowSurface.blit(self.sunrise_text, self.sunrise_rect)

    def open_network(self):
        self.connected = True
        try:
            self.info = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial'.format(self.city))
        except IOError:
            self.connected = False

