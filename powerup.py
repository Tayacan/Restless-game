from gamelib.gameobject import GameObject
from gamelib.vector2 import Vector2
from gamelib.collider import BoxCollider
from ball import Ball
import pygame

class PowerUp(GameObject):
    def __init__(self,screen,pos,color):
        GameObject.__init__(self)
        self.position = pos
        self.size = Vector2(50,10)
        self.rect = pygame.Rect(pos.x-25,pos.y-self.size.y,50,self.size.y)
        self.color = color

        self.collider = BoxCollider(self.rect)

        self.screen = screen

    def draw(self,pos):
        pygame.draw.rect(self.screen,self.color
                        ,pygame.Rect(pos.x-25,pos.y-self.size.y,self.size.x,self.size.y)
                        ,3)
        pygame.draw.rect(self.screen,self.color
                        ,pygame.Rect(pos.x-10
                                    ,pos.y-(self.size.y+2)
                                    ,20,2),1)

class HigherJump(PowerUp):
    def __init__(self,screen,pos):
        PowerUp.__init__(self,screen,pos,(100,100,255))

    def onCollision(self,col,obj):
        if isinstance(obj,Ball):
            obj.jumpspeed = 10

class SuperJump(PowerUp):
    def __init__(self,screen,pos):
        PowerUp.__init__(self,screen,pos,(200,200,0))

    def onCollision(self,col,obj):
        if isinstance(obj,Ball):
            obj.jumpspeed = 20

class NoJump(PowerUp):
    def __init__(self,screen,pos):
        PowerUp.__init__(self,screen,pos,(255,100,100))

    def onCollision(self,col,obj):
        if isinstance(obj,Ball):
            obj.jumpspeed = 0
