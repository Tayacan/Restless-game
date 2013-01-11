from vector2 import Vector2
import pygame

class GameObject:
    def __init__(self):
        self.position = Vector2(0,0)
        self.rotation = 0
        self.collider = None
        self.name = "Object"
        self.rect = pygame.Rect(0,0,0,0)

    def fillRect(self,pos,screen):
        surface = pygame.Surface((self.rect.width,self.rect.height),pygame.SRCALPHA)
        surface.fill(pygame.Color(255,255,255,55))
        screen.blit(surface,(pos.x,pos.y))

    def translate(self,v):
        self.position += v

    def rotate(self,r):
        self.rotation += r

    def onLoad(self):
        pass

    def update(self):
        pass

    def draw(self,pos,screen):
        pass

    def onGUI(self):
        pass

    def onCollision (self,collision,obj):
        pass

class Camera(GameObject):
    def __init__(self,screen):
        GameObject.__init__(self)
        self.screen = screen

    def screenToWorld(self,v):
        return v + self.position

    def worldToScreen(self,v):
        return v - self.position


