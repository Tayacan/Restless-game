import pygame
from os import path
from pygame.locals import *
from gamelib.vector2 import Vector2
from gamelib.gameobject import GameObject
from gamelib.collider import *
from gamelib.input import Input
from gamelib.game import Game
from obstacles import *
from gameover import GameOver

def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    return 0

def lerp(n,m,t):
    return n + (m - n) * t

class Ball(GameObject):
    """The ball that the player controls."""
    def __init__(self):
        # Start out as a basic GameObject, then modify
        GameObject.__init__(self)

        self.name = "Player"

        self.color = (255,255,255)
        self.radius = 15
        self.lineWidth = 3

        self.movespeed = 3
        self.startJumpspeed = 7

        # Woop, colliders are awesome
        self.collider = CircleCollider(self.radius,self.position)

        # Sound effects
        pygame.mixer.quit()
        pygame.mixer.pre_init(44100, -16, 2)
        pygame.mixer.init()
        mpath = path.join("sound","bounce.ogg")
        self.bounce = pygame.mixer.Sound(mpath)

        self.onLoad()

    def onLoad(self):
        # Starting position and speed
        self.position = Vector2(0,300)
        self.speed = Vector2(0,1)

        # Fix speed
        if Input.isset(K_LEFT):
            self.speed.x -= self.movespeed
        if Input.isset(K_RIGHT):
            self.speed.x += self.movespeed

        self.jumpspeed = self.startJumpspeed
        if Game.currentScene:
            GameOver.currentScene = Game.currentScene.name

    def draw(self,pos,screen):
        """Draw the player"""
        pygame.draw.circle(screen
                          ,self.color
                          ,(int(pos.x)
                           ,int(pos.y))
                          ,self.radius
                          ,self.lineWidth)

    def update(self):
        """Called every frame. Handles
        movement and other state updates."""

        if Input.down(K_LEFT):
            self.speed.x -= self.movespeed
        if Input.up(K_LEFT):
            self.speed.x += self.movespeed
        if Input.down(K_RIGHT):
            self.speed.x += self.movespeed
        if Input.up(K_RIGHT):
            self.speed.x -= self.movespeed

        self.jumpspeed = lerp(self.jumpspeed,self.startJumpspeed,0.02)

        self.translate(self.speed)
        self.collider.center = self.position
        self.speed.y += 0.5

        if self.position.y >= 1000:
            Game.loadSceneByName("GameOver")

    def onCollision(self,col,obj):
        nobounce = ["NoJump","WinStar"]

        if obj.name not in nobounce:
            channel = self.bounce.play()

        # Bounce off the object
        self.translate(col.minTranslation)
        if sign(col.minTranslation.y) == -1:
            self.speed.y = -self.jumpspeed
        elif sign(col.minTranslation.y) == 1:
            self.speed.y = self.jumpspeed

        if obj.name == "Spikes":
            Game.loadSceneByName("GameOver")



