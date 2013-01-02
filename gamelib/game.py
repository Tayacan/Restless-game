import pygame
from input import *

class Game:
    def __init__(self,objects,camera):
        self.objects = objects
        self.colliders = [o for o in self.objects if o.collider != None]
        self.mainCamera = camera

    def update(self):
        # Handle input
        Input.update_mouse(pygame.mouse.get_pressed(), pygame.mouse.get_pos())
        Input.add_events(pygame.event.get())

        # Update objects
        for o in self.objects:
            o.update()
        self.mainCamera.update()

        # Finish input handling
        Input.update()

    def draw(self):
        for o in self.objects:
            p = self.mainCamera.worldToScreen(o.position)
            o.draw(p)

    def collision(self):
        temp = self.colliders
        for c1 in self.colliders:
            temp = temp[1:]
            for c2 in temp:
                col1 = c1.collider.collision(c2.collider)
                col2 = c2.collider.collision(c1.collider)
                if col1.intersecting or col2.intersecting:
                    c1.onCollision(col1,c2)
                    c2.onCollision(col2,c1)

    def run(self):
        self.update()
        self.collision()
        self.draw()

