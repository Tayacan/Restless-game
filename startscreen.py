import pygame
from pygame.locals import *
from gamelib.gameobject import GameObject
from gamelib.game import Game
from gamelib.input import Input

class StartScreen(GameObject):
    def __init__(self):
        GameObject.__init__(self)

    def draw(self,pos,screen):
        screen.fill((0,0,0))
        if pygame.font.get_default_font():
            fontname = pygame.font.get_default_font()
            font = pygame.font.SysFont(fontname,50)
            smallFont = pygame.font.SysFont(fontname,30)
            fontSurface = font.render("Restless",True,(255,255,255))
            text = smallFont.render("- Press space to start -",True,(255,255,255))
            rect = fontSurface.get_rect()
            smallRect = text.get_rect()
            screen.blit(fontSurface,pygame.Rect((screen.get_width()-rect.width)/2
                                              ,(screen.get_height()-rect.height)/2
                                              ,rect.width
                                              ,rect.height))
            screen.blit(text,pygame.Rect((screen.get_width()-smallRect.width)/2
                                              ,(screen.get_height()+rect.height)/2
                                              ,smallRect.width
                                              ,smallRect.height))

    def update(self):
        if Input.down(K_SPACE):
            Game.loadSceneByName("Test")
