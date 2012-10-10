from vector2 import Vector2

class GameObject:
    def __init__(self):
        self.position = Vector2(0,0)
        self.rotation = 0

    def translate(self,v):
        self.position += v

    def rotate(self,r):
        self.rotation += r

    def update(self):
        pass
