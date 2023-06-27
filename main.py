import pygame
import random
from planets import LoadPlanet
from shuttle import LoadShuttle
from stars import draw_stars
import json

pygame.init()

data = open("DIMENSIONS.json",'r')
json_data = json.loads(data.read())

DIMENSIONS = (json_data['width'],json_data['height'])




screen = pygame.display.set_mode(DIMENSIONS)
clock = pygame.time.Clock()
shuttle = LoadShuttle()
planets = LoadPlanet()
FPS = 45

running = True 

while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    

    clock.tick(FPS)
    draw_stars(screen)
    planets.load_planets(screen)
    shuttle.load_shuttle(screen)


    pygame.display.update()
