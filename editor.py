#!/usr/bin/env python

import sys
import pygame
from gamelib.game import *
from gamelib.gameobject import *
from editor.parselevel import Parser
from editor.screen import Screen

def load(path,screen):
    f = open(path)
    objList = []
    for l in f.readlines():
        objList.append(Parser.parse(l,screen))

    return objList

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))

    objList = []
    if len(sys.argv) == 2:
        objList = load(sys.argv[1],screen)

    scene = Scene([Screen(screen,objList)],Camera())

    Game.start([scene],screen)

if __name__ == "__main__":
    main()
