import pygame

class Game:
    def __init__(self,objects):
        self.objects = objects

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw()

    def run(self):
        self.update()
        self.draw()
