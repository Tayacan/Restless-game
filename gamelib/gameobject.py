from vector2 import Vector2

class GameObject:
    def __init__(self):
        self.position = Vector2(0,0)
        self.rotation = 0
        self.collider = None

    def translate(self,v):
        self.position += v

    def rotate(self,r):
        self.rotation += r

    def update(self):
        pass

    def draw(self,pos):
        pass

    def onCollision (self,collision,obj):
        pass

class Camera(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        #self.screen = screen

    def screenToWorld(self,v):
        return v + self.position

    def worldToScreen(self,v):
        return v - self.position

