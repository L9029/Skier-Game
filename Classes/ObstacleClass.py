from Config import cfg
import pygame

#Building the Obstacles of the game
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_path, location, attribute):
        pygame.sprite.Sprite.__init__(self)
        
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        self.attribute = attribute
        self.passed = False
    
    def move(self, num):
        self.rect.centery = self.location[1] - num