import pygame
from gamelib.gameobject import *

class Screen(GameObject):
    def __init__(self,screen,objects=[]):
        GameObject.__init__(self)
        self.screen = screen
        self.objects = objects

        self.sceneView = pygame.Surface((700,600))
        self.sceneView.fill((0,0,255))
        self.controls = pygame.Surface((100,600))
        self.controls.fill((255,255,255))

    def draw(self,pos):
        self.screen.blit(self.sceneView
                        ,pygame.Rect(pos.x
                                    ,pos.y
                                    ,self.sceneView.get_width()
                                    ,self.screen.get_height()))

        self.screen.blit(self.controls
                        ,pygame.Rect(pos.x+700
                                    ,pos.y
                                    ,100
                                    ,self.screen.get_height()))
