from Config import cfg
from Classes import *
import random, pygame

def createObstacles(s, e, num=10):
    obstacles = pygame.sprite.Group()
    locations = []
    
    for i in range(num):
        row = random.randint(s, e)
        col = random.randint(0, 9)
        location = [col * 64 + 20, row * 64 + 20]
        
        if location not in locations:
            locations.append(location)
            attribute = random.choice(list(cfg.OBSTACLE_PATH.keys()))
            image_path = cfg.OBSTACLE_PATH[attribute]
            obstacle = Obstacle(image_path, location, attribute)
            obstacles.add(obstacle)
    
    return obstacles

def addObstacles(obstacles0, obstacles1):
    obstacles = pygame.sprite.Group()
    
    for obstacle in obstacles0:
        obstacles.add(obstacle)
    
    for obstacle in obstacles1:
        obstacles.add(obstacle)
    
    return obstacles