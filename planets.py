import pygame 
import random



planet_images = []
planet_coordinates = []

planets = {
    
}



for i in range(1,11):
    x = random.randrange(10,1200)
    y = random.randrange(-3000,600)
    vel = random.randrange(1,2)
    planet_images.append(pygame.image.load(f"assets/images/planet{i}.png"))
    planet_coordinates.append([x,y,vel])
   

class LoadPlanet:
    def __init__(self,**kwargs):
        super(LoadPlanet,self).__init__(**kwargs)
        pass

    def load_planets(self,screen):
        global rotx
        for image in planet_images:
            index = planet_images.index(image)
            planet_coordinates[index][1] += planet_coordinates[index][2]
        

            screen.blit(image,(planet_coordinates[index][0],planet_coordinates[index][1]))



            if planet_coordinates[index][1] > 700:
                planet_coordinates[index][1] = random.randrange(-8000,-1000)
                planet_coordinates[index][0] = random.randrange(10,1200)
        
