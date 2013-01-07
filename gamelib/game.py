import pygame
import sys
from input import *

class Game:
    scenes = []
    currentScene = None
    screen = None
    clock = pygame.time.Clock()

    @staticmethod
    def start(scenes,screen):
        Game.screen = screen
        Game.scenes = scenes
        Game.currentScene = scenes[0]
        Game.runGame()

    @staticmethod
    def loadScene(n):
        Game.currentScene = Game.scenes[n]
        Game.currentScene.onLoad()

    @staticmethod
    def loadSceneByName(name):
        for scene in Game.scenes:
            if scene.name == name:
                Game.currentScene = scene
                Game.currentScene.onLoad()
                return
        print("No such scene")

    @staticmethod
    def runGame():
        while(True):
            Game.clock.tick(60)

            Game.screen.fill((0,0,0))
            Game.currentScene.run()
            pygame.display.flip()

class Scene:
    num = 0
    names = []
    def __init__(self,objects,camera,screen,name="Scene"):
        # Give each scene a unique name
        if name in Scene.names:
            name += str(num)
            num += 1
        self.name = name
        Scene.names.append(name)

        self.objects = objects
        self.mainCamera = camera
        self.screen = screen
        self.colliders = [o for o in self.objects if o.collider != None]

    def onLoad(self):
        for o in self.objects:
            o.onLoad()
        self.mainCamera.onLoad()

    def update(self):
        # Handle input
        Input.update_mouse(pygame.mouse.get_pressed(), pygame.mouse.get_pos())
        Input.add_events(pygame.event.get())

        if Input.isset("QUIT"):
            pygame.quit()
            sys.exit()

        # Update objects
        for o in self.objects:
            o.update()
        self.mainCamera.update()

        # Finish input handling
        Input.update()

    def draw(self):
        for o in self.objects:
            p = self.mainCamera.worldToScreen(o.position)
            o.draw(p,self.screen)

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
