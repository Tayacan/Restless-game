import pygame
from gamelib.vector2 import Vector2
from gamelib.gameobject import GameObject
from gamelib.collider import *

class Box(GameObject):
    def __init__(self,pos,size):
        GameObject.__init__(self)
        self.position.x = pos[0]
        self.position.y = pos[1]

        self.name = "Box"

        self.width = size[0]
        self.height = size[1]

        self.rect = pygame.Rect(self.position.x - self.width/2
                               ,self.position.y - self.height
                               ,self.width
                               ,self.height)

        self.collider = BoxCollider(self.rect)


    def draw(self,pos,screen):
        pygame.draw.rect(screen,(255,255,255)
                        ,pygame.Rect(pos.x-self.width/2
                                    ,pos.y-self.height
                                    ,self.width
                                    ,self.height)
                        ,3)

class Spikes(GameObject):
    def __init__(self,pos,number,flip=False):
        GameObject.__init__(self)
        self.name = "Spikes"
        self.position = pos
        self.number = number

        self.flip = flip
        self.spikeWidth = 10
        self.spikeHeight = 15
        self.width = self.spikeWidth * number

        # Offset is 0 if the spikes are not flipped, otherwise 15, 
        # so they'll be drawn in the right place.
        self.offset = self.spikeHeight * (not flip)

        self.rect = pygame.Rect(self.position.x-self.width/2
                               ,self.position.y-self.offset
                               ,self.width
                               ,self.spikeHeight)

        self.collider = BoxCollider(self.rect)

    def drawSpike(self,pos,screen):
        left = pos[0]
        y = pos[1] - self.spikeHeight

        # Upside down if they're supposed to be flipped.
        if(self.flip):
            y = pos[1] + self.spikeHeight

        pygame.draw.lines(screen,(100,100,100),False,[(left,pos[1])
                                                     ,(left+self.spikeWidth/2,y)
                                                     ,(left+self.spikeWidth,pos[1])])

    def draw(self,pos,screen):
        left = pos.x-self.width/2
        for n in range(self.number):
            self.drawSpike((left+self.spikeWidth*n,pos.y),screen)

