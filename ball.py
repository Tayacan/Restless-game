import pygame
from gamelib.vector2 import Vector2
from gamelib.gameobject import GameObject
from gamelib.collider import *

def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    return 0

class Ball(GameObject):
    """The ball that the player controls."""
    def __init__(self,screen):
        # Start out as a basic GameObject, then modify
        GameObject.__init__(self)

        # Starting position and speed
        self.position = Vector2(400,300)
        self.speed = Vector2(0,1)

        self.screen = screen

        self.color = (255,255,255)
        self.radius = 15
        self.lineWidth = 3

        # Woop, colliders are awesome
        self.collider = CircleCollider(self.radius,self.position)

        # Ground level
        # TODO: Replace with proper collision checking
        self.miny = 500

    def draw(self,pos):
        """Draw the player"""
        pygame.draw.circle(self.screen
                          ,self.color
                          ,(int(pos.x)
                           ,int(pos.y))
                          ,self.radius
                          ,self.lineWidth)

    def update(self):
        """Called every frame. Handles
        movement and other state updates."""
        self.translate(self.speed)
        self.collider.center = self.position
        self.speed.y += 0.5

        #if self.lower() >= self.miny:
        #    self.position.y = self.miny-self.radius
        #    self.speed.y = -10

    def onCollision(self,col,obj):
        self.translate(col.minTranslation)
        if sign(col.minTranslation.y) == -1:
            self.speed.y = -10
        elif sign(col.minTranslation.y) == 1:
            self.speed.y = 10

    def lower(self):
        """The lower edge of the balls bounding box,
        for collisions"""
        return self.position.y+self.radius



