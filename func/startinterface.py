from Config import cfg
import pygame, sys

def ShowStartInterface(screen, screen_size):
    screen.fill((255, 255, 255)) #White Background
    
    #Title rect and font
    title_font = pygame.font.Font(cfg.FONT_PATH, screen_size[0] // 5)
    title = title_font.render(u"Skier Game", True, (255, 0, 0))
    title_rect = title.get_rect()
    title_rect.midtop = (screen_size[0] / 2, screen_size[1] / 5)
    
    #Content rect and font
    content_font = pygame.font.Font(cfg.FONT_PATH, screen_size[0] // 20)
    content = content_font.render(u"Press any key to Start!", True, (0, 0, 255))
    content_rect = content.get_rect()
    content_rect.midtop = (screen_size[0] / 2, screen_size[1] / 2)
    
    #Update
    screen.blit(title, title_rect)
    screen.blit(content, content_rect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                return
            
        pygame.display.update()