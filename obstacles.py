import pygame
from vector2 import Vector2
from gameobject import GameObject

class Box(GameObject):
    def __init__(self,screen):
        GameObject.__init__(self)
        self.position.x = 700
        self.position.y = 500

        self.screen = screen

        self.height = 50
        self.width = 80

    def draw(self):
        pygame.draw.rect(self.screen,(255,255,255)
                        ,pygame.Rect(self.position.x-self.width/2
                                    ,self.position.y-self.height
                                    ,self.width
                                    ,self.height)
                        ,3)

    def update(self):
        self.draw()
