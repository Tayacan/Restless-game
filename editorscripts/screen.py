import pygame
from pygame.locals import *
from gamelib.gameobject import *
from gamelib.game import Scene
from gamelib.input import Input
from gamelib.gui import GUI
from ball import Ball
from obstacles import *
from powerup import *
from win import WinFlag

class Screen(GameObject):
    def __init__(self,objects=[],save=None):
        GameObject.__init__(self)
        self.objects = objects
        self.save = save

        self.sceneView = pygame.Surface((700,600))
        self.controls = pygame.Surface((100,600))
        self.controls.fill((255,255,255))
        self.camera = Camera(self.sceneView)
        self.camera.position.x = -100

        self.mpos = Vector2(0,0)
        self.scene = Scene(self.objects + [Ball()],self.camera)
        self.selected = None

        self.modes = {"Select":None
                     ,"Move":self.move
                     ,"Scale":self.scale
                     ,"Rotate":None}
        self.mode = "Select"
        self.types = {"Box":self.makeBox
                     ,"Spikes":self.makeSpikes
                     ,"HigherJump":self.makeHigherJump
                     ,"NoJump":self.makeNoJump
                     ,"Win flag":self.makeWinFlag}

    def move(self,v):
        self.selected.translate(v)

    def scale(self,v):
        scaleX = float(v.x) / self.selected.rect.width + 1
        scaleY = float(-v.y) / self.selected.rect.height + 1
        self.selected.scale(Vector2(scaleX,scaleY))

    def add(self,obj):
        self.objects.append(obj)
        self.scene.objects.append(obj)

    def makeWinFlag(self):
        p = self.camera.screenToWorld(Vector2(400,300))
        n = raw_input("Name of next level: ")
        w = WinFlag(p,n)
        self.add(w)

    def makeNoJump(self):
        p = self.camera.screenToWorld(Vector2(400,300))
        j = NoJump(p)
        self.add(j)

    def makeHigherJump(self):
        p = self.camera.screenToWorld(Vector2(400,300))
        j = HigherJump(p)
        self.add(j)

    def makeBox(self):
        p = self.camera.screenToWorld(Vector2(100,100))
        b = Box((p.x,p.y),(100,100))
        self.add(b)

    def makeSpikes(self):
        f = raw_input("Flip? (y/n)")
        flip = 0
        if f.lower() == 'y':
            flip = 1
        s = Spikes(Vector2(0,0),5,flip)
        self.add(s)

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
        GUI.Label(self.mode
                 ,pygame.Rect(20,20,100,30)
                 ,(255,255,255)
                 ,16)
        offset = 0

        for t,f in self.types.iteritems():
            if GUI.Button(t,pygame.Rect(700,offset,100,30)):
                if f is not None:
                    f()
            offset += 30

        if self.save is not None and GUI.Button("Save",pygame.Rect(700,570,100,30)):
            self.save(self.objects)

    def update(self):
        # Change mode
        if Input.down(K_q):
            self.mode = "Select"
        elif Input.down(K_w):
            self.mode = "Move"
        elif Input.down(K_e):
            self.mode = "Scale"
        elif Input.down(K_r):
            self.mode = "Rotate"
        elif Input.down(K_d):
            try:
                self.objects.remove(self.selected)
                self.scene.objects.remove(self.selected)
                self.selected = None
            except:
                pass

        # On click: Selection of objects and updating mouse position.
        if Input.down("MB1"):
            self.mpos = Vector2(Input.mouse_pos[0],Input.mouse_pos[1])
            if not Input.isset(K_LALT):
                sel = False
                for o in self.objects:
                    p = self.camera.screenToWorld(Vector2(*Input.mouse_pos))
                    if o.rect.collidepoint(p.x,p.y):
                        self.selected = o
                        sel = True
                        break
                if not sel:
                    self.selected = None

        # On drag: Moving screen or object
        if Input.motion("MB1"):
            newPos = Vector2(Input.mouse_pos[0],Input.mouse_pos[1])
            move = self.mpos - newPos
            self.mpos = newPos
            if Input.isset(K_LALT):
                self.camera.translate(move)
            elif self.selected is not None:
                if self.modes[self.mode] is not None:
                    self.modes[self.mode](-move)
#                self.selected.translate(-move)

