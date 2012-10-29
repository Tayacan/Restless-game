from vector2 import Vector2
import math

# Holds information about a collision
class Collision:
    def __init__(self):
        self.intersecting = False
        self.willIntersect = False
        self.minTranslation = Vector2(0,0)

    def __str__(self):
        return "Intersecting: " + str(self.intersecting) + "\nV: " + str(self.minTranslation)

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

    def collision(self,other):
        col = Collision()
        if other.__class__.__name__ == 'BoxCollider':
            for line in other.getLines():
                c,intersects = self.lineIntersects(line[0],line[1])
                if intersects:
                    col.intersecting = True
                    r = c - self.center
                    m = r.clampMagnitude(self.radius - r.magnitude()) * -1
                    col.minTranslation = m

        return col



class BoxCollider(Collider):
    def __init__(self,points):
        self.points = points

    def getLines(self):
        l = []
        for i in range(0,len(self.points)):
            i2 = i+1
            if i2 == len(self.points): i2 = 0
            l.append((self.points[i],self.points[i2]))

        return l

    def collision(self,other):
        # TODO
        return Collision()
