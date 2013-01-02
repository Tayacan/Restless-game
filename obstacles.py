import pygame
from gamelib.vector2 import Vector2
from gamelib.gameobject import GameObject
from gamelib.collider import PolyCollider

class Box(GameObject):
    def __init__(self,screen,pos,size):
        GameObject.__init__(self)
        self.position.x = pos[0]
        self.position.y = pos[1]

        self.width = size[0]
        self.height = size[1]

        self.collider = PolyCollider([Vector2(self.position.x - self.width/2,self.position.y)
                                    ,Vector2(self.position.x - self.width/2,self.position.y - self.height)
                                    ,Vector2(self.position.x + self.width/2,self.position.y - self.height)
                                    ,Vector2(self.position.x + self.width/2,self.position.y)])

        self.screen = screen

    def draw(self,pos):
        pygame.draw.rect(self.screen,(255,255,255)
                        ,pygame.Rect(pos.x-self.width/2
                                    ,pos.y-self.height
                                    ,self.width
                                    ,self.height)
                        ,3)
