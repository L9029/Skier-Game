from Classes import *
from func import *
from Config import *
import pygame, sys

def main():
    #Initilization of pygame methods
    pygame.init()
    
    #Settings of the music
    pygame.mixer.init()
    pygame.mixer.music.load(cfg.BGM_PATH)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    #Settings of the Screen
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption("Skier Game")
    ShowStartInterface(screen, cfg.SCREENSIZE)
    
    #Settings of Obstacles and Skier
    skier = Skier()
    
    obstacles0 = createObstacles(20, 29)
    obstacles1 = createObstacles(10, 19)
    obstaclesFlag = 0
    
    obstacles = addObstacles(obstacles0, obstacles1)
    
    #Settings of the Clock
    clock = pygame.time.Clock()
    
    distance = 0
    score = 0
    speed = [0, 6]
    
if __name__ == "__main__":
    main()