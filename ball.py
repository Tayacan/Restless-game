import pygame
from vector2 import Vector2

class Ball:
    def __init__(self,screen):
        self.position = Vector2(400,300)
        self.speed = Vector2(0,0)

        self.screen = screen

        self.color = (255,255,255)
        self.radius = 15
        self.lineWidth = 3

    def draw(self):
        pygame.draw.circle(self.screen
                          ,self.color
                          ,(int(self.position.x)
                           ,int(self.position.y))
                          ,self.radius
                          ,self.lineWidth)

    # Move, relative to current position
    def translate(self,speed):
        self.position.x += speed.x
        self.position.y += speed.y

    # The lower edge of the balls bounding box, for collisions
    def lower(self):
        return self.position.y+self.radius



