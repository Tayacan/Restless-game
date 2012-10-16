#!/usr/bin/env python

import pygame
from pygame.locals import *
from obstacles import Box

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

        # Test new collision stuff
        print player.collider.collision(testBox.collider)

        # Drawing
        screen.fill((0,0,0))
        pygame.draw.line(screen,(255,255,255)
                        ,(0,groundlvl)
                        ,(800,groundlvl)
                        ,3)
        testBox.update()
        player.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()
