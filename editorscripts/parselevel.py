from obstacles import *
from powerup import *
from gamelib.vector2 import Vector2

class Parser:
    @staticmethod
    def parse(text):
        tokens = text.split(" ")
        if tokens[0].lower() == "box":
            x = int(tokens[1])
            y = int(tokens[2])
            w = int(tokens[3])
            h = int(tokens[4])
            return Box((x,y),(w,h))
        elif tokens[0].lower() == "nojump":
            x = int(tokens[1])
            y = int(tokens[2])
            return NoJump(Vector2(x,y))
        elif tokens[0].lower() == "higherjump":
            x = int(tokens[1])
            y = int(tokens[2])
            return HigherJump(Vector2(x,y))
        elif tokens[0].lower() == "spikes":
            x = int(tokens[1])
            y = int(tokens[2])
            n = int(tokens[3])
            flip = bool(int(tokens[4]))
            return Spikes(Vector2(x,y),n,flip)
