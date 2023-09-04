from Config import cfg
import pygame

#Document this
class Skier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.direction = 0
        self.images_path = cfg.SKIER_IMAGE_PATH[:-1]
        self.image = pygame.image.load(self.images_path[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.speed = [self.direction, 6 - abs(self.direction) * 2]