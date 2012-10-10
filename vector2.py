import math

class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # Operators and smart build-ins
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self,other):
        return Vector2(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Vector2(self.x-other.x,self.y-other.y)

    def __mul__(self,x):
        return Vector2(self.x*x,self.y*x)

    # Basic vector operations
    def sqrtMagnitude(self):
        return self.x * self.x + self.y * self.y

    def magnitude(self):
        return math.sqrt(self.sqrtMagnitude())

    def normalized(self):
        return Vector2(self.x / self.magnitude(),self.y / self.magnitude())

    def min(a,b):
        return Vector2(min(a.x,b.x),min(a.y,b.y))

    def max(a,b):
        return Vector2(max(a.x,b.x),max(a.y,b.y))

    # Utility functions
    def distance(a,b):
        return (a-b).magnitude()

    def clampMagnitude(self,m):
        return self.normalized * m

    def lerp(fromv,tov,t):
        return Vector2(fromv.x + (tov.x-fromv.x)*t
                      ,fromv.y + (tov.y-fromv.y)*t)


