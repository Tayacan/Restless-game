#!/usr/bin/env python

import sys
import pygame
from gamelib.game import *
from gamelib.gameobject import *
from editorscripts.parselevel import Parser
from editorscripts.screen import Screen

def load(path):
    f = open(path)
    objList = []
    for l in f.readlines():
        objList.append(Parser.parse(l))

    f.close()
    return objList

def save(objList,path):
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))

    objList = []
    if len(sys.argv) == 2:
        objList = load(sys.argv[1])

    c = Camera(screen)
    scene = Scene([Screen(objList)],c)

    Game.start([scene],screen)

if __name__ == "__main__":
    main()
