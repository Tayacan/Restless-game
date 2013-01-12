#!/usr/bin/env python

import pygame
import editor
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
    def __init__(self,player,screen):
        Camera.__init__(self,screen)
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

    player = Ball()
    movespeed = 3

    testBox = Box((700,500),(100,100))
    ground = Box((400,610),(1000,110))
    njump = NoJump(Vector2(100,500))
    hjump = HigherJump(Vector2(610,500))
    roof = Box((475,410),(200,50))
    spikes = Spikes(Vector2(475,410),15,True)
    win = WinFlag(Vector2(475,335))

    clock = pygame.time.Clock()

    c =  PlatformCamera(player,screen)

    # Set up the scenes
    level0Objs = editor.load("levels/test.lvl")
    level0 = Scene(level0Objs + [player],c,name="Level0")
    winScene = Scene([WinScene()],c,name="WinScene")
    startScreen = Scene([StartScreen()],c,name="StartScene")
    gameOverScene = Scene([GameOver()],c,name="GameOver")
    mainScene = Scene([njump,hjump,spikes,win,testBox,player,ground,roof],c,name="Main")

    # Start the game
    Game.start([startScreen,mainScene,gameOverScene,winScene,level0],screen)

if __name__ == "__main__":
    main()
