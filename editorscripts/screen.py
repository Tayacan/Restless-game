import pygame
from gamelib.gameobject import *
from gamelib.game import Scene
from gamelib.input import Input
from gamelib.gui import GUI
from ball import Ball
from obstacles import *

class Screen(GameObject):
    def __init__(self,objects=[]):
        GameObject.__init__(self)
        self.objects = objects

        self.sceneView = pygame.Surface((700,600))
        self.controls = pygame.Surface((100,600))
        self.controls.fill((255,255,255))
        self.camera = Camera(self.sceneView)
        self.camera.position.x = -100

        self.mpos = Vector2(0,0)

        self.scene = Scene(self.objects + [Ball()],self.camera)

        self.selected = None

        self.types = {"Box":self.makeBox
                     ,"Spikes":None
                     ,"HigherJump":None
                     ,"NoJump":None}

    def makeBox(self):
        b = Box((0,0),(100,100))
        self.objects.append(b)
        self.scene.objects.append(b)

    def draw(self,pos,screen):
        self.sceneView.fill((0,0,0))
        self.scene.draw()
        if self.selected is not None:
            p = Vector2(self.selected.rect.left,self.selected.rect.top)
            self.selected.fillRect(self.camera.worldToScreen(p),self.sceneView)

        screen.blit(self.sceneView
                   ,pygame.Rect(pos.x
                               ,pos.y
                               ,self.sceneView.get_width()
                               ,screen.get_height()))

        screen.blit(self.controls
                   ,pygame.Rect(pos.x+700
                               ,pos.y
                               ,100
                               ,screen.get_height()))

    def onGUI(self):
        offset = 0
        for o in self.objects:
            if(GUI.Button(o.name,pygame.Rect(700,offset,100,30))):
                self.selected = o
            offset += 30

        offset += 30
        for t,f in self.types.iteritems():
            if GUI.Button(t,pygame.Rect(700,offset,100,30)):
                if f is not None:
                    f()
            offset += 30

    def update(self):
        if Input.down("MB1"):
            self.mpos = Vector2(Input.mouse_pos[0],Input.mouse_pos[1])
            sel = False
            for o in self.objects:
                p = self.camera.screenToWorld(Vector2(*Input.mouse_pos))
                if o.rect.collidepoint(p.x,p.y):
                    self.selected = o
                    sel = True
                    break
            if not sel:
                self.selected = None

        if Input.motion("MB1"):
            newPos = Vector2(Input.mouse_pos[0],Input.mouse_pos[1])
            move = self.mpos - newPos
            self.mpos = newPos
            if self.selected is None:
                self.camera.translate(move)
            else:
                self.selected.translate(-move)

