#!/usr/bin/env python

import pygame
from pygame.locals import *
from obstacles import *
from gamelib.game import *
from gamelib.collider import BoxCollider
from gamelib.gameobject import Camera
from gamelib.vector2 import Vector2
from gameover import *
from startscreen import *
from win import *
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))

    player = Ball(screen)
    movespeed = 3

    # Make some things
    testBox = Box(screen,(700,500),(100,100))
    ground = Box(screen,(400,610),(1000,110))
    njump = NoJump(screen,Vector2(100,500))
    hjump = HigherJump(screen,Vector2(610,500))
    roof = Box(screen,(475,410),(200,50))
    spikes = Spikes(screen,(475,410),15,True)
    win = WinFlag(screen,Vector2(475,335))

    clock = pygame.time.Clock()

    c =  PlatformCamera(player)

    # Set up the scenes
    winScene = Scene([WinScene(screen)],c,name="WinScene")
    startScreen = Scene([StartScreen(screen)],c,name="StartScene")
    gameOverScene = Scene([GameOver(screen)],c,name="GameOver")
    mainScene = Scene([njump,hjump,spikes,win,testBox,player,ground,roof],c,name="Main")
    
    # Start the game
    Game.start([startScreen,mainScene,gameOverScene,winScene],screen)

if __name__ == "__main__":
    main()
