# import pygame, sys, time
#
# class Weather():
#     def __init__(self, city):
#         self.city = city
#         weather_font = pygame.font.Font("fonts/animeace2_reg.ttf", 35)
#         weather_font_large = pygame.font.Font("fonts/animeace2_reg.ttf", 45)
#         wind_font = pygame.font.Font("fonts/animeace2_reg.ttf", 28)
#         title_font = pygame.font.Font("fonts/ASTONISH.TTF", 200)
#         description = weather_font_large.render("The name of the city is " + j_data["name"], True, RED)
#         description_2 = weather_font_large.render("It is located in the country of " + j_data["sys"]["country"], True, RED)
#         weather = weather_font.render("The " + j_data["weather"][0]["description"], True, GREEN)
#         maximum_temp = weather_font.render("The maximum temperature today is {} degrees".format(max_temp), True, PURPLE)
#         minimum_temp = weather_font.render("The minimum temperature will be {} degrees".format(min_temp), True, PURPLE)
#         current_temperature = weather_font.render("The current temperature is {} degrees.".format(current_temp), True, LIGHT_BLUE)
#         wind_description = wind_font.render("There is a wind blowing at {} mph ".format(wind_speed), True, LIGHT_GREEN)
#         day = weather_font.render("The date is {}".format(time), True, PINK)
#         sunrise_text = weather_font.render("The sun rises at {} and sets at {}".format(s_time, sunset_time), True, LIGHT_BLUE)