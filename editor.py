#!/usr/bin/env python

import sys,os
import pygame
from gamelib.game import *
from gamelib.gameobject import *
from editorscripts.parselevel import Parser
from editorscripts.screen import Screen
from obstacles import *
from powerup import *

def load(path):
    f = open(path,"a+")
    objList = []
    for l in f.readlines():
        objList.append(Parser.parse(l))

    f.close()
    return objList

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    path = ""

    objList = []
    if len(sys.argv) == 2:
        path = sys.argv[1]
        objList = load(sys.argv[1])

    def save(objs):
        f = open(path,'w')
        for o in objs:
            if isinstance(o,Box):
                f.write("Box %d %d %d %d\n" % (o.position.x,o.position.y,o.width,o.height))
            elif isinstance(o,Spikes):
                f.write("Spikes %d %d %d %d\n" % (o.position.x,o.position.y,o.number,int(o.flip)))
            elif isinstance(o,NoJump):
                f.write("NoJump %d %d\n" % (o.position.x,o.position.y))
            elif isinstance(o,HigherJump):
                f.write("HigherJump %d %d\n" % (o.position.x,o.position.y))


        f.close()

    c = Camera(screen)
    scene = Scene([Screen(objList,save)],c)

    Game.start([scene],screen)

if __name__ == "__main__":
    main()
