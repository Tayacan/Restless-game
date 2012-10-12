from vector2 import Vector2
import math

# Holds information about a collision
class Collision:
    def __init__(self):
        self.intersecting = False
        self.willIntersect = False
        self.minTranslation = Vector2(0,0)

# A collider for a GameObject
class Collider:
    def __init__(self):
        pass


class CircleCollider(Collider):
    def __init__(self,radius,center):
        self.radius = radius
        self.center = center

    def pointIn(self,point):
        return Vector2.distance(self.center,point) < self.radius

    def lineIntersects(self,A,B):
        v = B - A
        w = self.center - A
        t = Vector2.dot(v,w) / Vector2.dot(v,v)
        if t > 1:
            t = 1
        elif t < 0:
            t = 0
        closest = A + (v*t)
        return closest,self.pointIn(closest)
