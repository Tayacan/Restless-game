#!/usr/bin/env python
# Plans:
# Read levels from bitmap
# Create proper classes, like a gameobject
# Do something smarter with input.

import pygame
from pygame.locals import *

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

    clock = pygame.time.Clock()

    groundlvl = player.miny

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
        pygame.draw.line(screen,(255,255,255)
                        ,(0,groundlvl)
                        ,(800,groundlvl)
                        ,3)
        #player.draw()
        player.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()
