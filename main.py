#!/usr/bin/env python

import pygame
from pygame.locals import *
from obstacles import *
from gamelib.game import *
from gamelib.collider import BoxCollider
from gamelib.gameobject import Camera
from gamelib.vector2 import Vector2
from gameover import *
from powerup import *
from time import sleep

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

class TestText(GameObject):
    def __init__(self,screen):
        GameObject.__init__(self)
        self.screen = screen
        self.startTime = pygame.time.get_ticks()

    def draw(self,pos):
        self.screen.fill((0,0,0))
        if pygame.font.get_default_font():
            fontname = pygame.font.get_default_font()
            font = pygame.font.SysFont(fontname,50)
            fonts = font.render("Test",True,(255,255,255))
            self.screen.blit(fonts,pygame.Rect(100,100,300,300))

    def update(self):
        if pygame.time.get_ticks() - self.startTime > 2000:
            Game.loadScene(1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))

    player = Ball(screen)
    movespeed = 3

    testBox = Box(screen,(700,500),(100,100))
    ground = Box(screen,(400,610),(1000,110))
    njump = NoJump(screen,Vector2(100,500))
    hjump = HigherJump(screen,Vector2(600,500))
    roof = Box(screen,(500,410),(100,50))
    spikes = Spikes(screen,(500,410),5,True)

    clock = pygame.time.Clock()

    c =  PlatformCamera(player)

    introScene = Scene([TestText(screen)],c)
    gameOverScene = Scene([GameOver(screen)],c,name="GameOver")
    mainScene = Scene([njump,hjump,spikes,testBox,player,ground,roof],c,name="Main")
    Game.start([mainScene,gameOverScene],screen)

    while(True):
        # Limit the framerate
        clock.tick(60)

        # Drawing
        screen.fill((0,0,0))
        game.run()
        pygame.display.flip()

if __name__ == "__main__":
    main()
