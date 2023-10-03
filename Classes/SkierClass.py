from Config import cfg
import pygame

#Building the class Skier
class Skier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #Attributes of the Skier
        self.direction = 0
        self.images_path = cfg.SKIER_IMAGE_PATH[:-1]
        self.image = pygame.image.load(self.images_path[self.direction]) #This will select a different image depend of the circumstance of moving left or right

        #Setting the rect of the Skier
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100] #Position Coordinate
        self.speed = [self.direction, 6 - abs(self.direction) * 2] #This define the position of the Skier when is changing
        
    #Actions of the Skier
    def turn(self, num):
        self.direction += num
        self.direction = max(-2, self.direction)
        self.direction = min(2, self.direction)
            
        center = self.rect.center
        self.image = pygame.image.load(self.images_path[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = [self.direction, 6 - abs(self.direction) * 2]
        return self.speed
    
    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centerx = max(20, self.rect.centerx)
        self.rect.centerx = min(620, self.rect.centerx)

    def setFall(self):
        self.image = pygame.image.load(cfg.SKIER_IMAGE_PATH[-1])
    
    def setForward(self):
        self.direction = 0
        self.image = pygame.image.load(self.images_path[self.direction])