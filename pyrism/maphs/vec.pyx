from math import sqrt

def sqr(x):
    return x*x

cdef struct vec2f:
    float x, y

cdef class Vector2f:
    cdef public float x, y
    def __init__(self, float x=0., float y=0.):
        self.x, self.y = x, y
    def __truediv__(self, float other):
        return Vector2f(self.x / other, self.y / other)
    def __mul__(self, float other):
        return Vector2f(self.x * other, self.y * other)
    def __add__(self, Vector2f other):
        return Vector2f(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2f(self.x - other.x, self.y - other.y)

    def __len__(self):
        return sqrt(sqr(self.x) + sqr(self.y))


cdef struct vec3f:
    float x, y, z

cdef class Vector3f:
    cdef public float x, y, z
    def __init__(self, float x=0., float y=0., float z=0.):
        self.x, self.y, self.z = x, y, z
    def __truediv__(self, float other):
        return Vector3f(self.x / other, self.y / other, self.z / other)
    def __mul__(self, float other):
        return Vector3f(self.x * other, self.y * other, self.z * other)
    def __add__(self, Vector3f other):
        return Vector3f(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, Vector3f other):
        return Vector3f(self.x - other.x, self.y - other.y, self.z - other.z)

    def __len__(self):
        return sqrt(sqr(self.x) + sqr(self.y) + sqr(self.z))
ctypedef Vector3f Point
