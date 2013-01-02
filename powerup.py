from gamelib.gameobject import GameObject
from gamelib.vector2 import Vector2
from gamelib.collider import BoxCollider
from ball import Ball
import pygame

class HigherJump(GameObject):
    def __init__(self,screen,pos):
        GameObject.__init__(self)
        self.position = pos
        self.size = Vector2(50,20)
        self.rect = pygame.Rect(pos.x-25,pos.y-20,50,20)

        self.collider = BoxCollider(self.rect)

        self.screen = screen

    def draw(self,pos):
        pygame.draw.rect(self.screen,(200,200,255)
                        ,pygame.Rect(pos.x-25,pos.y-20,self.size.x,self.size.y)
                        ,3)
        pygame.draw.rect(self.screen,(200,200,255)
                        ,pygame.Rect(pos.x-10
                                    ,pos.y-22
                                    ,20,2),1)

    def onCollision(self,col,obj):
        if isinstance(obj,Ball):
            obj.jumpspeed = 10
