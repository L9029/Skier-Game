from Classes import *
import pygame
from .score import *

#Update the Frames of the game
def updateFrame(screen, obstacles, skier, score):
    screen.fill((255, 255, 255)) #White Background
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    showScore(screen, score)
    
    pygame.display.update()