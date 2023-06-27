import pygame 
import random ,json

data = open("DIMENSIONS.json",'r')
json_data = json.loads(data.read())

DIMENSIONS = (json_data['width'],json_data['height'])

shuttle = pygame.image.load("assets/images/shuttle.png")
dx = 0
shuttle = pygame.transform.scale(shuttle,(60,60))
posx = DIMENSIONS[0]/2
posy = DIMENSIONS[1]/2

class LoadShuttle:
    def load_shuttle(self,screen):
        global posx,dx 
        
        for event in pygame.event.get():
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    dx -= 1.5
                
                if event.key == pygame.K_d:
                    dx += 1.5
            
            if event.type == pygame.KEYUP:
                dx = 0


        screen.blit(shuttle,(posx,posy))
        posx += dx


