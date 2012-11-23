import pygame
from vector2 import Vector2
from gameobject import GameObject
from collider import BoxCollider

class Box(GameObject):
    def __init__(self,screen):
        GameObject.__init__(self)
        self.position.x = 700
        self.position.y = 500

        self.collider = BoxCollider([Vector2(660,450)
                                    ,Vector2(660,500)
                                    ,Vector2(740,500)
                                    ,Vector2(740,450)])

        self.screen = screen

        self.height = 50
        self.width = 80

    def draw(self,pos):
        pygame.draw.rect(self.screen,(255,255,255)
                        ,pygame.Rect(pos.x-self.width/2
                                    ,pos.y-self.height
                                    ,self.width
                                    ,self.height)
                        ,3)
