import pygame,random
import json

data = open("DIMENSIONS.json",'r')
json_data = json.loads(data.read())

DIMENSIONS = (json_data['width'],json_data['height'])

STARS_NUM = 200
star_lists = []

FLOW_SPEEDY = 1
FLOW_SPEEDX = 0.5

for i in range(STARS_NUM):
    star_lists.append([random.randrange(0,DIMENSIONS[0]),random.randrange(0,DIMENSIONS[1]),random.randrange(1,4),random.randrange(-1,2)])


def draw_stars(screen):
    for star in star_lists:
        star[0] += star[3]
        star[1] += FLOW_SPEEDY
        pygame.draw.circle(screen, (255, 255, 255),(star[0], star[1]),star[2])

        if star[0] >= DIMENSIONS[0]:
            star[0] = 0
        
        if star[1] >= DIMENSIONS[1]:
            star[1] = 0
