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

    clock = pygame.time.Clock()

    c =  PlatformCamera(player,screen)

    # Set up the scenes
    winScene = Scene([WinScene()],c,name="WinScene")
    startScreen = Scene([StartScreen("tut1")],c,name="StartScene")
    gameOverScene = Scene([GameOver()],c,name="GameOver")

    tut1 = Scene(editor.load("levels/tutorial/01.lvl")+[player],c,name="tut1")
    tut2 = Scene(editor.load("levels/tutorial/02.lvl")+[player],c,name="tut2")
    tut3 = Scene(editor.load("levels/tutorial/03.lvl")+[player],c,name="tut3")
    tut4 = Scene(editor.load("levels/tutorial/04.lvl")+[player],c,name="tut4")

    lvl1 = Scene(editor.load("levels/lvl1.lvl")+[player],c,name="lvl1")

    # Start the game
    Game.start([startScreen
               ,gameOverScene
               ,winScene
               ,tut1
               ,tut2
               ,tut3
               ,tut4
               ,lvl1],screen)

if __name__ == "__main__":
    main()
