from Config import cfg
import pygame

#Content of the Score
def showScore(screen, score, pos=(10, 10)):
    font = pygame.font.Font(cfg.FONT_PATH, 30)
    score_text = font.render("Score: %s" % score, True, (0, 0, 0))
    screen.blit(score_text, pos)