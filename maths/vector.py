# TODO: cross product.
# TODO: generic normalize function
# TODO: template generic/single-dimensional vector class

import math

def sqr(n):
    return n*n
# static dot product function.
def dot(a, b):
    return (a*b).sum()
# static cross product function
def cross(a, b):
    return Vec3((a.y * b.z) - (a.z * b.y),
                (a.z*b.x) - (a.x*b.z),
                (a.x*b.y) - (a.y*b.x))

# three dimensional vector class
class Vec3(object):
    def __init__(self, *args):
        if len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
        elif len(args) == 1:
            if type(args[0]) == float:
                self.x=self.y=self.z=args[0]
            elif type(args[0]) == Vec3:
                self.x = args[0].x
                self.y = args[0].y
                self.z = args[0].z

    def __truediv__(self, other):
        if type(other)==Vec3:
            return Vec3(self.x / other.x,
                        self.y / other.y,
                        self.z / other.z)
        elif type(other)==float:
            return Vec3(self.x / other,
                        self.y / other,
                        self.z / other)

    def __idiv__(self, other):
        self.x /= other
        self.y /= other
        self.z /= other

    def __mul__(self, other):
        if type(other)==Vec3:
            return Vec3(self.x * other.x,
                        self.y * other.y,
                        self.z * other.z)
        else:
            return Vec3(self.x * other,
                        self.y * other,
                        self.z * other)

    def __add__(self, other):
        if type(other)==Vec3:
            return Vec3(self.x + other.x,
                        self.y + other.y,
                        self.z + other.z)
        elif type(other)==float:
            return Vec3(self.x + other,
                        self.y + other,
                        self.z + other)

    def __sub__(self, other):
        return Vec3(self.x - other.x,
                    self.y - other.y,
                    self.z - other.z)

    def __eq__(self, other):
        self.x = other.x
        self.y = other.y
        self.z = other.z

    def sum(self):
        return self.x + self.y + self.z

    def len(self):
        return math.sqrt(math.pow(self.x, 2) +
                         math.pow(self.y, 2) +
                         math.pow(self.z, 2))

    def len2(self):
        return math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2)

    def normalized(self):
        l = self.len()
        v = Vec3(self)
        if self.x != 0.0:
            v.x = self.x / l
        if self.y != 0.0:
            v.y = self.y / l
        if self.z != 0.0:
            v.z = self.z / l
        return v

    def normalize(self):
        l = self.len()
        if self.x!=0.0:
            self.x /= l
        if self.y!=0.0:
            self.y /= l
        if self.z!=0.0:
            self.z /= l
        return self

    def cross(self, other):
        self.x = (self.y * other.z) - (self.z * other.y)
        self.y = (self.z * other.x) - (self.x * other.z)
        self.z = (self.x * other.y) - (self.y * other.x)
        return self


class Vec2(object):
    def __init__(self, *args):
        if len(args) == 2 and type(args[0]):
            self.x = args[0]
            self.y = args[1]

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mod__(self, other):
        return Vec2(self.x % other.x, self.y % other.y)
