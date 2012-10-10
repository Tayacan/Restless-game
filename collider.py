from vector2 import Vector2
import math

class Collider:
    def __init__(self):
        pass


class CircleCollider(Collider):
    def __init__(self,radius,center):
        self.radius = radius
        self.center = center

    def pointIn(self,point):
        return Vector2.distance(self.center,point) < self.radius

    def _checkpoints(self):
        points = []
        for n in range(0,361,10):
            p = Vector2(math.sin(math.radians(n))
                       ,math.cos(math.radians(n)))
            p *= self.radius
            points.append(p)

    def collidedWith(self,obj):
        pass
