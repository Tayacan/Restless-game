import pygame
from vector2 import Vector2
from gameobject import GameObject
from collider import *

class Ball(GameObject):
    def __init__(self,screen):
        GameObject.__init__(self)
        self.position = Vector2(400,300)
        self.speed = Vector2(0,1)

        self.screen = screen

        self.color = (255,255,255)
        self.radius = 15
        self.lineWidth = 3

        self.collider = CircleCollider(self.radius,self.position)

        self.miny = 500

    def draw(self):
        pygame.draw.circle(self.screen
                          ,self.color
                          ,(int(self.position.x)
                           ,int(self.position.y))
                          ,self.radius
                          ,self.lineWidth)

    def update(self):
        self.translate(self.speed)
        self.speed.y += 0.5

        if self.lower() >= self.miny:
            self.position.y = self.miny-self.radius
            self.speed.y = -10

        self.draw()

    # The lower edge of the balls bounding box, for collisions
    def lower(self):
        return self.position.y+self.radius



