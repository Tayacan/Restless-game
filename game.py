import pygame

class Game:
    def __init__(self,objects):
        self.objects = objects
        self.colliders = [o for o in self.objects if o.collider != None]

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw()

    def collision(self):
        temp = self.colliders
        for c1 in self.colliders:
            temp = temp[1:]
            for c2 in temp:
                col1 = c1.collider.collision(c2.collider)
                col2 = c2.collider.collision(c1.collider)
                if col1.intersecting:
                    c1.onCollision(col1,c2)
                if col2.intersecting:
                    c2.onCollision(col2,c1)

    def run(self):
        self.update()
        self.collision()
        self.draw()
