import pygame
import os
from pygame.locals import *
from gamelib.gameobject import GameObject
from gamelib.game import Game
from gamelib.input import Input
from gamelib.collider import BoxCollider

class WinScene(GameObject):
    def __init__(self):
        GameObject.__init__(self)

    def draw(self,pos,screen):
        screen.fill((0,0,0))
        if pygame.font.get_default_font():
            fontname = pygame.font.get_default_font()
            font = pygame.font.SysFont(fontname,50)
            smallFont = pygame.font.SysFont(fontname,30)
            fontSurface = font.render("You Won",True,(255,255,255))
            text = smallFont.render("- Press space to go to title -",True,(255,255,255))
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
            Game.loadSceneByName("StartScene")

class WinFlag(GameObject):
    def __init__(self,position):
        GameObject.__init__(self)
        self.name = "WinStar"
        self.position = position
        self.image = pygame.image.load(os.path.join("images","star.jpg"))
        self.rect = pygame.Rect(self.position.x-self.image.get_width()/2
                                           ,self.position.y-self.image.get_height()/2
                                           ,self.image.get_width()
                                           ,self.image.get_height())

        self.collider = BoxCollider(self.rect)

    def draw(self,pos,screen):
        screen.blit(self.image,pygame.Rect(pos.x,pos.y,self.rect.width,self.rect.height))

    def onCollision(self,col,obj):
        if obj.name == "Player":
            Game.loadSceneByName("WinScene")
