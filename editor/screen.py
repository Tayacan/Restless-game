import pygame
from gamelib.gameobject import *
from gamelib.game import Scene
from gamelib.input import Input
from ball import Ball

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

    def draw(self,pos,screen):
        self.sceneView.fill((0,0,0))
        self.scene.draw()

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

    def update(self):
        if Input.down("MB1"):
            self.mpos = Vector2(Input.mouse_pos[0],Input.mouse_pos[1])
        if Input.motion("MB1"):
            newPos = Vector2(Input.mouse_pos[0],Input.mouse_pos[1])
            move = self.mpos - newPos
            self.mpos = newPos
            self.camera.translate(move)
