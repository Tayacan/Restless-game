import pygame
from pygame.locals import *
from gamelib.gameobject import GameObject
from gamelib.game import Game
from gamelib.input import Input

class StartScreen(GameObject):
    def __init__(self,screen):
        GameObject.__init__(self)
        self.screen = screen

    def draw(self,pos):
        self.screen.fill((0,0,0))
        if pygame.font.get_default_font():
            fontname = pygame.font.get_default_font()
            font = pygame.font.SysFont(fontname,50)
            smallFont = pygame.font.SysFont(fontname,30)
            fontSurface = font.render("Restless",True,(255,255,255))
            text = smallFont.render("- Press space to start -",True,(255,255,255))
            rect = fontSurface.get_rect()
            smallRect = text.get_rect()
            self.screen.blit(fontSurface,pygame.Rect((self.screen.get_width()-rect.width)/2
                                              ,(self.screen.get_height()-rect.height)/2
                                              ,rect.width
                                              ,rect.height))
            self.screen.blit(text,pygame.Rect((self.screen.get_width()-smallRect.width)/2
                                              ,(self.screen.get_height()+rect.height)/2
                                              ,smallRect.width
                                              ,smallRect.height))

    def update(self):
        if Input.down(K_SPACE):
            Game.loadSceneByName("Main")
