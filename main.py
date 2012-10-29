#!/usr/bin/env python

import pygame
from pygame.locals import *
from obstacles import Box
from game import Game
from collider import BoxCollider

import sys

from ball import *

def stop():
    pygame.quit()
    sys.exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))

    player = Ball(screen)
    movespeed = 3

    testBox = Box(screen)
    ground = Box(screen)
    ground.position.y = 610
    ground.height = 110
    ground.position.x = 400
    ground.width = 1000
    ground.collider = BoxCollider([Vector2(-10,500)
                                  ,Vector2(810,500)])

    clock = pygame.time.Clock()

    groundlvl = player.miny

    game = Game([testBox,player,ground])

    while(True):
        # Limit the framerate
        clock.tick(60)

        # Event handling
        for e in pygame.event.get():
            if e.type == QUIT:
                stop()
            elif e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    player.speed.x += movespeed
                elif e.key == K_LEFT:
                    player.speed.x -= movespeed
            elif e.type == KEYUP:
                if e.key == K_RIGHT:
                    player.speed.x -= movespeed
                elif e.key == K_LEFT:
                    player.speed.x += movespeed

        # Drawing
        screen.fill((0,0,0))
        game.run()
        pygame.display.flip()

if __name__ == "__main__":
    main()
