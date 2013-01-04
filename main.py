#!/usr/bin/env python

import pygame
from pygame.locals import *
from obstacles import *
from gamelib.game import Game
from gamelib.collider import BoxCollider
from gamelib.gameobject import Camera
from gamelib.vector2 import Vector2
from powerup import *

import sys

from ball import *

class PlatformCamera(Camera):
    def __init__(self,player):
        Camera.__init__(self)
        self.player = player

    def update(self):
        self.position.x = self.player.position.x - 400
        if self.worldToScreen(self.player.position).y < 100:
            self.position.y = self.player.position.y - 100
        if self.worldToScreen(self.player.position).y > 500:
            self.position.y = self.player.position.y - 500

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))

    player = Ball(screen)
    movespeed = 3

    testBox = Box(screen,(700,500),(100,100))
    ground = Box(screen,(400,610),(1000,110))
    safety = Box(screen,(400,1000),(2000,100))
    power = HigherJump(screen,Vector2(100,500))
    depower = NoJump(screen,Vector2(250,500))
    spikes = Spikes(screen,(700,400),5)

    clock = pygame.time.Clock()

    c =  PlatformCamera(player)

    game = Game([power,spikes,depower,testBox,player,ground,safety],c)

    while(True):
        # Limit the framerate
        clock.tick(60)

        # Drawing
        screen.fill((0,0,0))
        game.run()
        pygame.display.flip()

if __name__ == "__main__":
    main()
